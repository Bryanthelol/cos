from typing import Optional

from lin import BaseModel


class CosOutSchema(BaseModel):
    id: int
    file_name: str
    file_key: str
    url: str
