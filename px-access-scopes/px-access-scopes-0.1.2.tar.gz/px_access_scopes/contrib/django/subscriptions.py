from .generator import generate_all
from .globals import registries, aggregates


__all__ = 'generate_data_on_migrate',


def generate_data_on_migrate(sender, **kwargs):
    generate_all(registries, aggregates)
