from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from sqlalchemy import ForeignKey
from typing import Optional

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    num_of_moons: Mapped[int]
    moon_id: Mapped[Optional[int]] = mapped_column(ForeignKey("moon.id"))
    moon: Mapped[Optional["Moon"]] = relationship(back_populates="planet")

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            num_of_moons=self.num_of_moons,
            moon=self.moon.name if self.moon else None
        )
    
    @classmethod
    def from_dict(cls, planet_data):
        return cls(
            name=planet_data['name'],
            description=planet_data['description'],
            num_of_moons=planet_data['num_of_moons'],
            moon_id=planet_data.get("moon_id", None)
        )
