from typing import Any, Union

from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo.collection import Collection

from lna_app.schema.schema import AggregatedStory


async def fetch_stories(
    db: Union[AsyncIOMotorDatabase, Collection],
) -> list[AggregatedStory]:
    """Fetch all stories from MongoDB (supports both async and mock DB)."""

    cursor = db.stories.find()  # Get cursor

    if isinstance(db, AsyncIOMotorDatabase):
        # MongoDB (async) → Use async iteration
        raw_stories: list[dict[str, Any]] = [story async for story in cursor]
    else:
        # Mongomock (sync) → Convert cursor to list directly
        raw_stories = list(cursor)

    return [AggregatedStory(**story) for story in raw_stories]
