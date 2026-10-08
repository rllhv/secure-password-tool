import re
import secrets
import string

def check_password_strength(password: str) -> dict:
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short (aim for at least 12 characters).")

    # Character diversity checks
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Missing uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Missing lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Missing numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Missing special symbols.")

    # Rating determination
    if score >= 5:
        level = "Strong 🟢"
    elif score >= 3:
        level = "Moderate 🟡"
    else:
        level = "Weak 🔴"

    return {"level": level, "score": score, "feedback": feedback}

def generate_secure_password(length: int = 16) -> str:
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-="
    return "".join(secrets.choice(characters) for _ in range(length))

def main():
    print("=" * 45)
    print("🔐 Password Strength Checker & Generator")
    print("=" * 45)

    choice = input("1. Check Password\n2. Generate Secure Password\nSelect (1/2): ").strip()

    if choice == "1":
        pwd = input("Enter password to evaluate: ")
        result = check_password_strength(pwd)
        print(f"\nResult: {result['level']} (Score: {result['score']}/6)")
        if result["feedback"]:
            print("Suggestions to improve:")
            for item in result["feedback"]:
                print(f" - {item}")

    elif choice == "2":
        length = int(input("Enter desired length (default 16): ") or 16)
        generated = generate_secure_password(length)
        print(f"\nGenerated Password: {generated}")
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
