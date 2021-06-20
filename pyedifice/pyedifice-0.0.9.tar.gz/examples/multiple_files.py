from . import dependency
import edifice as ed

class App(ed.Component):

    def __init__(self):
        super().__init__()
        self.a = 1

    def render(self):
        print(id(dependency.OtherComp))
        return ed.View(layout="column")(
            dependency.OtherComp(self.a),
            ed.Label(self.a),
            ed.Button("Add 1", on_click=lambda e: self.set_state(a=self.a+1)),
        )
