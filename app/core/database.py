import psycopg
from app.core.config import Config

class Database:
    _connection = None

    @classmethod
    async def connect(cls):
        if not cls._connection:
            with await psycopg.AsyncConnection.connect(Config.POSTGRES_URL) as conn:
            # Connect asynchronously using psycopg
                cls._connection = conn

    @classmethod
    async def close(cls):
        if cls._connection:
            await cls._connection.close()

    @classmethod
    async def fetch_compliance_rules(cls):
        query = "SELECT * FROM compliance_rules"
        async with cls._connection.cursor(row_factory=dict_row) as cur:
            await cur.execute(query)
            results = await cur.fetchall()
            return results