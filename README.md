# Password Generator

## Secure password generator with strength analysis, custom rules, and CLI interface.

### Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
    - [Basic Generation](#basic-generation)
    - [Custom Length](#custom-length)
    - [Including/Excluding Character Types](#includingexcluding-character-types)
    - [Custom Character Sets](#custom-character-sets)
    - [Strength Analysis](#strength-analysis)
    - [Help](#help)
- [Development](#development)
- [Testing](#testing)
- [License](#license)

## Features
- **Secure Generation**: Utilizes Python's `secrets` module for cryptographically strong random number generation, ensuring high-quality entropy.
- **Customizable Length**: Generate passwords of any desired length, from short PINs to very long passphrases.
- **Character Type Control**: Fine-tune your password by including or excluding uppercase letters, lowercase letters, digits, and symbols.
- **Custom Character Sets**: Define your own pool of characters for highly specific requirements, overriding default character types.
- **Password Strength Analysis**: Get an immediate assessment of the generated password's strength, helping you understand its resilience against brute-force attacks.
- **CLI Interface**: Easy-to-use command-line interface for quick and efficient password generation directly from your terminal.

## Tech Stack
- **Python**: The core language for the application logic.
- `secrets`: Python's built-in module for generating cryptographically strong random numbers, crucial for secure password generation.
- `argparse`: Used for building a robust and user-friendly command-line interface, handling arguments and options.
- `setuptools`/`hatch`: (Implied by `pyproject.toml`) For project packaging, dependency management, and making the `pwdgen` command available system-wide.

## Installation

To get started with the Password Generator, follow these steps:

1.  **Clone the repository:**
    First, clone the project repository to your local machine:
    ```bash
    git clone https://github.com/your-username/password-generator.git
    cd password-generator
    ```
    (Replace `your-username` with the actual GitHub username or organization if applicable).

2.  **Create and activate a virtual environment (recommended):**
    It's best practice to install Python projects within a virtual environment to avoid conflicts with system-wide packages.
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install the project in editable mode with its dependencies:**
    This command installs the `pwdgen` package and all its required dependencies, making the `pwdgen` command-line tool accessible in your terminal while allowing for local development.
    ```bash
    pip install -e .
    ```

## Usage

The `pwdgen` command provides a flexible way to generate passwords with various options.

### Basic Generation

Generate a password with default settings (typically 12 characters, including uppercase, lowercase, digits, and symbols).

```bash
pwdgen
```

### Custom Length

Specify the desired length of the password using the `-l` or `--length` option.

```bash
pwdgen -l 16
pwdgen --length 20
```

### Including/Excluding Character Types

Control which types of characters are included or excluded in the generated password.

-   `--no-upper`: Exclude uppercase letters.
-   `--no-lower`: Exclude lowercase letters.
-   `--no-digits`: Exclude digits.
-   `--no-symbols`: Exclude symbols.
-   `--only-upper`: Only include uppercase letters (implies excluding others).
-   `--only-lower`: Only include lowercase letters (implies excluding others).
-   `--only-digits`: Only include digits (implies excluding others).
-   `--only-symbols`: Only include symbols (implies excluding others).

You can combine exclusion options. For example, to generate a 10-character password with only lowercase letters and digits:

```bash
pwdgen -l 10 --no-upper --no-symbols
# Alternatively, using 'only' flags for clarity:
pwdgen -l 10 --only-lower --only-digits
```

To generate a password consisting solely of symbols:

```bash
pwdgen -l 8 --only-symbols
```

### Custom Character Sets

Provide your own specific set of characters using the `-c` or `--chars` option. This option overrides all default character type settings (`--no-upper`, `--only-digits`, etc.).

```bash
pwdgen -l 15 -c "abcdeFGHIJ12345!@#$"
```

### Strength Analysis

By default, `pwdgen` provides a basic strength analysis for the generated password. The output will include a strength rating (e.g., "Weak", "Moderate", "Strong", "Very Strong").

```bash
pwdgen -l 18
```

### Help

To see all available options, their descriptions, and usage examples:

```bash
pwdgen --help
```

## Development

If you wish to contribute to this project or develop new features:

1.  Follow the [Installation](#installation) steps to set up your development environment.
2.  Make your desired code changes within the `src/pwdgen/` directory.
3.  Ensure all existing tests pass and add new tests for any new features or bug fixes in the `tests/` directory.
4.  Consider running linters and formatters (e.g., `flake8`, `black`) to maintain code quality and consistency.

## Testing

To run the test suite and ensure everything is working as expected:

1.  Make sure you have installed the project in editable mode (as per [Installation](#installation)).
2.  Navigate to the project's root directory.
3.  Execute `pytest`:
    ```bash
    pytest
    ```

## License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for full details.