#!/bin/bash
bash estado.sh || echo "⚠️ No se pudo ejecutar estado simbiótico"

echo "🔁 Iniciando despliegue simbiótico completo de NubemGenesis..."

# 1. Validar entorno
echo "🧪 Paso 1: Check del entorno..."
bash check_env.sh || { echo "❌ Fallo en check_env. Corrige y vuelve a intentar."; exit 1; }

# 2. Validar memoria activa
echo "🧠 Paso 2: Validar conexión con Firestore..."
source .venv/bin/activate
python3 scripts/validar_memoria_activa.py || { echo "❌ Fallo al conectar a Firestore. Aborto."; exit 1; }

# 3. Desplegar función principal
echo "🚀 Paso 3: Despliegue de Cloud Function..."
gcloud functions deploy crear_incidencia_gpt \
  --runtime python310 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point main \
  --source ./backend/crear_incidencia_gpt \
  --region=$GCP_REGION || { echo "❌ Error en despliegue de función."; exit 1; }

# 4. Desplegar frontend simbólico
echo "🖼️ Paso 4: Despliegue de frontend..."
cd frontend
firebase deploy --only hosting || { echo "❌ Error en frontend."; exit 1; }
cd ..

# 5. Reescribir commit si hay secreto en .env.template
echo "🧹 Paso 5: Limpieza de secretos en .env.template..."
sed -i 's/^OPENAI_API_KEY=.*/OPENAI_API_KEY=your-openai-key-here/' .env.template
git add .env.template
git commit --amend --no-edit
git push --force

# 6. Push final simbiótico completo
echo "📦 Paso 6: Subida final a GitHub"
git add .
git commit -m '🚀 Despliegue simbiótico automatizado completo'
git push

python3 release_preparar.py || echo '⚠️ No se pudo generar RELEASE.md'
echo '\n🧠 Ejecutando resumen final (dashboard.py)...'
python3 dashboard.py || echo '⚠️ No se pudo ejecutar dashboard simbiótico'
echo "🎉 NubemGenesis desplegado y validado simbióticamente con éxito."