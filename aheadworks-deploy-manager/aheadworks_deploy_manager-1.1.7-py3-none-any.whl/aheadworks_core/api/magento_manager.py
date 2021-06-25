from aheadworks_core.model.parser.json import Json as JsonParser


class MagentoManager:
    """manager for magento"""

    def __init__(self):
        self.json_parser = JsonParser()

    def get_module_dependencies_from_composer(self, composer_file):
        list_of_modules = dict()

        core_full_module_name = self.json_parser.get_variable_from_file('name', composer_file)
        core_version = self.json_parser.get_variable_from_file('version', composer_file)
        try:
            composer_requires = self.json_parser.get_variable_from_file('require', composer_file)
        except Exception:
            composer_requires = dict()
        try:
            composer_suggests = self.json_parser.get_variable_from_file('suggests', composer_file)
        except Exception:
            composer_suggests = dict()

        core_module_name = core_full_module_name.split('/')[1]
        list_of_modules[core_full_module_name] = dict(
            {'module_name': core_module_name, 'full_module_name': core_full_module_name, 'version': core_version.strip('><=')}
        )

        for full_module_name, version in composer_requires.items():
            if full_module_name.find('aheadworks') != -1:
                module_name = full_module_name.split('/')[1]
                list_of_modules[full_module_name] = dict(
                    {'module_name': module_name, 'full_module_name': full_module_name, 'version': version.strip('><=')}
                )

        for full_module_name, version in composer_suggests.items():
            if full_module_name.find(core_module_name) != -1:
                module_name = full_module_name.split('/')[1]
                list_of_modules[full_module_name] = dict(
                    {'module_name': module_name, 'full_module_name': full_module_name, 'version': version.strip('><=')}
                )

        return list_of_modules
