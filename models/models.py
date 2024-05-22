from datetime import datetime, timezone
from sqlalchemy import TIMESTAMP, ForeignKey, Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    registered_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Salary(Base):
    __tablename__ = "salary"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Связка с User
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    current_salary: Mapped[int] = mapped_column(Integer, nullable=False)
    next_raise_date: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False
    )
