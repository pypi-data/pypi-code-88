from abc import abstractmethod


class CfnResourceMapper:  # todo - each aws resource should implement it

    @abstractmethod
    def get_attribute(self, cfn_attribute_name: str):
        pass
