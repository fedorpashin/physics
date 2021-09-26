from physics.boundary_conditions.boundary_condition import BoundaryCondition

from dataclasses import dataclass
from final_class import final
from overrides import overrides

__all__ = ['FirstTypeBoundaryCondition']


@final
@dataclass
class FirstTypeBoundaryCondition(BoundaryCondition):
    __ν: float

    def __init__(self, ν: float):
        self.__ν = ν

    @property  # type: ignore
    @overrides
    def ν(self) -> float:
        return self.__ν
