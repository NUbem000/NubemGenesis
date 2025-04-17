#!/bin/bash

### ╔════════════════════════════════════════════╗
### ║  NUBEMGENESIS DEPLOY SCRIPT - SIMBIÓTICO  ║
### ╚════════════════════════════════════════════╝

# 🌐 CARGAR VARIABLES DEL ENTORNO
echo "🔁 Cargando variables desde .env..."
if [ -f .env ]; then
  export $(cat .env | xargs)
else
  echo "❌ Archivo .env no encontrado. Abortando."
  exit 1
fi

# 📁 CREAR ESTRUCTURA DE CARPETAS BÁSICA (si no existe)
echo "📦 Validando estructura simbiótica..."
mkdir -p frontend backend plugins logs backend/crear_incidencia_gpt

# ✅ COMPROBAR AUTENTICACIONES
echo "🔐 Verificando sesiones activas..."
gcloud auth list
firebase login:list

# 🧠 CONFIGURAR PROYECTO Y ZONA EN GCP
echo "⚙️ Configurando proyecto y región por defecto..."
gcloud config set project $GCP_PROJECT_ID
gcloud config set compute/region $GCP_REGION

# ☁️ DESPLEGAR FUNCIONES CLOUD
echo "🚀 Desplegando función crear_incidencia_gpt..."
gcloud functions deploy crear_incidencia_gpt \
  --runtime python310 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point main \
  --source ./backend/crear_incidencia_gpt \
  --region $GCP_REGION || { echo "❌ Error en despliegue de función."; exit 1; }

# 🔥 DEPLOY FRONTEND (Firebase Hosting)
echo "🖼️ Desplegando frontend simbólico..."
cd frontend
npm install || echo "⚠️ npm install falló o no es necesario."
npm run build || echo "⚠️ build no requerido para HTML estático."
firebase deploy --only hosting
cd ..

# 📜 CREAR PLUGIN (OpenAPI)
echo "📡 Generando archivos del plugin GPT..."
mkdir -p plugins
cat > plugins/ai-plugin.json <<EOF
{
  "schema_version": "v1",
  "name_for_human": "NubemGenesisDeploy",
  "name_for_model": "nubemgenesis_deploy",
  "description_for_human": "Asistente simbiótico de despliegue IA.",
  "api": {
    "url": "https://api.nubemflow.com/openapi.yaml"
  }
}
EOF

cat > plugins/openapi.yaml <<EOF
openapi: 3.0.0
info:
  title: NubemGenesisDeploy API
  version: 1.0.0
paths:
  /deploy:
    get:
      summary: Despliega módulo simbiótico
      responses:
        '200':
          description: Éxito
EOF

# 📝 LOG Y RESUMEN FINAL
LOG_FILE="logs/deploy_$(date +%F_%H-%M-%S).log"
echo "✅ Registro del despliegue: $LOG_FILE"
echo "🧠 NubemGenesisDeploy activado simbióticamente." > "$LOG_FILE"

# 🎉 FINAL
echo "🎉 Despliegue simbiótico completado con éxito."
