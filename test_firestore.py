from google.cloud import firestore

# Crear el cliente usando la cuenta de servicio activa
client = firestore.Client(project="nubemgenesis-deploy")

# Leer algo (por ejemplo, todos los documentos de una colección de prueba)
docs = client.collection("prueba").stream()

print("🧠 Documentos encontrados:")
for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")
