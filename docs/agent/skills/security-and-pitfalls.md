# Security & Pitfalls ( The Guardian )

## 🛡️ What is it?
This isn't a standalone agent you trigger, but a **continuously active set of rules** that all agents follow. It acts as the "Immune System" of TANTRA, preventing common Python vulnerabilities.

## ⚙️ What it protects against

### 1. The "Leaky Handle"
*   **Problem:** Opening files without closing them.
*   **Rule:** All file I/O must use `with open(...)` Context Managers.

### 2. Path Traversal
*   **Problem:** Malicious users inputting `../../etc/passwd`.
*   **Rule:** All file paths are validated against the workspace root using `pathlib` and `resolve()`.

### 3. Shell Injection
*   **Problem:** Running `subprocess.run("cmd " + user_input, shell=True)`.
*   **Rule:** `shell=True` is strictly forbidden. Commands are always passed as a list of arguments.

### 4. Mutable Defaults
*   **Problem:** `def func(items=[]): ...` (The list persists across calls).
*   **Rule:** Forbidden. Use `items=None` instead.

## 🔎 How to Audit
You can ask the **Quality Manager**:
*   `"Scan for security issues"`
*   `"Audit for python pitfalls"`

The system runs `scripts/scan_vulnerabilities.py` to catch these patterns.