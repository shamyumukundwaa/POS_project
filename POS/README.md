# Coffee Shop POS API

This project is a FastAPI-based point-of-sale backend for managing users, products, categories, customers, suppliers, sales, payments, and receipts.

## Features

- REST endpoints for core POS resources
- SQLAlchemy models and repositories
- Basic validation and error handling
- with PostgreSQL support via DATABASE_URL

## Project structure

- app/models: SQLAlchemy models
- app/repositories: database access logic
- app/routers: API endpoints
- app/schemas: request/response schemas
- app/services: business logic for selected flows
