from abc import abstractmethod, ABC


#abstract classes, static methods (annotations)
class YamlParseable(ABC):

    @staticmethod
    @abstractmethod
    def from_dict_entry(data: dict):
        pass
