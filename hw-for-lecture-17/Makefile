build:
	docker build --file Dockerfile --pull --tag study_managment .

run: build
	docker compose run --rm app python3 main.py

down:
	docker compose down

up: build
	docker compose up