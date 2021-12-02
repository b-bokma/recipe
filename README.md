# SQLAlchemy ORM 1.4 with FastAPI on asyncio

This is a tutorial app build for my [blog post](https://rogulski.it/blog/sqlalchemy-14-async-orm-with-fastapi/)
## Run project
`docker-compose up`

## Run tests
`docker-compose run app pytest`

# Database

The database is managed via sqlalchemy and alembic.
The Base Model is set up in tables/base_class and imported all underlying models.
Base.py imports all models to feed it to alembic

In config.settings you pass localhost (or 127.0.0.1) as db_host. 
In the .env file it is the name of the DB so docker will define the hostname.

## update /app/db/migrations/env.py
import Base models, import configs to load all metadata to alembic

## initialize Alembic
alembic init /app/db/migrations/

## initiate a migration
* run alembic stamp <migration script ID> to move the migration scripts to the latest version. 
If the DB is behind, run `alembic history` to find the ID of the last migration file.
  * `docker-compose run app alembic revision --autogenerate`
* When the file is created execute the migration
  * `docker-compose run app alembic upgrade head`
