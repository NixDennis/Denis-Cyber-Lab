# Password Checker

A small Python script that rates a password from 0 to 5. It starts at 5, loses a point for every rule the password breaks and prints what is missing.

## Rules

- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character (anything that isn't a letter or a digit)

## Verdict

| Score | Verdict |
| ----- | ------- |
| 0-2 | Weak |
| 3-4 | Medium |
| 5 | Strong |

## Usage

```bash
python password_checker.py
```

## What I learned

- String methods: `isdigit()`, `isupper()`, `islower()`, `isalnum()`
- Methods must be called with parentheses: `isdigit` without `()` is always truthy
- Counters belong before the loop, not inside it
- `if` / `elif` / `else` for mutually exclusive cases

## Ideas for next version

- Move the logic into a `check_password(password)` function that returns the score
- Hide the input with `getpass`
- Check the password against a list of common leaked passwords
