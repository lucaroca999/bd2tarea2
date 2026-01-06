"""Database configuration with SQLAlchemy."""

from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin, SQLAlchemySyncConfig
from app.config import settings

# Configuracion sync para coincidir conRepositorios
sqlalchemy_config = SQLAlchemySyncConfig(
    connection_string=settings.database_url,
    create_all=True, 
)

sqlalchemy_plugin = SQLAlchemyPlugin(config=sqlalchemy_config)