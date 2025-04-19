# 🔧 FUNCION: validar_memoria_activa
# 🧠 DESCRIPCION: Valida conexión y escritura en Firestore
# 📎 DEPENDE DE: google-cloud-firestore, credenciales.json

import os
from google.cloud import firestore
from datetime import datetime, timezone

# Establecer credenciales explícitamente
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/root/secrets/credenciales.json"

client = firestore.Client(project="nubemgenesis-deploy")

# Escritura simbólica
doc_ref = client.collection("memoria").document("nubem-test")
doc_ref.set({
    "estado": "activo",
    "autor": "David Anguera",
    "sello": "NubemGenesis",
    "timestamp": datetime.now(timezone.utc).isoformat()
})

# Lectura
docs = client.collection("memoria").stream()

print("🧠 Documentos encontrados en la colección 'memoria':")
for doc in docs:
    print(f"• {doc.id} => {doc.to_dict()}")