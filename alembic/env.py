from logging.config import fileConfig
import asyncio

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy import pool  # Aquí se importa el pool
from alembic import context

from app.models.database import Base  # Asegúrate de que estás importando correctamente tu Base

# Configuración de Alembic
config = context.config

# Configuración del logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# MetaData de tus modelos
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Ejecutar las migraciones en modo 'offline'.

    Configura el contexto solo con la URL y sin un Engine.
    Esto no necesita un DBAPI disponible.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations_online() -> None:
    """Ejecutar migraciones en modo 'online' con conexión asíncrona."""

    # Crear el motor asíncrono
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool  # Aquí se usa el pool
    )

    # Conexión con el contexto de migración
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


def do_run_migrations(connection):
    """Ejecutar las migraciones con el contexto."""
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Invoca el contexto asíncrono para ejecutar las migraciones en modo 'online'."""
    asyncio.run(run_async_migrations_online())


# Determina si ejecutar en modo 'offline' o 'online'
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
