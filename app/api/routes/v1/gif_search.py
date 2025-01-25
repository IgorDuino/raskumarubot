import logging
from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.core.db.models import GIF
from tortoise.exceptions import DoesNotExist

logger = logging.getLogger(__name__)
router = APIRouter(tags=["gif_search"])


@router.get("/search", response_model=List[GIF])
async def search_gifs(tags: List[str] = Query(..., description="List of tags to search for")):
    try:
        gifs = await GIF.filter(tags__overlap=tags)
        if not gifs:
            raise HTTPException(status_code=404, detail="No GIFs found for the given tags")
        return gifs
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="No GIFs found for the given tags")
    except Exception as e:
        logger.error(f"Error searching GIFs: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
