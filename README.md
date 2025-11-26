# B CLI - Universal Workflow Agent

B is a command-line interface that acts as a universal workflow agent by prepending `b.md` content to any prompt and processing it through Claude.

## Features

- **Universal Workflow**: Integrates `b.md` workflow rules with any prompt
- **Modificators**: Supports special flags for enhanced functionality
  - `--3`: Generate three alternative solutions
  - `-b`: Spawn sub-agents in background
- **Global Installation**: Available system-wide after installation

## Installation

### Quick Install
```bash
git clone <repository>
cd b
chmod +x install.sh
./install.sh
```

### Manual Install
```bash
pip install .
```

### Development Install
```bash
pip install -e .
```

## Usage

### Basic Usage
```bash
b "Create a REST API for user management"
```

### With Modificators

#### Generate Three Alternative Solutions (`--3`)
```bash
b --3 "Design a database schema for e-commerce"
```

#### Background Sub-agents (`-b`)
```bash
b -b "Analyze the performance of this algorithm"
```

#### Combined Modificators
```bash
b --3 -b "Create a microservices architecture"
```

## Requirements

- Python 3.6 or higher
- Claude CLI tool (`claude` command must be in PATH)
- pip package manager

## How It Works

1. **Reads b.md**: The CLI reads the content of `b.md` file
2. **Enhances Prompt**: Prepends `b.md` content to your prompt
3. **Processes via Claude**: Sends the enhanced prompt to Claude CLI
4. **Returns Results**: Displays Claude's response

## File Structure

```
b/
├── main.py           # Main CLI implementation
├── b.md              # Workflow rules and instructions
├── setup.py          # Package setup configuration
├── install.sh        # Installation script
└── README.md         # This file
```

## Troubleshooting

### Claude Command Not Found
Make sure the Claude CLI is installed and in your system PATH:
```bash
which claude
```

### Permission Denied
Make the installation script executable:
```bash
chmod +x install.sh
```

### Python Not Found
Ensure Python 3 is installed:
```bash
python3 --version
```

## Development

To modify or extend the CLI:

1. Edit `main.py` for core functionality
2. Edit `b.md` for workflow rules
3. Update `setup.py` for package configuration
4. Test with `python -m main "test prompt"`

## License

MIT License