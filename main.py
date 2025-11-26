#!/usr/bin/env python3
"""
B CLI Tool - Universal Workflow Agent

A command-line interface that prepends b.md content to any prompt
and processes it through Claude.
"""

import argparse
import subprocess
import sys
import os
from pathlib import Path


def read_bmd():
    """Read the b.md file content."""
    bmd_path = Path(__file__).parent / "b.md"
    if not bmd_path.exists():
        print("Error: b.md file not found in the same directory as the script")
        sys.exit(1)

    with open(bmd_path, 'r', encoding='utf-8') as f:
        return f.read()


def run_claude(prompt):
    """Run Claude with the given prompt."""
    try:
        # Try to run claude command with prompt as stdin
        process = subprocess.Popen(
            ['claude'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stdout, stderr = process.communicate(input=prompt)
        
        if process.returncode == 0:
            print(stdout)
        else:
            print(f"Error running Claude: {stderr}")
            sys.exit(1)
    except FileNotFoundError:
        print("Error: 'claude' command not found. Please make sure Claude CLI is installed and in PATH.")
        sys.exit(1)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="B CLI - Universal Workflow Agent",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  b "Create a REST API for user management"
  b --3 "Design a database schema for e-commerce"
  b -b "Analyze the performance of this algorithm"
        """
    )

    parser.add_argument(
        'prompt',
        help='The prompt to process (enclosed in quotes if contains spaces)'
    )

    parser.add_argument(
        '--3',
        action='store_true',
        help='Generate three alternative solutions'
    )

    parser.add_argument(
        '-b',
        action='store_true',
        help='Spawn sub-agents in background'
    )

    args = parser.parse_args()

    # Read b.md content
    bmd_content = read_bmd()

    # Build the enhanced prompt
    enhanced_prompt = f"{bmd_content}\n\n{args.prompt}"

    # Add modificators to prompt if specified
    if getattr(args, '3'):
        enhanced_prompt += "\n\n--3 modificator enabled: Generate three alternative solutions"

    if args.b:
        enhanced_prompt += "\n\n-b modificator enabled: Spawn sub-agents in background"

    print(f"B CLI - Processing prompt with b.md content...")
    print(f"Modified prompt length: {len(enhanced_prompt)} characters")
    print("-" * 50)

    # Run Claude with the enhanced prompt
    run_claude(enhanced_prompt)


if __name__ == "__main__":
    main()