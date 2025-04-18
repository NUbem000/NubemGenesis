from google.cloud import firestore
from datetime import datetime

# Configuración simbólica
COLECCION = "memoria"
DOCUMENTO = "nubem-test"

# Conexión al cliente Firestore
client = firestore.Client(project="nubemgenesis-deploy")

# Escritura simbólica de prueba
doc_ref = client.collection(COLECCION).document(DOCUMENTO)
doc_ref.set({
    "estado": "activo",
    "autor": "David Anguera",
    "sello": "NubemGenesis",
    "timestamp": datetime.utcnow().isoformat()
})

print("✅ Documento de prueba escrito correctamente.\n")

# Lectura de todos los documentos en la colección
docs = client.collection(COLECCION).stream()

print(f"🧠 Documentos encontrados en la colección '{COLECCION}':")
for doc in docs:
    print(f"• {doc.id} => {doc.to_dict()}")
