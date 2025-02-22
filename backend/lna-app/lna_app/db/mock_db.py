from datetime import datetime
from uuid import UUID

from mongomock import MongoClient
from pymongo.database import Database

client: MongoClient = MongoClient()
db: Database = client.test_database

# Create sample source
source_id = UUID("550e8400-e29b-41d4-a716-446655440000")
db.sources.insert_one(
    {
        "id": str(source_id),
        "name": "Global News Network",
        "url": "https://news.com",
    }
)

# Create Arabic sample source
arabic_source_id = UUID("660e8400-e29b-41d4-a716-446655440000")
db.sources.insert_one(
    {
        "id": str(arabic_source_id),
        "name": "الشبكة الإخبارية العربية",  # Arabic News Network
        "url": "https://arabnews.com",
    }
)

# Create sample articles
article_1_id = UUID("a631c8c8-5943-4d7d-b7bc-6d7f8e569e6b")
article_2_id = UUID("b724d849-5ad3-4e42-a29c-50049c6f4b38")

# Create Arabic sample articles
arabic_article_1_id = UUID("d631c8c8-5943-4d7d-b7bc-6d7f8e569e6b")
arabic_article_2_id = UUID("e724d849-5ad3-4e42-a29c-50049c6f4b38")

db.articles.insert_many(
    [
        {
            "id": str(article_1_id),
            "source_id": str(source_id),
            "title": "Breaking News",
            "content": "Something big happened! Here's the full story...",
            "summary": "Something big happened!",
            "url": "https://news.com/breaking",
            "publish_date": datetime(2024, 3, 15, 12, 30),
            "language": "en",
        },
        {
            "id": str(article_2_id),
            "source_id": str(source_id),
            "title": "Tech Update",
            "content": "AI is taking over the world. Here's what you need to know...",
            "summary": "AI is taking over the world",
            "url": "https://news.com/ai",
            "publish_date": datetime(2024, 3, 15, 14, 45),
            "language": "en",
        },
        {
            "id": str(arabic_article_1_id),
            "source_id": str(arabic_source_id),
            "title": "تطورات جديدة في مجال التكنولوجيا",
            "content": "شهد عالم التكنولوجيا تطورات مثيرة في مجال الذكاء الاصطناعي...",
            "summary": "أحدث التطورات في مجال التكنولوجيا والذكاء الاصطناعي",
            "url": "https://arabnews.com/tech-news",
            "publish_date": datetime(2024, 3, 15, 13, 30),
            "language": "ar",
        },
        {
            "id": str(arabic_article_2_id),
            "source_id": str(arabic_source_id),
            "title": "مستقبل الذكاء الاصطناعي",
            "content": "يتوقع الخبراء أن يشهد مجال الذكاء الاصطناعي تطورات كبيرة...",
            "summary": "توقعات مستقبلية حول تطور الذكاء الاصطناعي",
            "url": "https://arabnews.com/ai-future",
            "publish_date": datetime(2024, 3, 15, 15, 45),
            "language": "ar",
        },
    ]
)

# Create sample aggregated story
db.stories.insert_one(
    {
        "id": str(UUID("c834d941-4fd2-4819-a3b7-7cc8971ab25e")),
        "title": "Technology Advances in 2024",
        "summary": "Latest developments in AI and tech sector",
        "language": "en",
        "publish_date": datetime(2024, 3, 15, 12, 30),
        "article_ids": [str(article_1_id), str(article_2_id)],
    }
)

# Create Arabic aggregated story
db.stories.insert_one(
    {
        "id": str(UUID("d834d941-4fd2-4819-a3b7-7cc8971ab25e")),
        "title": "مستقبل التكنولوجيا والذكاء الاصطناعي",
        "summary": "آخر التطورات والتوقعات في مجال التكنولوجيا والذكاء الاصطناعي",
        "language": "ar",
        "publish_date": datetime(2024, 3, 15, 13, 30),
        "article_ids": [str(arabic_article_1_id), str(arabic_article_2_id)],
    }
)


def get_mock_db() -> Database:
    """Returns the mock MongoDB instance."""
    return db
