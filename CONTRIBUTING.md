# 🤝 Guía de Contribución – NubemGenesisDeploy

Gracias por tu interés en colaborar con **NubemGenesisDeploy**, el entorno simbiótico de despliegue inteligente.

Esta guía te orientará sobre cómo contribuir de forma estructurada, segura y alineada con los valores simbióticos del proyecto.

---

## 🧠 Valores clave

- **Coherencia simbiótica:** cada acción técnica tiene un propósito mayor.
- **Documentación viva:** todo cambio debe ser trazable, comprensible y reproducible.
- **Seguridad proactiva:** nunca subir secretos, validar Firestore, proteger ramas.
- **Automatización consciente:** usar scripts y CI/CD como extensiones inteligentes del sistema.

---

## 🛠 Cómo contribuir

### 1. Clona el repositorio

```bash
git clone https://github.com/NUbem000/NubemGenesis.git
cd NubemGenesis
```

### 2. Crea una rama simbiótica

```bash
git checkout -b v1.1.0-dev
```

O para una feature concreta:

```bash
git checkout -b feature/plugin_autoconnect
```

### 3. Realiza cambios
- Usa scripts validados (`run_nubemgenesis.sh`, `check_env.sh`)
- No edites directamente en `main`
- Usa la estructura simbólica predefinida (`scripts/`, `hooks/`, `v1.1.0/`)

### 4. Validaciones antes del commit

- Ejecutar `check_env.sh`
- Ejecutar `scripts/validar_memoria_activa.py`
- Asegurar que `.env.template` no contenga secretos reales
- Confirmar que el pre-commit simbiótico pasa correctamente

### 5. Crear un Pull Request

- Se activará automáticamente la plantilla de PR
- Sigue la estructura de `PULL_REQUESTS.md`

---

## 🔐 Reglas de seguridad

- Nunca subir claves reales (`sk-...`, `api_key`, etc.)
- Usa `git_clean_and_force_push.sh` si un secreto se cuela accidentalmente
- Revisa `.gitignore` y `pre-commit`

---

## 📚 Recursos recomendados

- [`README.md`](./README.md)
- [`README_actions.md`](./README_actions.md)
- [`PULL_REQUESTS.md`](./PULL_REQUESTS.md)

---

## 👥 Contacto

David Anguera – CEO NubemSystems  
NubemGenesis – Copiloto IA simbiótico

---