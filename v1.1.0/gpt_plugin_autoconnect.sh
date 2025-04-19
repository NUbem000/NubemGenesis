#!/bin/bash
echo "🔗 Verificando y registrando el plugin OpenAPI en GPT..."

if [ ! -f plugins/ai-plugin.json ]; then
  echo "❌ Plugin no encontrado. Abortando."
  exit 1
fi

PLUGIN_URL="https://api.nubemflow.com/openapi.yaml"
echo "✅ Plugin definido en: $PLUGIN_URL"
# Aquí puedes integrar futuras llamadas a GPT Dev Tools o CLI personalizados

exit 0