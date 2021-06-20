import edifice as ed


class MyApp(ed.Component):
    def __init__(self):
        super().__init__()
        self.spawned_windows = set()
        self.counter = 0
        self.main_window_open = True

    def create_window(self, e):
        with self.render_changes():
            self.spawned_windows = self.spawned_windows | {self.counter}
            self.counter += 1

    def close_window(self, i, e):
        with self.render_changes():
            self.spawned_windows = self.spawned_windows - {i}

    def close_main_window(self, e):
        with self.render_changes():
            self.spawned_windows = set()
            self.main_window_open = False

    def render(self):
        return ed.List()(
            self.main_window_open and ed.Window(on_close=self.close_main_window)(
                ed.Button("New window", on_click=self.create_window),
            ),
            *[
                ed.Window(on_close=lambda e, idx=i: self.close_window(idx, e))(
                    ed.Label(f"Window {i + 1}"),
                ).set_key(str(i))
                for i in self.spawned_windows
            ],
        )

if __name__ == "__main__":
    ed.App(MyApp()).start()
