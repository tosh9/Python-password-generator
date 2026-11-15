# Secure Password Generator

A Python-based Secure Password Generator that creates strong, random passwords using Python's built-in `secrets` module.

Generate customized passwords with lowercase letters, uppercase letters, numbers, and special characters.

## Features

- Generate secure random passwords.
- Customize password length.
- Choose lowercase letters.
- Choose uppercase letters.
- Choose mixed-case letters.
- Include numbers and special characters.
- Uses cryptographically secure random generation.
- Follows a 50-30-20 character distribution.

## Technologies Used

- Python 3
- Secrets Module
- String Module
- Math Module

## Requirements

- Python 3.x
- No external libraries required.

## Example Output

    SECURE PASSWORD GENERATOR

    Enter password length: 16

    1. Lowercase
    2. Uppercase
    3. Mixed case

    Choose character type (1/2/3): 3

    Generated Password: aG7@kP2#xM5&bR9$

Note: Generated password will be different each time.

## Password Distribution

The generator follows a 50-30-20 distribution:

| Character Type | Percentage |
|----------------|------------|
| Alphabets      | 50%        |
| Numbers        | 30%        |
| Special Characters | 20%    |

## Project Structure

    Secure-Password-Generator

     -password_generator.py
     -README.md
