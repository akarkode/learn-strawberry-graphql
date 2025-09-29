from sqlalchemy.orm import validates
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.src.database.session import Base

class Product(Base):
    __tablename__ = "products"
    __table_args__ = (
        CheckConstraint('qty >= 0', name='check_qty_non_negative'),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(index=True, nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    qty: Mapped[int] = mapped_column(nullable=False, default=0)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped["User"] = relationship(back_populates="products") # type: ignore # noqa: F821

    @validates("qty")
    def validate_qty(self, _, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        return value