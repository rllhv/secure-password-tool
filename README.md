# 🔐 Secure Password Evaluator & Generator

A Python command-line security utility that evaluates password strength and generates cryptographically secure random passwords.

---

## Features

- **Rule-based strength scoring:** evaluates length and character variety (uppercase, lowercase, digits, special symbols) and rates each password as Weak, Moderate, or Strong.
- **Actionable feedback:** tells the user exactly what is missing to strengthen a weak password.
- **Secure password generation:** built on Python's `secrets` module rather than `random`, whose output is predictable and unsuitable for security purposes.
- **Lightweight:** written entirely with the Python standard library.

---

## Sample Output

**Checking a password**

```
Result: Moderate 🟡 (Score: 3/6)
Suggestions to improve:
 - Missing uppercase letters.
 - Missing special symbols.
```

**Generating a password**

```
Enter desired length (default 16): 16

Generated Password: k7#Qm2$vXp9!Lw4R
```

---

## Scoring Model

| Check | Points |
|---|---|
| Length of 12 or more characters | +2 |
| Length of 8 to 11 characters | +1 |
| Contains an uppercase letter | +1 |
| Contains a lowercase letter | +1 |
| Contains a digit | +1 |
| Contains a special symbol | +1 |

| Score | Rating |
|---|---|
| 5 - 6 | Strong 🟢 |
| 3 - 4 | Moderate 🟡 |
| 0 - 2 | Weak 🔴 |

---

## Security Concepts Applied

- Cryptographically secure randomness (`secrets` vs. `random`)
- Password policy checks using regular expressions
- User-facing security feedback and remediation guidance

---

## Built With

Python 3 · `re` · `secrets` · `string`
