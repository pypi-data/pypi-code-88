from typing import Iterable, Any, Callable

import pmakeup as pm


class CachePMakeupPlugin(pm.AbstractPmakeupPlugin):

    def _setup_plugin(self):
        pass

    def _teardown_plugin(self):
        pass

    def _get_dependencies(self) -> Iterable[type]:
        return []

    @pm.register_command.add("cache")
    def clear_cache(self):
        """
        Clear the cache of pmakeup
        """
        self._model.pmake_cache.reset()

    @pm.register_command.add("cache")
    def set_variable_in_cache(self, name: str, value: Any, overwrite_if_exists: bool = True):
        """
        Set a variable inside the program cache. Setting variable in cache allows pmakeup to
        store information between several runs of pmakeup.

        How pmakeup stores the information is implementation dependent and it should not be relied upon

        :param name: name of the variable to store
        :param value: object to store
        :param overwrite_if_exists: if true, if the cache already contain a variable with the same name, such a varaible will be replaced
            with the new one
        """
        self._log_command(f"Setting {name}={value} in cache")
        self._model.pmake_cache.set_variable_in_cache(
            name=name,
            value=value,
            overwrites_is_exists=overwrite_if_exists
        )

    @pm.register_command.add("cache")
    def has_variable_in_cache(self, name: str) -> bool:
        """
        Check if a variable is in the pmakeup cache

        :param name: name of the variable to check
        :return: true if a varaible with such a name is present in the cache, false otherwise
        """
        result = self._model.pmake_cache.has_variable_in_cache(
            name=name
        )
        self._log_command(
            f"Checking if \"{name}\" is present in the pamkeup cache. It is {'present' if result else 'absent'}")
        return result

    @pm.register_command.add("cache")
    def get_variable_in_cache(self, name: str) -> Any:
        """
        Get the variable from the cache. if the variable does not exist, an error is generated

        :param name: name of the variable to check
        :return: the value associated to such a variable
        """
        return self._model.pmake_cache.get_variable_in_cache(
            name=name
        )

    @pm.register_command.add("cache")
    def get_variable_in_cache_or_fail(self, name: str) -> Any:
        """
        Get the variable value from the cache or raise an error if it does not exist

        :param name: name of the variable to fetch
        :return: the variable value
        """
        if self._model.pmake_cache.has_variable_in_cache(name):
            return self._model.pmake_cache.get_variable_in_cache(name)
        else:
            raise ValueError(f"Cannot find variable \"{name}\" in pmakeup cache!")

    @pm.register_command.add("cache")
    def get_variable_in_cache_or(self, name: str, default: Any) -> Any:
        """
        Get the variable value from the cache or get a default value if it does not exist

        :param name: name of the variable to fetch
        :param default: if the variable does not exist in the cache, the value to retturn from this function
        :return: the variable value
        """
        if self._model.pmake_cache.has_variable_in_cache(name):
            return self._model.pmake_cache.get_variable_in_cache(name)
        else:
            return default

    @pm.register_command.add("cache")
    def get_variable_in_cache_or_set_it(self, name: str, default: Callable[[], Any]) -> Any:
        """
        Get the variable value from the cache. In case the cache does not contains such a value, we will execute the
        function passed in default and populates the "naem" cache variable with its return value

        :param name: name of the variable to fetch
        :param default: if the variable does not exist in the cache, the function output use to set the enw variable "name"
        :return: the variable value
        """
        if self._model.pmake_cache.has_variable_in_cache(name):
            return self._model.pmake_cache.get_variable_in_cache(name)
        else:
            value = default()
            self._model.pmake_cache.set_variable_in_cache(name)
            return value


    @pm.register_command.add("cache")
    def add_or_update_variable_in_cache(self, name: str, supplier: Callable[[], Any], mapper: Callable[[Any], Any]):
        """
        Add a new variable in the cache

        :param name: the variable to set
        :param supplier: function used to generate the value fo the variable if the variable does not exist in the cache
        :param mapper: function used to generate the value fo the variable if the variable does exist in the cache. The input
            is the variable old value
        """
        if self._model.pmake_cache.has_variable_in_cache(name):
            new_value = mapper(self._model.pmake_cache.get_variable_in_cache(name))
        else:
            new_value = supplier()
        self._log_command(f"Setting {name}={new_value} in cache")
        self._model.pmake_cache.set_variable_in_cache(name, new_value)

    @pm.register_command.add("cache")
    def load_cache(self):
        """
        Load all the variables present in cache into the available variables
        """

        self._log_command(f"Loading variables in cache...")
        i = 0
        for key in self._model.pmake_cache.variable_names():
            self.set_variable(key, self._model.pmake_cache.get_variable_in_cache(key))
            i += 1
        self._log_command(f"Loaded {i} variables")