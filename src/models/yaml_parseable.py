from abc import abstractmethod, ABC


#abstract classes, static methods (annotations)
class Parseable(ABC):

    @staticmethod
    @abstractmethod
    def to_object(data: dict, **kwargs):
        pass
