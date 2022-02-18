from FileTreatMentException import FileTreatMentException

class Entry:

    def get_name(self):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

    def add(self, entry):
        raise FileTreatMentException

    def print_list(self, prefix=""):
        raise NotImplementedError

    def __str__(self):
        return f"{self.get_name()} ({self.get_size()})"

    # def __repr__(self):
    #     return f"{self.get_name()} ({self.get_size})"
