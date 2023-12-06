from pydantic import BaseModel
from typing import Optional, Union, Text
from datetime import datetime


class Schema_tasks(BaseModel):
    id: Optional[Union[str, int, None]] = None
    name: str
    description: Text
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class Schema_tasks_create_or_update(BaseModel):
    name: str
    description: Text
