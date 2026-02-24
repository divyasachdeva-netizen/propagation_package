

```python
import numpy as np

def powerlaw(E, index, norm=1.0, E0=1e9):
    """Simple E^-index spectrum."""
    return norm * (E/E0)**(-index)
