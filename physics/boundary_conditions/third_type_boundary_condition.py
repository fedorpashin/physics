from physics.boundary_conditions.boundary_condition import BoundaryCondition

from dataclasses import dataclass
from final_class import final
from overrides import overrides

__all__ = ['ThirdTypeBoundaryCondition']


@final
@dataclass
class ThirdTypeBoundaryCondition(BoundaryCondition):
    __ν: float
    __κ: float

    def __init__(self, ν: float, κ: float):
        self.__ν = ν
        self.__κ = κ

    @property  # type: ignore
    @overrides
    def ν(self) -> float:
        return self.__ν

    @property
    def κ(self) -> float:
        return self.__κ
