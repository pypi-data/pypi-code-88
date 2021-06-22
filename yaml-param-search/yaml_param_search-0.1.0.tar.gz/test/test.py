from yaml_param_search import Config


config = Config("template", "search.yaml")
for i in config.yield_param():
    config.write_logs(i)