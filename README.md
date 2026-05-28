# Phishing Email Analyzer

A Python-based cybersecurity tool that scans email text files for common phishing indicators and assigns a risk level based on suspicious content.

## Features

- Detects suspicious phishing phrases
- Assigns a phishing risk score
- Identifies common social engineering language
- Reads email content from external `.txt` files
- Generates a simple phishing analysis report

## Technologies Used

- Python 3
- Linux / WSL
- Git & GitHub

## Example Detection Indicators

The tool searches for phrases such as:

- urgent
- immediately
- verify your password
- click here
- account suspended

## Example Output

```text
Phishing Email Analysis Report
------------------------------

Suspicious score: 2

Red flags found:
- urgent
- immediately

Risk Level: MEDIUM
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/zuzadiaz/phishing-email-analyzer.git
```

Move into the project folder:

```bash
cd phishing-email-analyzer
```

Run the analyzer:

```bash
python3 analyzer.py
```

## Future Improvements

- Regex URL detection
- Suspicious domain analysis
- Email header analysis
- Machine learning classification
- GUI interface

## Author

Zuzanna Diaz
Cybersecurity / Python / Linux / Git
