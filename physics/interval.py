from dataclasses import dataclass
from typing import Union

__all__ = ['Interval']


@dataclass(frozen=True)
class Interval:
    l: Union[float, int]
    r: Union[float, int]

    def __post_init__(self):
        assert self.l < self.r
