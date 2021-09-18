from physics.boundary_conditions.boundary_condition import BoundaryCondition

from dataclasses import dataclass
from final_class import final

__all__ = ['SecondTypeBoundaryCondition']


@final
@dataclass(frozen=True)
class SecondTypeBoundaryCondition(BoundaryCondition):
    ν: float
