#!/bin/bash

echo "📊 Estado simbiótico de NubemGenesis"

echo "Último commit:"
git log -1 --pretty=format:'%h %s (%cr) <%an>'

echo -e "\nÚltima versión registrada:"
cat VERSION

echo -e "\nÚltimos cambios:"
tail -n 5 CHANGELOG.md

echo -e "\nValidación rápida de entorno:"
bash check_env.sh | tail -n 10