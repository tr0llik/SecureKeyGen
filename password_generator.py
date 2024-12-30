import random


def generate_secure_password(group_length=6, num_groups=3):
    """
    Generate a secure, easy-to-read, and memorable password with grouped formatting:
    - Groups of lowercase characters (e.g., reXoq-gikjib-vorda1)
    - Exactly one uppercase letter in one of the groups
    - Exactly one digit in one of the groups
    - Each group must have unique and readable characters
    """
    # Define character sets without ambiguous characters
    lowercase = "abcdefghijkmnopqrstuvwxyz"
    uppercase = "ABCDEFGHJKLMNPQRSTUVWXYZ"
    digits = "123456789"

    # Generate password groups
    groups = []
    for _ in range(num_groups):
        group = ''.join(random.sample(lowercase, group_length))  # Ensure unique characters per group
        groups.append(group)

    # Ensure exactly one uppercase letter in one random group
    random_upper_group_index = random.randint(0, num_groups - 1)
    group_with_upper = list(groups[random_upper_group_index])
    group_with_upper[random.randint(0, group_length - 1)] = random.choice(uppercase)
    groups[random_upper_group_index] = ''.join(group_with_upper)

    # Ensure exactly one digit in one random group
    random_digit_group_index = random.randint(0, num_groups - 1)
    while random_digit_group_index == random_upper_group_index:
        random_digit_group_index = random.randint(0, num_groups - 1)
    group_with_digit = list(groups[random_digit_group_index])
    group_with_digit[random.randint(0, group_length - 1)] = random.choice(digits)
    groups[random_digit_group_index] = ''.join(group_with_digit)

    # Join groups with hyphens
    password = '-'.join(groups)

    return password


if __name__ == "__main__":
    # Example usage
    group_length = 6  # Length of each group
    num_groups = 3  # Number of groups
    secure_password = generate_secure_password(group_length, num_groups)
    print("Generated Secure Password:", secure_password)
