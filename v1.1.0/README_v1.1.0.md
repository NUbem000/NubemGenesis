# 🚀 NubemGenesisDeploy – Roadmap simbiótico v1.1.0

**Fecha estimada:** 2025-04  
**Estado:** En desarrollo inicial

---

## 🧬 Objetivo

La versión `v1.1.0` de NubemGenesisDeploy amplía las capacidades del entorno con módulos de despliegue CI/CD extendido, documentación viva, conexión automática a plugins GPT y dashboard simbiótico de estado.

---

## 🧩 Módulos clave

### 1. `frontend_deploy.yml` – CI/CD para frontend
- Despliegue automático a Firebase Hosting al detectar cambios en `/frontend`
- Uso de `FIREBASE_DEPLOY_TOKEN` desde GitHub Secrets

### 2. `gpt_plugin_autoconnect.sh` – Autoregistro OpenAPI
- Verifica si existe `ai-plugin.json`
- Expone la URL del plugin (`/openapi.yaml`)
- Preparado para integrarse con flujos de GPT personalizados

### 3. `docs_autogen.md` – Documentación viva generada
- Extraída de la estructura de carpetas, scripts y configuraciones
- Listado de componentes y responsables simbióticos

### 4. `config.yaml` – Configuración simbiótica centralizada
- Unifica entorno, región, Firestore, frontend, modelo GPT, etc.
- Ideal para escalar a múltiples entornos (`produccion`, `staging`, `dev`)

### 5. `estado.sh` – Dashboard CLI simbiótico
- Muestra último commit, versión, extracto de changelog y estado general
- Ideal para diagnósticos rápidos antes de ejecutar despliegues

---

## 🛡️ Seguridad y evolución

- Se mantiene activo el pre-commit simbiótico (`hooks/pre-commit`)
- Cada nueva función incluirá validación previa y logging
- `run_nubemgenesis.sh` podrá integrar `config.yaml` para adaptar flujos dinámicamente

---

## 📦 Paquete de trabajo

`NubemGenesisDeploy_v1.1.0_scaffold.zip` contiene todos los módulos iniciales con estructura base lista para iteración y pruebas.

---

## 📘 Recomendación

Crear un branch simbiótico llamado `v1.1.0-dev` para implementar y testear estas nuevas funcionalidades antes de su integración en `main`.

---

## 👤 Responsable

David Anguera · CEO NubemSystems  
Asistido por NubemGenesis – sistema IA simbiótico evolutivo

---