from pydantic import BaseModel
from typing import Optional, Union, Text
from datetime import datetime

class Schema_pets(BaseModel):
    id: Union[str, int, None] = None
    name: str
    age: int
    owner: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    
class Schema_pets_create_or_update(BaseModel):
    name: str
    age: int
    owner: int
    