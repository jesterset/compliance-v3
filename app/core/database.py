import psycopg
from psycopg.rows import dict_row
from app.core.config import get_config

class Database:
    _connection: psycopg.AsyncConnection | None = None

    @classmethod
    async def connect(cls):
        """
        Connects to the PostgreSQL database using the provided URL.

        Returns:
            None
        """
        if cls._connection is None:
            config = get_config()  # Get the configuration lazily
            cls._connection = await psycopg.AsyncConnection.connect(config.postgres.host)

    @classmethod
    async def close(cls):
        """
        Closes the connection to the database.

        Returns:
            None
        """
        if cls._connection:
            await cls._connection.close()
            cls._connection = None

    @classmethod
    async def fetch_compliance_rules(cls):
        """
        Fetches all compliance rules from the database.

        Returns:
            list: A list of dictionaries representing the compliance rules.
        """
        await cls.connect()
        async with cls._connection.cursor(row_factory=dict_row) as cur:
            await cur.execute("SELECT * FROM compliance_rules;")
            results = await cur.fetchall()
            return [row for row in results]

    @classmethod
    async def fetch_chat_messages(cls):
        """
        Fetches all chat messages from the database.

        Returns:
            list: A list of dictionaries representing the chat messages.
        """
        await cls.connect()
        async with cls._connection.cursor(row_factory=dict_row) as cur:
            await cur.execute(
                "SELECT * FROM chat_messages WHERE timestamp BETWEEN '2024-09-12T01:01:01' AND '2024-09-12T01:01:01';"
            )
            results = await cur.fetchall()
            return [row for row in results]