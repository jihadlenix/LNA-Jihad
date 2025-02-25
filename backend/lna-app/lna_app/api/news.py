from datetime import datetime
from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID, uuid4

from ..schema.schema import Language, UserPreferences, User, Source, Article, AggregatedStory

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
router = APIRouter()
# Fixed UUIDs for sources, articles, users, and aggregated stories
source1_id = UUID("f47ac10b-58cc-4372-a567-0e02b2c3d479")
source2_id = UUID("810b14da-11d3-4e58-a9be-adf922c3d678")

article1_id = UUID("76e6d807-2d55-419e-8a7b-9634ac9fa47a")
article2_id = UUID("6a96829f-41a2-4b96-9348-cf18b1233654")
aggregated_story_id = UUID("c430c8ef-868f-4189-9e53-c64151882e40")

# Dummy Sources

sources = [
Source(
    id=source1_id,
    name="Global News",
    url="http://globalnews.com/feed"
)
,
Source(
    id=source2_id,
    name="Tech Daily",
    url="http://techdaily.com/feed"
)
]

articles = [
Article(
    id=article1_id,
    source_id=source1_id,
    url="http://globalnews.com/quantum-computing-breakthrough",
    publish_date=datetime.now(),
    title="Quantum Computing Breakthrough Achieved at MIT Labs",
    content="Researchers at MIT have successfully demonstrated error correction...",
    language=Language.ENGLISH
),

Article(
    id=article2_id,
    source_id=source2_id,
    url="http://techdaily.com/new-ai-chip",
    publish_date=datetime.now(),
    title="New AI Chip Speeds Up Machine Learning",
    content="A new AI chip released today promises to radically improve the speed...",
    language=Language.ENGLISH
)
]



# Dummy Aggregated Story
aggregated_stories = [AggregatedStory(
    id=aggregated_story_id,
    title="Advancements in Technology",
    summary="A summary of recent breakthroughs in technology and AI.",
    language=Language.ENGLISH,
    publish_date=datetime.now(),
    article_ids=[article1_id, article2_id]
)]

@router.get("/aggregated-stories/", response_model=List[dict])  # Custom response using dict to manage returned data structure
async def get_aggregated_stories():
    results = []
    for story in aggregated_stories:
        story_data = {
            "id": str(story.id),
            "title": story.title,
            "summary": story.summary,
            "language": story.language.name,  # Ensure the output is string representation of the enum
            "publish_date": story.publish_date.isoformat(),
            "articles": []
        }
        for article_id in story.article_ids:
            article = next((a for a in articles if a.id == article_id), None)
            if article:
                source = next((s for s in sources if s.id == article.source_id), None)
                if source:
                    story_data["articles"].append({
                        "article_title": article.title,
                        "article_url": article.url,
                        "article_content":article.content,
                        "source_name": source.name,
                        "source_url": source.url

                    })
        results.append(story_data)
    return results

@router.get("/articles/{article_id}", response_model=Article)
async def get_article(article_id: UUID):
    for article in articles:
        if article.id == article_id:
            return article
    raise HTTPException(status_code=404, detail="Article not found")