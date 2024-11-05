from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db


class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    size: Mapped[str]
    description: Mapped[str]
    planet: Mapped[list["Planet"]] = relationship(back_populates="moon")
    

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            size=self.size,
            description=self.description,
        )

    @classmethod
    def from_dict(cls, moon_data):
        return cls(
            name=moon_data['name'],
            size=moon_data['size'],
            description=moon_data['description']
        )
