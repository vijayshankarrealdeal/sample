from pydantic import BaseModel
from typing import List, Optional

class Section(BaseModel):
    id: int
    heading: str
    content: str
    article_id: int

class Article(BaseModel):
    id: int
    title: str
    introduction: str
    conclusion: str
    sections_count: int

    
