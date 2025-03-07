from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, EmailStr, Field

from lna_app.core.types import Language, UUIDstr


class UserPreferences(BaseModel):
    """
    Stores the user's preferences, such as which sources they follow
    and their preferred language.

    Attributes:
        source_ids: List of unique identifiers (UUIDs) of the sources a user follows.
        language: The preferred language in which the user wants to read news.
    """

    source_ids: list[UUIDstr] = Field(
        default_factory=list, description="List of Source IDs that the user follows."
    )
    language: Language = Field(
        Language.UNKNOWN, description="Preferred language for reading news."
    )


class User(BaseModel):
    """
    Represents a user in the system.

    Attributes:
        id: Unique identifier for the user.
        email: Email address used for contact and authentication.
        preferences: User preferences, including source subscriptions and language.
    """

    id: UUIDstr = Field(
        default_factory=uuid4, description="Unique identifier for the user (UUID)."
    )
    email: EmailStr = Field(..., description="User's email address.")
    preferences: UserPreferences = Field(
        default_factory=UserPreferences,
        description="User's saved preferences (sources followed, language).",
    )


class Source(BaseModel):
    """
    Represents a source from which articles can be collected.

    Attributes:
        id: Unique identifier for the source (UUID).
        name: Display name of the source.
        urls: List of URLs associated with the source (e.g., homepage, RSS feed).
    """

    id: UUIDstr = Field(
        default_factory=uuid4, description="Unique identifier for the source (UUID)."
    )
    name: str = Field(
        ..., description="Display name of the source (e.g., 'Daily Star Lebanon')."
    )
    url: str = Field(
        ..., description="URL (homepage or RSS feed) associated with this source."
    )


class Article(BaseModel):
    """
    Represents a single article fetched from a given source.

    Attributes:
        id: Unique identifier for the article (UUID).
        source_id: ID referencing the Source from which this article was collected.
        url: Direct URL to the article.
        publish_date: Date and time when the article was published.
        title: Title of the article.
        content: Full body text of the article.
        language: Language of the article, defaults to UNKNOWN if undetermined.
    """

    id: UUIDstr = Field(
        default_factory=uuid4, description="Unique identifier for the article (UUID)."
    )
    source_id: UUIDstr = Field(
        ..., description="Reference to the Source.id this article belongs to."
    )
    url: str = Field(..., description="Direct URL to the published article.")
    publish_date: datetime = Field(
        ..., description="Date and time when the article was published."
    )
    title: str = Field(..., description="Title of the article.")
    content: str = Field(..., description="Full body text of the article.")
    language: Language = Field(
        Language.UNKNOWN, description="Language of the article; defaults to UNKNOWN."
    )


class AggregatedStory(BaseModel):
    """
    Represents a clustered or aggregated news 'event' or 'story,'
    which groups multiple articles covering the same topic or event.

    Attributes:
        id: Unique identifier for the aggregated story (UUID).
        title: System-generated or AI-generated title describing the cluster.
        summary: A short summary of the story or event.
        language: Language of the aggregated story (usually the dominant language).
        publish_date: Representative date for the story (e.g., earliest publish date
        among articles).
        article_ids: List of article IDs (UUIDs) that belong to this aggregated story.
    """

    id: UUIDstr = Field(
        default_factory=uuid4,
        description="Unique identifier for the aggregated story (UUID).",
    )
    title: str = Field(..., description="Descriptive title for the aggregated story.")
    summary: str = Field(
        ..., description="Short overview or summary of the aggregated story."
    )
    language: Language = Field(..., description="Language of the aggregated story.")
    publish_date: datetime = Field(
        ..., description="Representative publish date (e.g., earliest article date)."
    )
    article_ids: list[UUIDstr] = Field(
        ..., description="List of UUIDs referencing articles in this story cluster."
    )


class AggregatedStoryListResponse(BaseModel):
    """
    Represents a list of aggregated stories.
    """

    stories: list[AggregatedStory] = Field(
        ..., description="List of aggregated stories."
    )
