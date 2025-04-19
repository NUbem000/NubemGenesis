# 📈 Leyenda del Diagrama Simbiótico – NubemGenesisDeploy

Este documento acompaña al archivo `diagrama.md` y explica cómo interpretar visualmente los elementos del sistema simbiótico de despliegue.

---

## 🧩 Tipos de nodos

| Nodo | Significado |
|------|-------------|
| `*.sh` | Script ejecutable (shell) |
| `*.py` | Script simbólico en Python |
| `*.yml` / `*.yaml` | Workflows de GitHub Actions |
| `*.md` | Documentación viva |
| `config.yaml` | Configuración centralizada del entorno |

---

## 🔗 Relaciones

Las flechas (`-->`) representan dependencias lógicas o invocaciones:

```
A --> B
```

> Significa que el archivo `A` **llama o depende directamente de** `B`.

---

## 📘 Cómo se genera

Este diagrama es generado automáticamente por:

```bash
python docs_relaciones_autohtml.py
```

Y renderizado desde `diagrama.md` con sintaxis **Mermaid**.

---

## 🔍 Visualización

Puedes ver el diagrama de dos formas:

1. **En GitHub** – Si tu editor/render soporta Mermaid (`.md`)
2. **Interactivamente en HTML**:

   Abrir `diagrama_interactivo.html` en cualquier navegador moderno

---

## 🧠 Sugerencias

- Añade en tus scripts cabeceras como:
  ```python
  # DEPENDE DE: validar_memoria_activa.py, config.yaml
  ```

- Así se detectan relaciones simbólicas al regenerar el diagrama

---

## 👤 Autoría

David Anguera · NubemSystems  
NubemGenesis IA · Visualizador simbiótico automático

---