build:
	docker build --file Dockerfile --pull --tag airbnb .

run: build
	docker compose run --rm app python3 main.py

down:
	docker compose down