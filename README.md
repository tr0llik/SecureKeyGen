**SecureKeyGen** is a lightweight yet powerful password generator designed to create strong, user-friendly passwords. This tool adheres to modern security standards while maintaining readability and ease of use, inspired by Apple's password policies.

### Key Features:
- **Grouped Format**: Generates passwords divided into groups of 6 characters each, separated by hyphens (e.g., `nPovtd-upvf8k-avwkex`).
- **Strong Security**: 
  - Guarantees **exactly one uppercase letter** in one group.
  - Ensures **exactly one digit** in another group.
- **Unique Characters**: Each group contains only distinct characters for maximum entropy.
- **Readable Design**: Excludes ambiguous characters like `O`, `l`, and `I` to avoid confusion.
- **Customizable**: Allows users to define the number of groups and the length of each group.

### Usage:
1. Clone the repository and ensure Python is installed on your system.
2. Run the script directly from your terminal.
3. Customize the parameters (`group_length`, `num_groups`) or use the default settings to generate a password.

### Example Output:
```
Generated Secure Password: nPovtd-upvf8k-avwkex
```

### Why Choose SecureKeyGen?
SecureKeyGen is ideal for anyone who values both security and simplicity. Its intuitive design ensures that passwords are not only strong but also easy to remember and input.

Contribute to the project or adapt it for your own needs — SecureKeyGen is your reliable companion for managing online account security!

## License
This project is licensed under the GNU General Public License v3.0. You are free to use, modify, and distribute this software under the terms of the GPL license. Any derivative works must also be licensed under GPL.

For more information, see the [LICENSE](LICENSE) file included in this repository.
