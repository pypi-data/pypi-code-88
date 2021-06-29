import importlib.resources


def extension_metadata():
    return {
        "priority": -100,
        "web_resources": {
            "static": [importlib.resources.files("DIRACWebAppResources") / "WebApp" / "static"],
        }
    }
