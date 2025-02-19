from typing import List
from fastapi import APIRouter, Depends
from models.learn_model import Article, Section
from services.auth_helper import oauth2_scheme
from engine.articles import get_articles, get_sections

learn_router = APIRouter(tags=["learn"])

@learn_router.get("/get_articles", response_model=List[Article])
async def get_db_article():
    data = await get_articles()
    return data


@learn_router.get("/get_section", response_model=List[Section])
async def get_article_sections(article_id: int):
    data = await get_sections(article_id)
    return data