from __future__ import annotations

from dataclasses import dataclass
from typing import Union

__all__ = ("Vector2D",)


@dataclass
class Vector2D:
    x: float
    y: float

    def __add__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: Vector2D) -> Vector2D:
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other: Vector2D) -> Vector2D:
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other: Union[float, int]) -> Vector2D:
        return Vector2D(other * self.x, other * self.y)

    def __rmul__(self, other: Union[float, int]) -> Vector2D:
        return self * other

    def __imul__(self, other: Union[float, int]) -> Vector2D:
        self.x *= other
        self.y *= other
        return self
