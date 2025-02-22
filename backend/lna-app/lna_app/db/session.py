from motor.motor_asyncio import AsyncIOMotorDatabase

from lna_app.db.mongo import get_db as get_real_db


async def get_database() -> AsyncIOMotorDatabase:
    """Returns the real CosmosDB database."""
    return await get_real_db()
