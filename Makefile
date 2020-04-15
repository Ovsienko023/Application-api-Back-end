build :
	python3 Application-api/tests/scheme_data_base.py

test :
	python3 Application-api/tests/test_class_bd.py

run :
	python3 Application-api/src/server/server_flask.py
