"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Use two values to control start and next value of generator."""

        self.start = self.next = start

    def __repr__(self):
        """This shows the current representation of the object"""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Return next value."""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Set number to beginning value"""

        self.next = self.start
        
    



