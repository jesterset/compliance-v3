import psycopg
# from psycopg.rows import dict_row
from app.core.config import Config
from psycopg.rows import dict_row

class Database:
    _connection = None

    @classmethod
    async def connect(cls):
        if not cls._connection:
            cls._connection = await psycopg.AsyncConnection.connect(Config.POSTGRES_URL)

    @classmethod
    async def close(cls):
        if cls._connection:
            await cls._connection.close()

    @classmethod
    async def fetch_compliance_rules(cls):
        async with cls._connection.cursor(row_factory=dict_row) as cur:
            await cur.execute("SELECT * FROM compliance_rules")
            results = await cur.fetchall()
            return [row for row in results]