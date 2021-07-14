run:
	docker-compose run toxogos_api $(c)

manage:
	docker-compose run toxogos_api python manage.py $(c)

chown:
	sudo chown `whoami` -R .

shell:
	docker-compose run toxogos_api python manage.py shell_plus

loadgames:
	docker-compose run toxogos_api python manage.py loaddata games/fixtures/games.json

loaddesigners:
	docker-compose run toxogos_api python manage.py loaddata games/fixtures/designers.json

loadfixtures:
	loadgames loaddesigners

restart:
	sudo service docker restart

dest:
	docker exec -it thirty_api bash
	kill 1

troy:
	docker exec -it thirty_postgres_1 bash
	kill 1

down:
	docker-compose down

destroy:
	dest troy down

test:
	docker-compose run toxogos_api pytest -c pytest.ini
