def sequence_repr(self):
    data = "<akida.Sequence"
    data += ", name=" + self.name
    data += ", backend=" + str(self.backend).split('.')[-1]
    data += ", layers="
    program = self.program
    if program is None:
        data += repr(self.layers)
    else:
        data += "["

        def layer_config(layer):
            config = [
                "layer=" + repr(layer), "nps=" + repr(program.config(layer))
            ]
            return "{" + ", ".join(config) + "}"

        layers = [layer_config(layer) for layer in self.layers]
        data += ", ".join(layers) + "]"
        data += ", program_size=" + str(len(program.to_buffer()))
    data += ">"
    return data
