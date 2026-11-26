#!/bin/sh
# Determinism check: run main.py twice into separate directories and
# require byte-identical output that passes the competition gate
# (UTF-8, 1-180 characters, not only white space, exactly one line).
set -eu
cd "$(dirname "$0")"

A=$(mktemp -d)
B=$(mktemp -d)
trap 'rm -rf "$A" "$B"' EXIT

MAKEFUN_OUTPUT_DIR="$A" python3 main.py
MAKEFUN_OUTPUT_DIR="$B" python3 main.py

cmp -s "$A/entry.txt" "$B/entry.txt" || { echo "FAIL: runs differ"; exit 1; }

python3 - "$A/entry.txt" <<'PY'
import re, sys
path = sys.argv[1]
data = open(path, "rb").read()
text = data.decode("utf-8")  # must be valid UTF-8
assert 1 <= len(text) <= 180, f"chars={len(text)}"
assert text.strip(), "only white space"
assert text.strip() == text, "leading/trailing white space"
assert "\n" not in text, "contains newline"
mode = __import__("os").stat(path).st_mode & 0o777
assert mode == 0o644, f"mode={oct(mode)}"
print(f"OK: {len(text)} chars, {len(data)} bytes, one line, mode 0644")
PY

echo "PASS: two runs byte-identical, gate check passed"
