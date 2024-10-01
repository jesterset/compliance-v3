import os
import logging
import pathlib
from enum import Enum
from dotenv import load_dotenv
from typing import Dict, Literal, Set
from pydantic_settings import BaseSettings
from pydantic import BaseModel, Field, field_validator

VALID_ENV_FILES: Set[str] = {
        '.env_dev',
        '.env_uat', 
        '.env_qat', 
        '.env_prod'
}

class Environment(str, Enum):
    DEV: Literal['dev'] = 'dev'
    UAT: Literal['uat']  = 'uat'
    QAT: Literal['qat']  = 'qat'
    PROD: Literal['prod']  = 'prod'

ENV_FILE_MAP: Dict[Environment, str] = {
    Environment.DEV: '.env_dev',
    Environment.UAT: '.env_uat',
    Environment.QAT: '.env_qat',
    Environment.PROD: '.env_prod'
}

class ElasticConfig(BaseModel):
    host: str = Field(default_factory=lambda: os.getenv('ES_HOST'))
    # port: int = Field(default_factory=lambda: os.getenv('ES_PORT'))
    # username: str = Field(default_factory=lambda: os.getenv('ES_USERNAME'))
    # password: str = Field(default_factory=lambda: os.getenv('ES_PASSWORD'))

class PostgresConfig(BaseModel):
    host: str = Field(default_factory=lambda: os.getenv('PG_HOST'))
    # port: int = Field(default_factory=lambda: os.getenv('PG_PORT'))
    # username: str = Field(default_factory=lambda: os.getenv('PG_USERNAME'))
    # password: str = Field(default_factory=lambda: os.getenv('PG_PASSWORD'))
    # db_name: str = Field(default_factory=lambda: os.getenv('PG_DB_NAME'))

class Config(BaseSettings):
    _instance: 'Config' = None
    env: Environment | None = None
    elastic: ElasticConfig | None = None
    postgres: PostgresConfig | None = None

    @classmethod
    def load(cls: 'Config', environment: Environment) -> 'Config':
        cls._instance = cls.load(environment=Environment.DEV)
        return cls(
            env=environment,
            elastic=ElasticConfig(),
            postgres= PostgresConfig()
        )
    
    class EnvConfig:
        envirnment: Environment | None = Field(default=Environment.DEV)
        env_file: Literal['.env_dev', '.env_uat', '.env_qat', '.env_prod'] = ENV_FILE_MAP[Environment.DEV]
        env_file_encoding: str = 'utf-8'

        def __repr__(self) -> str:
            return f'<Config env={self.env}>'
        
        @property
        def env_file(self) -> str:
            return ENV_FILE_MAP[self.env]
        
        @field_validator('env_file', mode='before')
        def validate_env_file(cls: 'EnvConfig', value: str) -> str:
            if value not in VALID_ENV_FILES:
                raise ValueError(f'Invalid env file: {value}. Must be one of {VALID_ENV_FILES}')
            return value
        
        @classmethod
        def load(cls: 'EnvConfig', environment: Environment) -> 'EnvConfig':
            cls.envirnment: Environment = environment
            cls.env_file: str = ENV_FILE_MAP[environment.value]

            root_path: str = pathlib.Path(__file__).parent.parent.parent
            env_file_path: str = f'{root_path}/{cls.env_file}'

            if pathlib.Path(env_file_path).exists():
                load_dotenv(env_file_path, override=True)
                logging.info(f'Loaded environment variables from: {env_file_path}')
            else:
                logging.error(f'{env_file_path} not found. Loading from host environment variables...')


config: 'Config' = Config.load(Environment.DEV)

__all__ = ['config']