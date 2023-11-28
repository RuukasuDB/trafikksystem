class Pass(object):
    """A datastructure for storing a pass

    Longer class information....
    Longer class information....

    Attributes:
        date (str): The date of the pass.
        time (str): The time of the pass.
        registration_number (str): The registration number associated with the pass.

    Methods:
        None
    """
    def __init__(self, date: str, time: str, registration_number: str):
        """Initializes a Pass object with the given attributes.

        Args:
            date (str): The date of the pass.
            time (str): The time of the pass.
            registration_number (str): The registration number associated with the pass.
        """
        self.date = date
        self.time = time
        self.registration_number = registration_number