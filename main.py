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


def update_from_github():
    """Update CLI to latest version from GitHub."""
    print("🔄 Checking for updates from GitHub...")
    
    try:
        # Get the directory where this script is located
        script_dir = Path(__file__).parent
        
        # Run git pull to update
        result = subprocess.run(
            ['git', '-C', str(script_dir), 'pull', 'origin', 'main'],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✅ Successfully updated from GitHub!")
            print("Changes applied:")
            print(result.stdout)
        else:
            print("❌ Failed to update from GitHub:")
            print(result.stderr)
            
    except FileNotFoundError:
        print("❌ Git not found. Please install git to use auto-update feature.")
    except Exception as e:
        print(f"❌ Error during update: {e}")

def init_workflow_symlinks():
    """Initialize b.md symlinks in Windsurf and Claude Code workflow folders."""
    print("🔗 Initializing b.md workflow symlinks...")
    
    # Get the directory where this script and b.md are located
    script_dir = Path(__file__).parent
    bmd_source = script_dir / "b.md"
    
    if not bmd_source.exists():
        print(f"❌ Error: b.md not found at {bmd_source}")
        return
    
    # Common workflow folders for Windsurf and Claude Code
    workflow_paths = [
        Path.home() / ".windsurf" / "workflows",
        Path.home() / ".claude" / "workflows", 
        Path.home() / ".claude-code" / "workflows",
        Path.home() / ".config" / "windsurf" / "workflows",
        Path.home() / ".config" / "claude" / "workflows",
        # Windows equivalent paths
        Path.home() / "AppData" / "Local" / "Windsurf" / "workflows",
        Path.home() / "AppData" / "Local" / "Claude" / "workflows",
    ]
    
    success_count = 0
    
    for workflow_dir in workflow_paths:
        if workflow_dir.exists():
            try:
                # Create the symlink
                symlink_target = workflow_dir / "b.md"
                
                # Remove existing symlink if it exists
                if symlink_target.exists() or symlink_target.is_symlink():
                    symlink_target.unlink()
                
                # Create new symlink
                symlink_target.symlink_to(bmd_source)
                print(f"✅ Created symlink: {symlink_target} -> {bmd_source}")
                success_count += 1
                
            except Exception as e:
                print(f"⚠️  Could not create symlink in {workflow_dir}: {e}")
        else:
            # Try to create the directory and then symlink
            try:
                workflow_dir.mkdir(parents=True, exist_ok=True)
                symlink_target = workflow_dir / "b.md"
                symlink_target.symlink_to(bmd_source)
                print(f"✅ Created directory and symlink: {symlink_target} -> {bmd_source}")
                success_count += 1
            except Exception as e:
                print(f"⚠️  Could not create directory/symlink in {workflow_dir}: {e}")
    
    if success_count > 0:
        print(f"\n🎉 Successfully initialized {success_count} workflow symlink(s)!")
        print("\n📋 Integration complete! b.md workflow rules will now be available in:")
        print("   • Windsurf workflows")
        print("   • Claude Code workflows")
        print("\n💡 You may need to restart Windsurf/Claude Code for changes to take effect.")
    else:
        print("\n⚠️  No workflow directories found or created.")
        print("💡 You can manually create symlinks to b.md in your preferred workflow locations.")

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
  b --update "Update to latest version from GitHub"
  b init "Initialize b.md workflow symlinks"
        """
    )

    parser.add_argument(
        'prompt',
        nargs='?',
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

    parser.add_argument(
        '--update',
        action='store_true',
        help='Update to latest version from GitHub'
    )

    parser.add_argument(
        'init',
        nargs='?',
        const='init',
        help='Initialize b.md workflow symlinks for Windsurf/Claude Code'
    )

    args = parser.parse_args()

    # Handle init command
    if args.prompt == 'init' or args.init == 'init':
        init_workflow_symlinks()
        return

    # Handle update command
    if args.update:
        update_from_github()
        return

    # Require prompt if not updating or initializing
    if not args.prompt:
        parser.error("Prompt is required when not using --update or init")

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