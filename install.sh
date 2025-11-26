#!/bin/bash
# Installation script for B CLI tool

echo "Installing B CLI tool globally..."

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

# Install the package
if command -v pip3 &> /dev/null; then
    pip3 install .
else
    pip install .
fi

# Check if installation was successful
if command -v b &> /dev/null; then
    echo "✅ B CLI tool installed successfully!"
    echo ""
    echo "Usage examples:"
    echo '  b "Create a REST API for user management"'
    echo '  b --3 "Design a database schema for e-commerce"'
    echo '  b -b "Analyze the performance of this algorithm"'
    echo ""
    echo "Run 'b --help' for more options."
else
    echo "❌ Installation failed. Please check your PATH and try installing manually with:"
    echo "  pip install ."
fi