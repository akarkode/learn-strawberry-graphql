from app.src.models.product import Product
from app.src.database.session import session_manager


def get_product(
    id: int | None = None,
    name: str | None = None,
    owner_id: int | None = None,
    limit: int = 20,
):
    with session_manager() as db:
        filters = []
        if id:
            filters.append(Product.id == id)
        if name:
            filters.append(Product.name.ilike(f"%{name}%"))
        if owner_id:
            filters.append(Product.owner_id == owner_id)

        product = db.query(Product).filter(*filters).limit(limit).first()
        if not product:
            raise FileNotFoundError("Product not found")

        _ = product.owner
        return product
