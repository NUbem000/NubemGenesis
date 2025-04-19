import os
from pathlib import Path

ROOT = Path(".")
OUTPUT = "DOCUMENTACION_COMPLETA_GENERADA.md"

def extract_headers_from_file(filepath):
    headers = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip().startswith("#"):
                    headers.append(line.strip())
                if len(headers) > 0 and not line.strip().startswith("#"):
                    break  # Stop at the first non-header block
    except Exception as e:
        headers.append(f"# ❌ Error leyendo {filepath.name}: {str(e)}")
    return headers

def generate_documentation(root_path):
    doc_lines = ["# 📚 Documentación simbiótica generada automáticamente", ""]
    for dirpath, dirnames, filenames in os.walk(root_path):
        rel_dir = Path(dirpath).relative_to(root_path)
        if rel_dir.parts and rel_dir.parts[0].startswith(".git"):
            continue  # Ignorar carpetas de git

        if rel_dir != Path("."):
            doc_lines.append(f"## 📁 Carpeta: `{rel_dir}`\n")

        for filename in filenames:
            filepath = Path(dirpath) / filename
            if filepath.suffix in [".sh", ".py", ".yml", ".yaml", ".md"]:
                doc_lines.append(f"### 📄 Archivo: `{filepath.relative_to(root_path)}`")
                headers = extract_headers_from_file(filepath)
                if headers:
                    doc_lines.extend(headers)
                else:
                    doc_lines.append("_Sin descripción simbólica encontrada._")
                doc_lines.append("")  # Separación
    return doc_lines

if __name__ == "__main__":
    content = generate_documentation(ROOT)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
    print(f"✅ Documentación generada en: {OUTPUT}")