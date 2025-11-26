#!/usr/bin/env python3
"""
Setup script for B CLI Tool
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README file
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding='utf-8') if readme_path.exists() else ""

setup(
    name="b-cli",
    version="1.0.0",
    description="B CLI - Universal Workflow Agent",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Biliboss",
    py_modules=["main"],
    python_requires=">=3.6",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "b=main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)