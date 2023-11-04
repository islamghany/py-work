DB_DSN ?= 'postgres://postgres:islamghany@localhost:5432/py_test?sslmode=disable'

## help: print this help message
.PHONY: help
help:
	@echo 'Usage:'
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'

.PHONY: confirm
confirm:
	@echo -n 'Are you sure? [y/N] ' && read ans && [ $${ans:-N} = y ]


### Database migrations:

## db/migrate/create name=$1: create a new database migration
.PHONY: db/migrate/create
db/migrate/create:
	@echo 'Creating migration files for ${name}...'
	migrate create -ext sql -dir infra/db/migrations --seq ${name}

## db/migrate/up: run database migrations
.PHONY: db/migrate/up
db/migrate/up:
	@echo 'Running database migrations...'
	migrate -path infra/db/migrations -database ${DB_DSN} up

## db/migrate/down: rollback database migrations
.PHONY: db/migrate/down
db/migrate/down: confirm
	@echo 'Rolling back database migrations...'
	migrate -path infra/db/migrations -database ${DB_DSN} down

## db/migrate/force version=$1: force database migrations to a specific version
.PHONY: db/migrate/force
db/migrate/force: confirm
	@echo 'Forcing database migrations...'
	migrate -path infra/db/migrations -database ${DB_DSN} force ${version}

## db/migrate/version: print current database version
.PHONY: db/migrate/version
db/migrate/version:
	@echo 'Printing database version...'
	migrate -path infra/db/migrations -database ${DB_DSN} version

## db/migrate/seed: seed database
.PHONY: db/migrate/seed
db/migrate/seed:
	@echo 'Seeding database...'
	migrate -path infra/db/seeds -database ${DB_DSN} up
