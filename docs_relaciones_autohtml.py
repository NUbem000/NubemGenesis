import os
from pathlib import Path

MERMAID_FILE = "diagrama.md"
HTML_FILE = "diagrama_interactivo.html"

def extract_dependencies(file_path):
    dependencies = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if "# DEPENDE DE:" in line:
                    parts = line.strip().split(":", 1)
                    if len(parts) == 2:
                        deps = parts[1].strip().split(",")
                        dependencies.extend([d.strip() for d in deps])
    except Exception:
        pass
    return dependencies

def generate_mermaid_diagram():
    lines = ["graph TD"]
    all_nodes = set()

    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith((".py", ".sh", ".yml", ".yaml")):
                full_path = os.path.join(root, file)
                node = Path(full_path).as_posix().replace("./", "")
                all_nodes.add(node)
                dependencies = extract_dependencies(full_path)
                for dep in dependencies:
                    lines.append(f'  {dep.replace(".", "_")} --> {node.replace(".", "_")}')
                    all_nodes.add(dep)

    for node in sorted(all_nodes):
        short = node.replace(".", "_")
        lines.append(f'  {short}["{node}"]')

    return lines

def generate_html_diagram(mermaid_lines):
    html_lines = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "  <meta charset='UTF-8'>",
        "  <title>📈 Diagrama Simbiótico – NubemGenesis</title>",
        "  <script type='module'>",
        "    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';",
        "    mermaid.initialize({ startOnLoad: true });",
        "  </script>",
        "</head>",
        "<body>",
        "  <h2>📈 Diagrama simbiótico generado automáticamente</h2>",
        "  <pre class='mermaid'>"
    ]
    html_lines.extend(mermaid_lines)
    html_lines.extend(["  </pre>", "</body>", "</html>"])
    return html_lines

if __name__ == "__main__":
    diagram_lines = generate_mermaid_diagram()

    with open(MERMAID_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(["# 📈 Diagrama generado automáticamente", "```mermaid"] + diagram_lines + ["```"]))
    print(f"✅ Mermaid Markdown generado: {MERMAID_FILE}")

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(generate_html_diagram(diagram_lines)))
    print(f"✅ Diagrama interactivo HTML generado: {HTML_FILE}")