.PHONY: gen-proto
gen-proto:
	@echo "Generating proto files..."

	cd ./proto && buf generate

	@echo "Done"

.PHONY: server
server:
	python cli.py server

.PHONY: client
client:
	python cli.py client

.PHONY: compose-db
compose-db:
	@echo "Starting database..."

	docker compose up -d

	@echo "Done"

.PHONY: compose-up
compose-up:
	@echo "Starting services..."

	docker compose --profile server up -d

	@echo "Done"

.PHONY: compose-down
compose-down:
	@echo "Stopping services..."

	docker compose --profile server down -v

	@echo "Done"
