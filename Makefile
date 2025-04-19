deploy:
	./run_nubemgenesis.sh

docs:
	python3 docs_autogen.py

status:
	python3 dashboard.py

firestore:
	python3 scripts/validar_memoria_activa.py

firebase:
	bash check_firebase_source.sh
