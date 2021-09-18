from physics.boundary_conditions.boundary_condition import BoundaryCondition

from dataclasses import dataclass
from final_class import final

__all__ = ['FirstTypeBoundaryCondition']


@final
@dataclass(frozen=True)
class FirstTypeBoundaryCondition(BoundaryCondition):
    ν: float
