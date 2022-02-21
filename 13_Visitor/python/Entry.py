from Element import Element
from FileTreatMentException import FileTreatMentException


class Entry(Element):

    def get_name(self):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

    def add(self, entry):
        raise FileTreatMentException

    def __str__(self):
        return f"{self.get_name()} ({self.get_size()})"