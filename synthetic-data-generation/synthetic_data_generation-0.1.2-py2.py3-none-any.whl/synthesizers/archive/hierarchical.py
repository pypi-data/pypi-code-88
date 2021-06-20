class HierarchicalAttribute(DiscreteNetworkNode):

    def __init__(self, RV, name=None, description='', hierarchy=None, height=0, generalization_level=0):
        super().__init__(RV=RV, name=name, description=description)

        # hierarchy: {value: [list of generalized values], ...}
        # height of the hierarchy - assume 0 if no hierarchy is given.
        self.hierarchy, self.height = self._check_hierarchy(hierarchy, height)
        self.generalization_level = generalization_level

    def _check_hierarchy(self, hierarchy, height):
        if not hierarchy and height > 0:
            raise ValueError('Height cannot be higher than 0 if hierarchy is None')
        if hierarchy is not None and not isinstance(hierarchy, dict):
            raise ValueError('Hierarchy should be a dict of form: {value: [list of generalized values], ...}')
        if hierarchy and height == 0:
            raise ValueError('Define the height of the hierarchy ')

        return hierarchy, height

    def add_hierarchy(self, hierarchy, height):
        self.hierarchy, self.height = self._check_hierarchy(hierarchy, height)

    def generalize(self, data, generalization_level):
        if generalization_level <= self.height:
            raise ValueError('Generalization level cannot exceed the height of the attribute')
        pass

    def __repr__(self):
        """x.__repr__() <==> repr(x)"""
        components = [f"Generalizedattribute('{self.RV}'"]

        if self.name:
            components.append(f"name='{self.name}'")
        if self.states:
            states = ', '.join([f"'{s}'" for s in self.states])
            components.append(f"states=[{states}]")
        if self.description:
            components.append(f"description='{self.description}'")
        components.append(f"height='{self.height}")
        return ', '.join(components) + ')'



    # def create_hierarchy(data, n_bins):
    #     unique_values = data.unique()
    #     unique_values.sort()
    #
    #     bin_size = np.int(np.ceil(len(unique_values) / n_bins))
    #
