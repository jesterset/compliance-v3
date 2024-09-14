import psycopg
# from psycopg.rows import dict_row
from app.core.config import Config

class Database:
    _connection = None

    @classmethod
    async def connect(cls):
        print("connecting")
        if not cls._connection:
            cls._connection = await psycopg.AsyncConnection.connect(Config.POSTGRES_URL)

    @classmethod
    async def close(cls):
        if cls._connection:
            await cls._connection.close()

    @classmethod
    async def fetch_compliance_rules(cls):
        print("here", cls._connection)
        async with cls._connection.cursor() as cur:
            print("in")

            await cur.execute("SELECT * FROM compliance_rules")
            print("deeper")

            results = await cur.fetchall()
            print("results ", results)
            return results