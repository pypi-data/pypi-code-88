
import pkg_resources

IONIZATION_DATA_PATH = pkg_resources.resource_filename(
    "pyeqeq", "data/ionizationdata.dat"
)
CHARGE_DATA_PATH = pkg_resources.resource_filename("pyeqeq", "data/chargecenters.dat")
