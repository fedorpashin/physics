from physics.boundary_conditions.boundary_condition import BoundaryCondition

from dataclasses import dataclass
from final_class import final

__all__ = ['ThirdTypeBoundaryCondition']


@final
@dataclass(frozen=True)
class ThirdTypeBoundaryCondition(BoundaryCondition):
    ν: float
    κ: float
