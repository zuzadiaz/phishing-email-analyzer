# Phishing Email Analyzer

with open("suspicious_email.txt", "r") as file: 
	email_text = file.read()

suspicious_words = [
    "urgent",
    "immediately",
    "verify your password",
    "account suspension",
    "account has been locked",
    "click here"
]

suspicious_score = 0
findings = []

for word in suspicious_words:
    if word in email_text.lower():
        suspicious_score += 1
        findings.append(word)

print("Phishing Email Analysis Report")
print("------------------------------")
print(f"Suspicious score: {suspicious_score}")

print("\nRed flags found:")

for finding in findings:
    print(f"- {finding}")

if suspicious_score >= 3:
    print("\nRisk Level: HIGH")
elif suspicious_score >= 1:
    print("\nRisk Level: MEDIUM")
else:
    print("\nRisk Level: LOW")
