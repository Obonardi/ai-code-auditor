"""
AI CODE AUDITOR
---------------
Purpose: Automate the evaluation of code snippets for 
adherence to specified quality dimensions.

Evaluation Dimensions:
- Correctness: Syntactic and functional validity.
- Clarity: Readability and documentation standards.
- Efficiency: Algorithmic complexity and resource usage.
- Reasoning: Validity of logic within the provided code.
"""

def audit_clarity(file_path):
    """
    Checks if a Python file contains docstrings (indicated by triple quotes).
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if '"""' in content or "'''" in content:
                return "PASS: Documentation found."
            else:
                return "FAIL: Missing docstrings."
    except Exception as e:
        return f"Error auditing file: {e}"

# Simple test for this auditor itself
print(f"Auditing current file: {audit_clarity('auditor.py')}")

def audit_correctness(file_path):
    """
    Checks if the file has content; an empty file is a functional error.
    """
    import os
    if os.path.getsize(file_path) > 0:
        return "PASS: File contains logic."
    else:
        return "FAIL: File is empty."

# Update your print statements to show both
print(f"Auditing Clarity: {audit_clarity('auditor.py')}")
print(f"Auditing Correctness: {audit_correctness('auditor.py')}")