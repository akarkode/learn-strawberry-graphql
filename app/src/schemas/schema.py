from __future__ import annotations

import strawberry
from typing import List

from app.src.resolvers.user import get_user
from app.src.resolvers.product import get_product


@strawberry.type
class User:
    id: int
    fullname: str
    email: str
    products: List[Product]
    orders: List[Product]


@strawberry.type
class Product:
    id: int
    name: str
    price: float
    qty: int
    owner: User

@strawberry.type
class Query:
    user: User = strawberry.field(resolver=get_user)
    product: Product = strawberry.field(resolver=get_product)