# Copyright (c) 2021, Moritz E. Beber.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Provide a class for major microspecies computation."""


from .abstract_chemaxon_adapter import AbstractChemAxonAdapter
from .chemaxon_manager import ChemAxonManager
from .chemaxon_molecule import ChemAxonMolecule


class MajorMicrospecies(AbstractChemAxonAdapter):
    """Define an adapter for the ChemAxon MajorMicrospeciesPlugin."""

    _plugin_cls = (
        ChemAxonManager.get_instance().chemaxon.marvin.calculations.MajorMicrospeciesPlugin  # noqa: E501
    )

    def __init__(
        self,
        *,
        ph: float = 7.0,
        keep_hydrogens: bool = False,
        **kwargs,
    ) -> None:
        """
        Initialize the major microspecies' parameters.

        Parameters
        ----------
        ph
            Compute major microspecies at this pH (default 7.0).
        keep_hydrogens
            Determine whether result molecule keeps explicit hydrogens or not
            (default false).
        """
        super().__init__(**kwargs)
        self._plugin.setpH(ph)
        self._plugin.setKeepExplicitHydrogens(keep_hydrogens)

    def get_major_microspecies(self) -> ChemAxonMolecule:
        """Return the major microspecies at the specified pH value."""
        self._check_molecule_is_set()
        return ChemAxonMolecule(molecule=self._plugin.getMajorMicrospecies())
