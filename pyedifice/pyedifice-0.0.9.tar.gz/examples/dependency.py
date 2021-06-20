import edifice as ed

class OtherComp(ed.Component):

    @ed.register_props
    def __init__(self, a):
        self.b = 0

    def render(self):
        return ed.Label(self.props.a + self.b)
