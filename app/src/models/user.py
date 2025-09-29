from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.src.database.session import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fullname: Mapped[str] = mapped_column(index=True)
    email: Mapped[str] = mapped_column(index=True)

    orders: Mapped[list["Order"]] = relationship(back_populates="user")  # type: ignore # noqa: F821
    products: Mapped[list["Product"]] = relationship(back_populates="owner")  # type: ignore # noqa: F821
