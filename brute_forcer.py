def brute_force(password_list, target_password):
    print("Trying to guess the password...")
    for password in password_list:
        if password == target_password:
            print(f"Password found: {password} ✅")
            return
    print("Password not found ❌")

# Example
if __name__ == "__main__":
    passwords = ["1234", "admin", "password", "letmein"]
    brute_force(passwords, "letmein")
