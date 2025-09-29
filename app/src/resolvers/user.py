from app.src.models.user import User
from app.src.models.order import Order
from app.src.models.product import Product
from app.src.database.session import session_manager


def get_user(
    id: int | None = None,
    email: str | None = None,
    fullname: str | None = None,
    order_id: int | None = None,
    product_id: int | None = None,
    limit: int = 20,
):
    with session_manager() as db:
        filters = []
        if id:
            filters.append(User.id == id)
        if email:
            filters.append(User.email == email)
        if fullname:
            filters.append(User.fullname.ilike(f"%{fullname}%"))
        if order_id:
            filters.append(Order.id == order_id)
        if product_id:
            filters.append(Product.id == product_id)

        query = (
            db.query(User)
            .join(Order, Order.user_id == User.id)
            .join(Product, Product.owner_id == User.id)
            .filter(*filters)
            .limit(limit)
        )

        user = query.first()
        if not user:
            raise FileNotFoundError("User not found")

        _ = user.products
        _ = [p.owner for p in user.products]
        return user
