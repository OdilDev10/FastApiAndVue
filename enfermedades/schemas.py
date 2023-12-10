from pydantic import BaseModel
from typing import Optional, Union, Text
from datetime import datetime

class Schema_enfermedades(BaseModel):
    id: Union[str, int, None] = None
    email: str
    password: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    
class Schema_enfermedades_create_or_update(BaseModel):
    email: str
    password: str
    