#!/bin/bash

echo "📊 Estado simbiótico actual de NubemGenesisDeploy"
echo "──────────────────────────────────────────────────"

# Última versión registrada
if [ -f VERSION ]; then
  echo "🧬 Versión activa: $(cat VERSION)"
else
  echo "🧬 Versión activa: (no definida)"
fi

# Último commit
echo -e "\n🔁 Último commit:"
git log -1 --pretty=format:'%h - %s (%cr) [%an]'

# Rama actual
echo -e "\n🌿 Rama activa:"
git branch --show-current

# Validación rápida del entorno
echo -e "\n🔎 Validación de entorno (check_env.sh):"
if [ -f check_env.sh ]; then
  bash check_env.sh | tail -n 10
else
  echo "❌ check_env.sh no disponible"
fi

# Últimos cambios en changelog
if [ -f CHANGELOG.md ]; then
  echo -e "\n📜 Últimos cambios:"
  tail -n 10 CHANGELOG.md
fi

echo "──────────────────────────────────────────────────"