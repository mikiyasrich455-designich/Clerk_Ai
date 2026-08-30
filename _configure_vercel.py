import io

path = r"C:\Users\mikiyas\Documents\TimeDetective\clerk\backend.py"
lines = io.open(path, encoding="utf-8").read().splitlines()
replacements = {
    "GROQ_KEY =": 'GROQ_KEY = os.environ.get("GROQ_API_KEY", "").strip()',
    "SERP_KEY =": 'SERP_KEY = os.environ.get("SERP_API_KEY", "").strip()',
}
changed = []
for index, line in enumerate(lines):
    for prefix, replacement in replacements.items():
        if line.startswith(prefix):
            lines[index] = replacement
            changed.append(prefix[:-3])

if sorted(changed) != ["GROQ_KEY", "SERP_KEY"]:
    raise RuntimeError("Expected both API-key configuration lines")

io.open(path, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print("Replaced embedded API-key fallbacks with environment-variable reads.")
