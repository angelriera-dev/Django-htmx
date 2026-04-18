

init:
	python3 -m venv .venv
	pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt

dev:
	.venv/bin/python manage.py runserver

migrate:
	.venv/bin/python manage.py migrate




APP_NAME := app

dev_container:
	@bash -lc '\
	if docker ps --filter "name=app-app" --format "{{.Names}}" | grep -q "app-app"; then \
		echo "Development container already running."; \
	else \
		echo "Starting development containers..."; \
		docker compose -f docker-compose.yml --project-name $(APP_NAME) up -d --build; \
		sleep 2; \
	fi; \
	exec docker compose -f docker-compose.yml --project-name $(APP_NAME) exec $(APP_NAME) bash'


clear_container:
	@docker compose down &&


rm rm-all:
	@ids="$(shell docker ps -aq)"; \
	if [ -n "$$ids" ]; then docker stop $$ids && docker rm $$ids; else echo "no containers"; fi


temp:
	@docker run -it --rm -v .:/app -w /app  python:slim /bin/bash -c "adduser --disabled-password --gecos '' --uid 1000 devuser && su devuser"
