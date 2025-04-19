# 🛣️ Roadmap simbiótico – NubemGenesisDeploy v1.2.0

Este roadmap traza las líneas evolutivas y funcionales de la versión `v1.2.0-dev` como parte del ecosistema NubemGenesisDeploy.

---

## 🧭 Objetivo general

Pasar de un sistema simbiótico funcional a uno **autoconfigurable, visual, expandible y conectado con IA**.

---

## 🧩 Módulos clave planificados

### 1. `dashboard.py`
- ✅ Mostrar versión, rama, último commit, validación de entorno y Firestore

### 2. `config.yaml`
- Centralizar toda la configuración del entorno
- Habilitar alternancia entre `dev`, `staging`, `prod`
- Ser leído por todos los scripts (`run`, `deploy`, `dashboard`, etc.)

### 3. `gpt_plugin_autoconnect.sh`
- Autoregistrar el plugin `openapi.yaml` en GPT personalizado
- Validar integridad del plugin antes de deploy
- Opcional: integración con `gh release` o API externa

### 4. `frontend_deploy.yml`
- CI/CD para desplegar frontend automáticamente al detectar cambios
- Usar token de Firebase desde GitHub Secrets
- Validar presencia de `firebase.json`

### 5. `makefile`
- Comandos simbólicos rápidos:
  - `make deploy`
  - `make docs`
  - `make check`
  - `make dashboard`

### 6. `meta/` (nuevo)
- Contendrá:
  - Glosario simbiótico
  - Trazabilidad de relaciones
  - Etiquetas de flujos (`DEPENDE DE`, `USA`, `TRIGGERS`)

---

## 🔐 Seguridad y control

- Integrar `pre-push` (además del `pre-commit`) para proteger ramas principales
- Validar que ningún secreto llegue a GitHub Actions
- Despliegue bloqueado si `test_memoria.sh` falla

---

## 🧬 Fase futura: `v2.0.0`

- Dashboards web live con Flask o HTML interactivo
- Núcleo IA con GPT personalizado embebido
- Autodescripción y documentación IA-generada (`self-describing scripts`)
- Conexión con el frontend simbiótico de NubemGenesis

---

## 🧠 Autoría

David Anguera – CEO NubemSystems  
Asistido por NubemGenesis – IA simbiótica generativa y evolutiva

---