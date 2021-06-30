def get_custom_tf_versions():
    return {"versions":
                {"0.12": "45",
                 "0.13": "39",
                 "0.14": "43",
                 "0.15": "22",
                 "1.0": "13"},
            "architectures": {
                "0.12": ["linux-amd64", "darwin-amd64"],
                "0.13": ["linux-amd64", "darwin-amd64"],
                "0.14": ["linux-amd64", "darwin-amd64"],
                "0.15": ["linux-amd64", "darwin-amd64", "darwin-arm64"],
                "1.0": ["linux-amd64", "darwin-amd64", "darwin-arm64"]}}
