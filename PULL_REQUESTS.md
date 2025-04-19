# 🔀 Guía para Pull Requests – NubemGenesisDeploy

Esta guía define el flujo simbiótico para proponer cambios en NubemGenesisDeploy mediante Pull Requests (PR).  
Está diseñada para mantener coherencia, trazabilidad y seguridad en cada fusión.

---

## ✅ ¿Cuándo crear un PR?

- Al completar una función o módulo nuevo (por ejemplo: `estado.sh`)
- Al corregir o mejorar scripts existentes (`deploy_nubemgenesis.sh`)
- Al actualizar documentación clave (`README.md`, `CHANGELOG.md`)
- Al agregar validaciones o seguridad (`hooks/pre-commit`, GitHub Actions)

---

## 📦 Requisitos previos

Antes de crear el PR:

1. Validar el entorno con `check_env.sh`
2. Validar conexión a Firestore con `validar_memoria_activa.py`
3. Asegurarse de que no hay secretos en `.env` ni `.env.template`
4. Pasar todos los checks de GitHub Actions
5. Actualizar `CHANGELOG.md` y `VERSION` si corresponde

---

## 🧠 Estructura simbiótica del PR

Al abrir el PR se cargará automáticamente `pull_request_template.md` con secciones para:

- Contexto
- Cambios realizados
- Checklist de validaciones
- Enlaces a issues o ramas relacionadas

---

## 🔁 Proceso de revisión simbiótica

1. Revisión técnica (validación de estructura y lógica)
2. Revisión simbólica (coherencia con propósito y narrativa del proyecto)
3. Validación de CI/CD
4. Aprobación final

---

## 🧪 Recomendaciones

- Usa ramas como `v1.1.0-dev`, `feature/plugin_autoconnect`, `fix/firestore-permissions`
- Mantén commits claros y con mensajes simbólicos si aplica
- No fuerces `push` a `main` directamente (usa PR)

---

## 🧬 Fusión y cierre

Una vez aprobado el PR:
- Se fusiona en `main`
- Se crea tag si corresponde (`v1.1.0`)
- Se publica la release si es una nueva versión

---

## 👤 Contacto simbiótico

David Anguera – CEO NubemSystems  
Asistido por NubemGenesis – IA simbiótica operativa

---