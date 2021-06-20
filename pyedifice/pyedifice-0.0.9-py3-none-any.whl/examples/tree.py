import edifice as ed

class TreeView(ed.Component):

    @ed.register_props
    def __init__(self, title):
        super().__init__()
        self.collapsed = False

    def toggle(self, e):
        self.set_state(collapsed=not self.collapsed)

    def render(self):
        child = None
        if not self.collapsed:
            child = ed.View(layout="row", style={"align": "left"})(
                ed.View(layout="column", style={"width": 20, }).set_key("indent"),
                ed.View(layout="column", style={"align": "top"})(
                    *[comp.set_key(str(i)) for i, comp in enumerate(self.props.children)]
                ).set_key("children")
            ).set_key("children")
        return ed.View(layout="column", style={"align": "top"})(
            ed.View(layout="row", style={"align": "left"})(
                ed.Icon("caret-right",
                        rotation=0 if self.collapsed else 90,
                        on_click=self.toggle,
                ).set_key("caret"),
                ed.Label(self.props.title, style={"margin-left": 5}).set_key("title"),
            ).set_key("root"),
            child
        )

class App(ed.Component):

    def __init__(self):
        super().__init__()
        self.selected = None

    def render(self):
        return ed.View(layout="row")(
            ed.ScrollView(layout="column", style={"width": 220, "min-height": 450})(
                TreeView(title="A")(
                    TreeView("Ap")(
                        ed.Label("App", on_click=lambda e: self.set_state(selected="App")),
                        ed.Label("Apple", on_click=lambda e: self.set_state(selected="Apple")),
                    ),
                    ed.Label("Hi", on_click=lambda e: self.set_state(selected="Hi")),
                )
            ),
            ed.View(layout="column", style={"min-width": 400, "height": 450})(
                self.selected and ed.Label(self.selected, style={"font-size": "20px"})
            )
        )
