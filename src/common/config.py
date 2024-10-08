import os
import logging
import pathlib
from enum import Enum
from typing import Dict, Literal, Set, Type
from pydantic_settings import BaseSettings
from pydantic import BaseModel, Field
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

VALID_ENV_FILES: Set[str] = {
    '.env_dev', 
    '.env_uat', 
    '.env_qat', 
    '.env_prod'
}

class Environment(str, Enum):
    DEV: Literal['dev'] = 'dev'
    UAT: Literal['uat'] = 'uat'
    QAT: Literal['qat'] = 'qat'
    PROD: Literal['prod'] = 'prod'

ENV_FILE_MAP: Dict[Environment, str] = {
    Environment.DEV: '.env_dev',
    Environment.UAT: '.env_uat',
    Environment.QAT: '.env_qat',
    Environment.PROD: '.env_prod'
}

class ElasticConfig(BaseModel):
    host: str = Field(default_factory=lambda: os.getenv('ES_HOST'))
    username: str = Field(default_factory=lambda: os.getenv('ES_USERNAME'))
    password: str = Field(default_factory=lambda: os.getenv('ES_PASSWORD'))

    def __repr__(self):
        return f"ElasticConfig(host={self.host}, username={self.username})"

class PostgresConfig(BaseModel):
    host: str = Field(default_factory=lambda: os.getenv('PG_HOST'))

    def __repr__(self):
        return f"PostgresConfig(host={self.host})"

class Config(BaseSettings):
    _instance: Type['Config'] | None = None

    env: Environment | None = None
    elastic: ElasticConfig | None = None
    postgres: PostgresConfig | None = None
    env_file: str | None = None

    def __repr__(self):
        return (f"Config(env={self.env}, "
                f"elastic={self.elastic}, "
                f"postgres={self.postgres})")

    @classmethod
    def get_instance(cls) -> Type['Config']:
        if cls._instance is None:
            raise RuntimeError("Config has not been loaded. Call 'get_config' first.")
        return cls._instance

    @classmethod
    def load(cls, environment: Environment = Environment.DEV) -> Type['Config']:
        logging.info("Loading config for environment: %s", environment)
    
        env_file_path = cls._determine_env_file(environment)
        print(f"env_file_path: {env_file_path}")
        cls._load_env_file(self=cls,env_file=env_file_path)

        cls._instance = cls(
            env=environment if environment else Environment.DEV,
            elastic=ElasticConfig(),
            postgres=PostgresConfig(),
            env_file=cls._determine_env_file(environment)
        )
        
        return cls._instance

    @staticmethod
    def _determine_env_file(environment: Environment) -> str:
        return ENV_FILE_MAP.get(environment, '.env_dev')

    def _load_env_file(self, env_file: str):
        root_path = pathlib.Path(__file__).parent.parent.parent
        env_file_path = root_path / env_file
        logging.info(f"Attempting to load environment variables from: {env_file_path}")

        if env_file_path.exists():
            logging.info(f"Loading environment variables from: {env_file_path}")
            load_dotenv(dotenv_path=env_file_path, verbose=True, override=True)

            es_host = os.getenv('ES_HOST')
            es_username = os.getenv('ES_USERNAME')
            pg_host = os.getenv('PG_HOST')
            logging.info(f"Loaded ES_HOST: {es_host}, ES_USERNAME: {es_username}, PG_HOST: {pg_host}")

        else:
            logging.warning(f"{env_file_path} not found. Loading from host environment variables...")


config = None

def get_config():
    global config
    if config is None:
        config = Config.load()
    return config

config_instance = get_config()

print(config_instance)  # For debugging
print(config_instance.elastic.username)
print(config_instance.elastic.password)

__all__ = ['get_config']
