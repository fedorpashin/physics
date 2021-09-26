from physics.grids.common_grid import CommonGrid
from physics.grids.common_auxiliary_grid import CommonAuxiliaryGrid
from physics.grids.uniform_grid import UniformGrid
from physics.grids.uniform_auxiliary_grid import UniformAuxiliaryGrid

from multimethod import multimeta
from final_class import final

__all__ = ['AuxiliaryGrid']


@final
class AuxiliaryGrid(metaclass=multimeta):
    def __new__(cls, grid: CommonGrid) -> CommonAuxiliaryGrid:
        return CommonAuxiliaryGrid(grid)

    def __new__(cls, grid: UniformGrid) -> UniformAuxiliaryGrid:  # type: ignore
        return UniformAuxiliaryGrid(grid)
