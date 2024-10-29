# Stores REST API

This project is a REST API for managing stores, items, tags, and users. Built with Flask, it uses JWT-based authentication for secure user access, a SQL database for persistence, and auto-generated Swagger documentation for ease of use.

## Features
- User authentication with JWT (JSON Web Tokens)
- CRUD operations for stores, items, tags, and users
- Swagger UI for interactive API documentation
- SQLite support (default) with easy configuration for other databases
- JWT blocklist to handle revoked tokens
- Token-based error handling for expired, invalid, and unauthorized tokens
- **Dockerized** for easy setup and deployment

## Technologies Used
- **Flask**: Web framework for building REST APIs
- **Flask-Smorest**: API Blueprinting and documentation
- **Flask-Migrate**: Database migrations
- **Flask-JWT-Extended**: JWT authentication and security
- **Swagger**: API documentation
- **SQLAlchemy**: ORM for database interactions
- **SQLite**: Default database (can be configured)
- **Docker**: Containerization for easy deployment