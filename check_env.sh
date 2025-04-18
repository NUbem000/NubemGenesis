#!/bin/bash

echo "🔎 Verificando entorno simbiótico NubemGenesisDeploy..."
echo "──────────────────────────────────────────────────────"

# 1. Carpetas requeridas
declare -a folders=(
  "/root/nubemgenesis"
  "/root/nubemgenesis/backend/crear_incidencia_gpt"
  "/root/nubemgenesis/frontend"
  "/root/nubemgenesis/plugins"
  "/root/secrets"
)

echo "📁 Verificando carpetas requeridas..."
for folder in "${folders[@]}"; do
  if [ -d "$folder" ]; then
    echo "✅ Existe: $folder"
  else
    echo "❌ Falta: $folder"
  fi
done

# 2. Archivos requeridos
declare -a files=(
  "/root/nubemgenesis/deploy_nubemgenesis.sh"
  "/root/nubemgenesis/.env"
  "/root/secrets/credenciales.json"
)

echo -e "\n📄 Verificando archivos requeridos..."
for file in "${files[@]}"; do
  if [ -f "$file" ]; then
    echo "✅ Existe: $file"
  else
    echo "❌ Falta: $file"
  fi
done

# 3. Variables esenciales en .env
echo -e "\n🔐 Validando variables clave en .env..."
REQUIRED_VARS=("GCP_PROJECT_ID" "GCP_REGION" "GOOGLE_APPLICATION_CREDENTIALS" "OPENAI_API_KEY" "JIRA_EMAIL" "JIRA_TOKEN" "JIRA_URL")
for var in "${REQUIRED_VARS[@]}"; do
  if grep -q "^$var=" /root/nubemgenesis/.env; then
    echo "✅ Definida: $var"
  else
    echo "❌ FALTA: $var"
  fi
done

# 4. Herramientas instaladas
echo -e "\n⚙️ Comprobando herramientas clave..."
declare -a commands=("gcloud" "firebase" "node" "npm" "python3" "docker")
for cmd in "${commands[@]}"; do
  if command -v $cmd &>/dev/null; then
    echo "✅ $cmd disponible: $(which $cmd)"
  else
    echo "❌ $cmd no encontrado"
  fi
done

# 5. Sesión activa en GCloud
echo -e "\n🔐 Verificando sesión GCloud activa..."
gcloud auth list 2>/dev/null | grep ACTIVE &>/dev/null
if [ $? -eq 0 ]; then
  echo "✅ Sesión activa en GCloud"
else
  echo "❌ No hay sesión activa en GCloud"
fi

echo "──────────────────────────────────────────────────────"
echo "✔️ Checklist simbiótico finalizado."
