# 🚀 NubemGenesisDeploy – Release v1.0.0

**Fecha de publicación:** 2025-04-19

**Versión simbiótica generada automáticamente desde los metadatos del proyecto.**

---

## 📦 Componentes destacados

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


