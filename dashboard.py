import os
import subprocess
from pathlib import Path

def print_header(title):
    print(f"\n🧭 {title}")
    print("-" * 60)

def read_file(path, default="(no disponible)"):
    if Path(path).exists():
        return Path(path).read_text().strip()
    return default

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"(error: {e})"

def main():
    print("📊 NubemGenesisDeploy – Dashboard simbiótico CLI")
    print("=" * 60)

    # VERSION
    print_header("Versión activa")
    print(read_file("VERSION"))

    # RAMA
    print_header("Rama activa")
    print(run_command("git branch --show-current"))

    # COMMIT
    print_header("Último commit")
    print(run_command("git log -1 --pretty=format:'%h - %s (%cr) [%an]'"))

    # FIRESTORE TEST
    print_header("Validación simbólica de Firestore")
    if Path("test_memoria.sh").exists():
        os.chmod("test_memoria.sh", 0o755)
        result = subprocess.call("./test_memoria.sh")
        print("✅ Memoria activa OK" if result == 0 else "❌ Fallo en memoria simbólica")
    else:
        print("⚠️ test_memoria.sh no encontrado")

    # ENV CHECK
    print_header("check_env.sh (últimos 10 resultados)")
    if Path("check_env.sh").exists():
        output = run_command("bash check_env.sh | tail -n 10")
        print(output)
    else:
        print("⚠️ check_env.sh no encontrado")

    # CHANGELOG
    print_header("Últimos cambios (CHANGELOG.md)")
    print(run_command("tail -n 10 CHANGELOG.md"))

    print("\n✅ Dashboard simbiótico ejecutado con éxito.")
    print("=" * 60)

if __name__ == "__main__":
    main()