from pydantic import BaseModel
from typing import List


class Symbol(BaseModel):
    symbol: str


# распарсим
class Symbols(BaseModel):
    symbols: List[Symbol]
