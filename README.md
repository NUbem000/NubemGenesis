# 🧠 NubemGenesisDeploy – Entorno Simbiótico de Despliegue
[![📘 Documentación Simbiótica](https://github.com/NUbem000/NubemGenesis/actions/workflows/docs_autogen.yml/badge.svg)](https://github.com/NUbem000/NubemGenesis/actions/workflows/docs_autogen.yml)

**NubemGenesisDeploy** es una arquitectura diseñada para desplegar, validar y versionar simbólicamente todos los componentes críticos de un sistema inteligente. Opera como núcleo técnico de NubemGenesis y conecta funciones, frontend y memoria activa en Firestore con automatización total y control simbólico.

---


📚 [Ver índice completo de documentación simbiótica](./docs_menu.md)

## 🚀 ¿Qué hace este entorno?

- Despliega funciones (Google Cloud Functions)
- Despliega frontend (Firebase Hosting)
- Valida conectividad con Firestore como memoria activa
- Verifica el entorno antes de cada despliegue
- Limpia secretos antes de cada `push`
- Versiona todo el sistema con control y trazabilidad
- Ejecuta todo desde una única línea

---

## 📂 Estructura del proyecto

```
nubemgenesis/
├── backend/
│   └── crear_incidencia_gpt/       # Función simbólica mínima
├── frontend/                        # Web simbólica desplegable
├── scripts/
│   ├── validar_memoria_activa.py   # Validador de Firestore
│   └── check_env.sh                # Verificación de entorno
├── .env.template                   # Plantilla sin secretos
├── deploy_nubemgenesis.sh          # Despliegue manual
├── run_nubemgenesis.sh             # Orquestador simbiótico total
└── git_clean_and_force_push.sh     # Limpieza automática de secretos
```

---

## ⚙️ Requisitos del entorno

- Ubuntu 20.04+ (en Cloud o local)
- Python 3.10+
- GCloud SDK + Firebase CLI
- Node.js + npm
- Git configurado con acceso a GitHub
- Firestore activado en Google Cloud (modo Nativo)

---

## 🧪 Comandos principales

### Validar entorno y Firestore

```bash
bash check_env.sh
```

### Desplegar todo automáticamente

```bash
./run_nubemgenesis.sh
```

### Validar Firestore directamente

```bash
source .venv/bin/activate
python scripts/validar_memoria_activa.py
```

### Limpiar secretos y forzar push (en caso de error)

```bash
./git_clean_and_force_push.sh
```

---

## 🔐 Seguridad simbólica

- Push Protection activo en GitHub
- `.env.template` no contiene valores reales
- Preconfigurado para integración con GitHub Actions y control remoto

---

## 🧭 Filosofía

Cada despliegue es una extensión de la intención simbiótica del sistema. Este entorno no solo automatiza, sino que respeta la evolución, protege el conocimiento y deja huella trazable en cada acción técnica.

---

## 👤 Autor

David Anguera (NubemSystems)  
Conectado simbióticamente con ChatGPT

---