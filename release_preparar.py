import datetime

VERSION_FILE = "VERSION"
CHANGELOG_FILE = "CHANGELOG.md"
OUTPUT_FILE = "RELEASE.md"

def get_version():
    try:
        with open(VERSION_FILE, "r") as f:
            return f.read().strip()
    except:
        return "vX.Y.Z"

def get_changelog_summary(lines=20):
    try:
        with open(CHANGELOG_FILE, "r") as f:
            changelog = f.readlines()
        # Buscar la última sección que comienza con ## [vX.X.X]
        indices = [i for i, line in enumerate(changelog) if line.startswith("## [v")]
        if indices:
            last_index = indices[-1]
            return "".join(changelog[last_index:last_index+lines])
        return "".join(changelog[-lines:])
    except:
        return "No se pudo cargar el changelog."

def generate_release(version):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    changelog = get_changelog_summary()

    header = f"# 🚀 NubemGenesisDeploy – Release {version}\n"
    date = f"**Fecha de publicación:** {today}\n"
    desc = f"**Versión simbiótica generada automáticamente desde los metadatos del proyecto.**\n\n---\n"
    body = f"## 📦 Componentes destacados\n\n{changelog}\n"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join([header, date, desc, body]))

    print(f"✅ RELEASE.md generado simbólicamente para {version}")

if __name__ == "__main__":
    version = get_version()
    generate_release(version)