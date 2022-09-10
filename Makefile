## @ Docker Commands
.PHONY: build up down run restart
build: ## Create the image of dockerfile
	docker-compose build

up: ## Start the application
	docker-compose up -d

down: ## Remove the docker images and containers
	docker-compose down

run: ## Build and run the application
	docker-compose --env-file ./env.env -f docker-compose.yml up --build -d

run_dev: ## Build and run the application in dev mode
	docker-compose -f docker-compose.dev.yml up --build -d
	poetry run python ./application/main.py

run_local: ## Build and run the application in local mode !!you need run the application by yorself!!
	docker-compose --env-file ./env.env -f docker-compose.dev.yml up --build -d

restart: down run ## Rebuild all application

## @ Tests Commands
.PHONY: test
test: ## Run tests
	pytest -v

## @ Helper Commands
.PHONY: requirements help
requirements: ## Update requirements.txt
	poetry export --without-hashes -f requirements.txt > requirements.txt

help: ## Show this help.
	python help.py
