import importlib_resources
import spiceypy as spice

# Load leap second kernel if not loaded already
lsk = importlib_resources.files("uvisaurorae.resources").joinpath("naif0012.tls")  # type: ignore
try:
    spice.kinfo(str(lsk))
except spice.stypes.SpiceyError:
    spice.furnsh(str(lsk))
