import datetime

HISTORY_FILE = "VERSION_HISTORY.md"
VERSION_FILE = "VERSION"
RELEASE_FILE = "RELEASE.md"

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def read_version():
    try:
        with open(VERSION_FILE, "r") as f:
            return f.read().strip()
    except:
        return "vX.Y.Z"

def read_release_notes():
    try:
        with open(RELEASE_FILE, "r") as f:
            return f.read().strip()
    except:
        return "Sin notas de release disponibles."

def append_to_history():
    date = get_current_date()
    version = read_version()
    notes = read_release_notes()

    new_entry = f"""\n## 🔁 {version} – {date}\n\n**Estado:** Publicado  \n**Descripción:** Release generada automáticamente desde `RELEASE.md`.\n\n{notes}\n\n---\n"""

    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(new_entry)

    print(f"✅ Historial actualizado con la versión {version}.")

if __name__ == "__main__":
    append_to_history()