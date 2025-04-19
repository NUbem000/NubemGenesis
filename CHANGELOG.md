# 📜 CHANGELOG – NubemGenesisDeploy

---

## [v1.0.0] - 2025-04-18

### 🔰 Primera release oficial del entorno simbiótico

#### 🧱 Infraestructura
- Configuración de VM Ubuntu Clouding (2vCPU, 8GB RAM)
- Instalación de herramientas base: gcloud, firebase, node, pip, docker, git

#### 🔐 Autenticaciones y servicios
- Activación de cuenta personal y cuenta de servicio (GCP)
- Configuración de Firestore como memoria activa (modo nativo)
- Validación de conectividad y permisos desde entorno virtual Python

#### 🧠 Scripts creados
- `check_env.sh`: Verificación de entorno simbiótico
- `validar_memoria_activa.py`: Test de lectura/escritura en Firestore
- `deploy_nubemgenesis.sh`: Despliegue manual con validación previa
- `git_clean_and_force_push.sh`: Limpieza automática de secretos en `.env.template`
- `run_nubemgenesis.sh`: Orquestador simbiótico que ejecuta todo desde una línea

#### 🔄 CI/CD GitHub Actions
- `deploy.yml`: Validación de entorno y Firestore
- `deploy_full.yml`: Validación + despliegue automático de Cloud Function
- Documentación completa en `README_actions.md`

#### 🔐 Seguridad
- Activación de Push Protection en GitHub
- Hook `pre-commit` con detección de secretos (`sk-...`)
- Logging automático en `.git/hooks/commit.log`

#### 📦 Packaging
- Consolidación de todos los componentes en `NubemGenesisDeploy_v1.0.zip`
- Estructura preparada para evolución: scripts, workflows, hooks, documentación

---## [v1.2.0-dev] - [en desarrollo]

### Añadido
- 📁 Versión simbiótica inicial v1.2.0-dev
- 🧭 Activación del roadmap para dashboards y plugins GPT

---