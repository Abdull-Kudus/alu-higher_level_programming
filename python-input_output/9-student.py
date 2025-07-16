
#!/usr/bin/python3
"""
This program is to define a Student in a class
"""


class Student():
    """
    Class of a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Constructor of a student
        Args:
          - first_name: str
          - last_name: str
          - age: int
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dict representation of an instance
        """
        return (self.__dict__)
