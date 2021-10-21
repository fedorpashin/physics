# physics

[![build](https://github.com/fedorpashin/physics/workflows/build/badge.svg)](https://github.com/fedorpashin/linalg/actions)
[![codecov](https://codecov.io/gh/fedorpashin/physics/branch/master/graph/badge.svg?token=TFJEK2G1FB)](https://codecov.io/gh/fedorpashin/linalg)
[![Maintainability](https://api.codeclimate.com/v1/badges/4ab431eca5f8c0ff3b3c/maintainability)](https://codeclimate.com/github/fedorpashin/physics/maintainability)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![Managed By Self XDSD](https://self-xdsd.com/b/mbself.svg)](https://self-xdsd.com/p/fedorpashin/physics?provider=github)

## Usage

```python
import physics as ph

print(
    ph.IntegroInterpolationMethod().solution(
        ph.HeatEquation(
            interval=(interval := ph.Interval(0, 2)),
            k=lambda x: x**2 + 3,
            q=lambda x: 10,
            f=lambda x: 4 * (x**2 + 11),
            left_boundary_condition=ph.FirstTypeBoundaryCondition(5),
            right_boundary_condition=ph.FirstTypeBoundaryCondition(9)
        ),
        ph.UniformGrid(
            interval=interval,
            num_parts=10
        )
    )
)
```
