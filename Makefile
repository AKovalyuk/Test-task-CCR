env:
	cp .env.sample .env

requirements:
	pip freeze > requirements.txt
	echo "psycopg2==2.9.9" >> requirements.txt