#!/bin/bash
# Development installation script for B CLI tool
# Installs in editable mode - updates automatically when code changes

echo "Installing B CLI tool in development mode (auto-updates)..."
echo "This means changes to the code will be reflected immediately!"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
    echo "Error: pip is required but not installed."
    exit 1
fi

# Install the package in editable mode (-e)
if command -v pip3 &> /dev/null; then
    pip3 install -e .
else
    pip install -e .
fi

# Check if installation was successful
if command -v b &> /dev/null; then
    echo "✅ B CLI tool installed in development mode!"
    echo ""
    echo "🚀 AUTO-UPDATE ENABLED: Any changes to the code will be available immediately!"
    echo ""
    echo "Usage examples:"
    echo '  b "Create a REST API for user management"'
    echo '  b --3 "Design a database schema for e-commerce"'
    echo '  b -b "Analyze the performance of this algorithm"'
    echo '  b --update "Update to latest version from GitHub"'
    echo ""
    echo "Run 'b --help' for more options."
else
    echo "❌ Installation failed. Please check your PATH and try installing manually with:"
    echo "  pip install -e ."
fi