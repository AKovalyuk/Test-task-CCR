env:
	cp .env.sample .env

requirements:
	pip freeze > requirements.txt
	# Сложно поставить локально на manjaro linux, в Docker все нормально
	echo "psycopg2==2.9.9" >> requirements.txt