import re

# === QA Rubric Rules ===
RUBRIC = {
    "Clarity": [
        r"(next step|please|you can|try the following)",
        r"(let me know|if it doesn’t work|feel free to)"
    ],
    "Structure": [
        r"(\d\.)",             # Numbered list
        r"(-|\*) ",            # Bulleted list
    ],
    "Tone": [
        r"(thank you|you're welcome|happy to help|no worries)",
        r"(hi\s+\w+|hello\s+\w+)",  # Greeting with name
    ],
    "Escalation Ready": [
        r"(error message|issue persist|provide more details|confirm the following)",
        r"(escalate|troubleshooting|tech team)"
    ],
    "Actionability": [
        r"(try|follow these steps|please restart|click the link)",
        r"(test page|check your spam|reboot)"
    ]
}

# === Check Function ===
def check_response(response_text):
    print("\n📋 QA Evaluation")
    passed = True
    for category, patterns in RUBRIC.items():
        matched = any(re.search(p, response_text, re.IGNORECASE) for p in patterns)
        checkbox = "✅" if matched else "❌"
        print(f"{checkbox} {category}")
        if not matched:
            passed = False
    return passed

# === Test GPT Response ===
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python qa_check.py 'your GPT response'")
    else:
        gpt_output = sys.argv[1]
        check_response(gpt_output)
