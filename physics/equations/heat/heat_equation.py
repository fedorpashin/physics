from physics.equations.any_equation import AnyEquation
from physics.interval import Interval
from physics.boundary_conditions.boundary_condition import BoundaryCondition

from dataclasses import dataclass
from typing import Callable

__all__ = ['HeatEquation']


@dataclass(frozen=True)
class HeatEquation(AnyEquation):
    interval: Interval
    k: Callable[[float], float]
    q: Callable[[float], float]
    f: Callable[[float], float]
    left_boundary_condition: BoundaryCondition
    right_boundary_condition: BoundaryCondition
