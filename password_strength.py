import tkinter as tk
from tkinter import messagebox
import re


def assess_password_strength(password):
    # Criteria definitions
    criteria = {
        "length": len(password) >= 12,
        "uppercase": re.search(r'[A-Z]', password) is not None,
        "lowercase": re.search(r'[a-z]', password) is not None,
        "digits": re.search(r'[0-9]', password) is not None,
        "special": re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    }

    # Assessment logic
    score = sum(criteria.values())
    strength = "Weak"
    feedback = []

    if score == 5:
        strength = "Very Strong"
        feedback.append("Your password is very strong!")
    elif score == 4:
        strength = "Strong"
        feedback.append("Your password is strong.")
    elif score == 3:
        strength = "Moderate"
        feedback.append("Your password is moderate. Consider adding:")
        if not criteria["length"]:
            feedback.append("- More characters (12 or more).")
        if not criteria["uppercase"]:
            feedback.append("- Uppercase letters.")
        if not criteria["lowercase"]:
            feedback.append("- Lowercase letters.")
        if not criteria["digits"]:
            feedback.append("- Digits.")
        if not criteria["special"]:
            feedback.append("- Special characters (e.g., !@#$%^&*).")
    elif score == 2:
        strength = "Weak"
        feedback.append("Your password is weak. Consider adding:")
        if not criteria["length"]:
            feedback.append("- More characters (12 or more).")
        if not criteria["uppercase"]:
            feedback.append("- Uppercase letters.")
        if not criteria["lowercase"]:
            feedback.append("- Lowercase letters.")
        if not criteria["digits"]:
            feedback.append("- Digits.")
        if not criteria["special"]:
            feedback.append("- Special characters (e.g., !@#$%^&*).")
    else:
        strength = "Very Weak"
        feedback.append("Your password is very weak. Consider adding:")
        if not criteria["length"]:
            feedback.append("- More characters (12 or more).")
        if not criteria["uppercase"]:
            feedback.append("- Uppercase letters.")
        if not criteria["lowercase"]:
            feedback.append("- Lowercase letters.")
        if not criteria["digits"]:
            feedback.append("- Digits.")
        if not criteria["special"]:
            feedback.append("- Special characters (e.g., !@#$%^&*).")

    return strength, feedback


def on_assess():
    password = entry_password.get()
    strength, feedback = assess_password_strength(password)
    messagebox.showinfo("Password Strength", f"Strength: {strength}\n\n" + "\n".join(feedback))


# GUI Setup
root = tk.Tk()
root.title("Password Strength Assessor")

label_password = tk.Label(root, text="Enter Password:")
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*", width=50)
entry_password.pack(pady=10)

button_assess = tk.Button(root, text="Assess Strength", command=on_assess)
button_assess.pack(pady=10)

root.mainloop()
