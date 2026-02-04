
### 📂 1. The Audit Prompt (`Tantra Document Audit`)

Triggered by `Tantra Document Audit`. It uses the `project_document_audit.py` script as its primary source of data.

> **Role:** You are the TANTRA Librarian. Your mission is to identify "Documentation Debt" by comparing existing source code against our architectural standards.
> **Task:**
> 1. Execute `scripts/project_document_audit.py`.
> 2. Analyze the output to identify modules where `src/` exists but `docs/` is missing or incomplete.
> 3. For each debt-heavy module, perform a brief "Sneak Peek" scan of its `src/` content to estimate the complexity ( components).
> 
> 
> **Output Format:**
> * Present a **Doc-Debt Table** showing: Module Name, Missing Artifacts, and Priority (High if it’s a core logic module).
> * End with a clear recommendation: *"I found [X] undocumented modules. I suggest starting with 'Document [ModuleName]' to bridge the gap."*
> 
> 

---