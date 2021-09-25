from physics.length import HasLength

from dataclasses import dataclass
from typing import Union

__all__ = ['Interval']


@dataclass(frozen=True)
class Interval(HasLength):
    l: Union[float, int]
    r: Union[float, int]

    def __post_init__(self):
        assert self.l < self.r

    @property
    def length(self) -> float:
        return self.r - self.l
