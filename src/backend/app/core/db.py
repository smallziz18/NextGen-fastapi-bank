from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from backend.app.core.config import settings
from backend.app.logging import get_logger

logger = get_logger()
engine = create_async_engine(
    settings.DATABASE_URL
)
async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        except Exception as e:
            logger.error(e)
            await session.rollback()
            raise
        finally: await session.close()


def init_db() -> None:
    pass