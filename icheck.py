import abc


class ICheck(metaclass=abc.ABCMeta):
    """Interface for checking the validity of a given value."""

    @abc.abstractmethod
    def identifier(self):
        """Returns a unique identifier for the check."""
        raise NotImplementedError("ICheck.identifier()")


    @abc.abstractmethod
    def name(self):
        """Returns the name of the check."""
        raise NotImplementedError("ICheck.name()")

    def description(self):
        """Returns a description of the check."""
        return "No description available."


