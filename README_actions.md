# 🔐 GitHub Actions – NubemGenesis CI/CD Simbiótico

Este documento detalla cómo configurar y utilizar los workflows de CI/CD simbiótico en el repositorio **NubemGenesis**. El sistema automatiza la validación, despliegue de funciones y protege contra secretos filtrados.

---

## 📁 Workflows disponibles

| Archivo | Funcionalidad |
|--------|----------------|
| `.github/workflows/deploy.yml` | Validación simbólica de estructura y Firestore |
| `.github/workflows/deploy_full.yml` | Validación + despliegue automático de Cloud Function |

---

## 🧾 Requisitos previos

1. Tener activado **GitHub Actions** (por defecto está habilitado).
2. Cargar los secretos necesarios en el repositorio.

---

## 🔐 GitHub Secrets requeridos

Ve a 👉 [Settings > Secrets > Actions](https://github.com/NUbem000/NubemGenesis/settings/secrets/actions)

Y añade lo siguiente:

| Nombre del Secret | Valor sugerido |
|-------------------|----------------|
| `GCP_PROJECT_ID`  | `nubemgenesis-deploy` |
| `GCP_REGION`      | `europe-west1` |
| `GCP_SERVICE_KEY` | Contenido completo del archivo `credenciales.json` (Service Account) |

> 🔁 Puedes abrir el archivo con `nano` o un editor y copiar todo el contenido para pegarlo como valor del secret.

---

## 🚀 ¿Qué hace cada workflow?

### ✅ `deploy.yml`

- Se ejecuta en cada `push` a `main`
- Verifica que estén los archivos simbióticos
- Ejecuta `scripts/validar_memoria_activa.py`

### 🚀 `deploy_full.yml`

- Hace lo mismo que el anterior +
- Despliega automáticamente la función `crear_incidencia_gpt` si Firestore está validado

---

## 💬 Notas simbólicas

- Los workflows están diseñados para crecer: puedes añadir despliegue de frontend, validación de `.env`, o integración con otros módulos.
- Este sistema representa un flujo evolutivo. Cada acción deja una huella simbólica del estado del sistema.

---

## 🧠 Futuro

- Integración con NubemGenesis UI para disparar workflows manualmente
- Añadir notificaciones vía Discord, Telegram o correo
- Validación automática del `README`, changelogs y releases

---