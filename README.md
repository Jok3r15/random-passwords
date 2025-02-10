
# Secure Password Generator

This project is a tool for generating secure random passwords. The user can specify the password length via a command-line argument or, if the argument is not provided, the program will prompt the user to input the length interactively.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/secure-password-generator.git
   cd secure-password-generator
   ```

2. Install any necessary dependencies (if applicable).

## Usage

### Running with Length Argument

You can run the script directly from the command line and specify the password length using the `--length` argument:

```bash
python main.py --length 16
```

This command will generate a password of 16 characters using a mix of letters (uppercase and lowercase), numbers, and symbols.

### Running Without Length Argument

If you do not specify the `--length` argument, the program will prompt you to input the desired password length interactively:

```bash
python main.py
```

The program will ask you to input the desired length for the password:

```
Please enter the desired password length: 12
```

Once the value is entered, the program will generate the password with the specified length.

## Code Explanation

The script uses the `argparse` module to handle command-line arguments and the `random` module along with `string` to generate random passwords. The password is composed of:

- Uppercase and lowercase letters (`string.ascii_letters`)
- Numbers (`string.digits`)
- Special characters (`string.punctuation`)

### Function `generate_password(length)`

This function takes the desired password length and returns a random password using the allowed characters.

### Arguments

- `--length`: Specifies the length of the password (integer). If this argument is not provided, the program will prompt the user to enter the length.

## Example

Generate a password of 16 characters:

```bash
python main.py --length 16
```

Generate a password with the length specified by the user:

```bash
python main.py
```

## Contributions

If you would like to contribute to this project, please fork the repository and open a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
