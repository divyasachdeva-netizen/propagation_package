import crpropa
from crpropa import ModuleList

def setup_simple_propagation(maxlen=3000 * crpropa.Mpc):
    """Returns a CRPropa ModuleList for straight-line photon propagation."""
    sim = ModuleList()
    sim.add(crpropa.SimplePropagation(maxlen))
    return sim
