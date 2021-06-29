'''
====================
Convenience Kinetics
====================
'''
import os

from vivarium.core.composer import Composer
from vivarium.core.composition import (
    composite_in_experiment,
    simulate_experiment,
    COMPOSITE_OUT_DIR,
)
from vivarium.plots.simulation_output import plot_simulation_output
from vivarium.library.units import units
from vivarium.library.timeseries import (
    flatten_timeseries, load_timeseries,
    save_timeseries, assert_timeseries_close)

from vivarium.processes.ecoli_shape_deriver import EcoliShape
from vivarium_multibody.processes.local_field import LocalField

from vivarium_convenience.processes.convenience_kinetics import ConvenienceKinetics, get_glc_lct_config
from vivarium_convenience.reference_data import REFERENCE_DATA_DIR

NAME = 'convenience_composite'


class ConvenienceComposite(Composer):
    defaults = {
        'convenience_kinetics': {},
        'local_field': {},
        'ecoli_shape': {
            'width': 1.0}
    }
    def __init__(self, config):
        super().__init__(config)

    def generate_processes(self, config):
        return {
            'convenience_kinetics': ConvenienceKinetics(config['convenience_kinetics']),
            'local_field': LocalField(config['local_field']),
            'ecoli_shape': EcoliShape(config['ecoli_shape']),
        }

    def generate_topology(self, config):
        return {
            'convenience_kinetics': {
                'exchanges': ('exchanges',),
                'external': ('external',),
                'fluxes': ('fluxes',),
                'global': ('global',),
                'internal': ('internal',)
            },
            'local_field': {
                'exchanges': ('exchanges',),
                'location': ('location',),
                'fields': ('fields',),
                'dimensions': ('dimensions',),
            },
            'ecoli_shape': {
                'global': ('global',)
            },
        }


def test_convenience_composite(total_time=2520):
    config = {
        'convenience_kinetics': get_glc_lct_config()}
    composer = ConvenienceComposite(config)
    composite = composer.generate()

    # get the initial state
    initial_state = composite.initial_state()
    initial_state['external'] = {
            'glc__D_e': 1.0,
            'lcts_e': 1.0}

    # make the experiment and run it
    settings = {
        'environment': {
            'volume': 1e-14 * units.L,
            'concentrations': initial_state['external'],
        },
        'total_time': total_time}

    experiment = composite_in_experiment(
        composite=composite,
        settings=settings,
        initial_state=initial_state)
    data = simulate_experiment(experiment, settings)
    return data


def test_convenience_kinetics_correlated_to_reference():
    timeseries = test_convenience_composite()
    flattened = flatten_timeseries(timeseries)
    reference_timeseries = load_timeseries(
        os.path.join(REFERENCE_DATA_DIR, NAME + '.csv'))
    assert_timeseries_close(
        flattened, reference_timeseries,
        tolerances={
            'internal_pyr_c': 9,
            'internal_pep_c': 9,
            'internal_g6p_c': 9,
        }
    )


def main():
    out_dir = os.path.join(COMPOSITE_OUT_DIR, NAME)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    timeseries = test_convenience_composite()

    plot_settings = {}
    plot_simulation_output(timeseries, plot_settings, out_dir)
    save_timeseries(timeseries, out_dir)


# run module with python vivarium_convenience/processes/convenience_kinetics.py
if __name__ == '__main__':
    main()