#!/bin/bash

echo "🧪 Test simbiótico de memoria activa (Firestore)"
source .venv/bin/activate

python3 scripts/validar_memoria_activa.py
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
  echo "✅ Memoria activa validada simbólicamente"
  exit 0
else
  echo "❌ Fallo en validación de memoria activa"
  exit 1
fi