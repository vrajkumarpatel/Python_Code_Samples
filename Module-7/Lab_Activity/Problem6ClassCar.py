# Your Name: Vrajkumar Patel
# The Date: 2025-11-10
# Problem 6: Class Car
# Description: Differentiate between an attribute and a method in a Python class definition.
# Then modify the given car class to add two additional attributes: 'type' and 'manufacturer'.
# Also add corresponding methods and update fullspecs() to include the new attributes.






class car:
    def __init__(self, model: str, year: int, color: str, type: str, manufacturer: str):
        self.model = model
        self.year = year
        self.color = color
        self.type = type  # new attribute
        self.manufacturer = manufacturer  # new attribute

    def get_model(self) -> str:
        return self.model

    def get_year(self) -> int:
        return self.year

    def get_color(self) -> str:
        return self.color

    def get_type(self) -> str:
        return self.type

    def get_manufacturer(self) -> str:
        return self.manufacturer

    def fullspecs(self) -> str:
        # Include manufacturer and type in the full specs string
        return (
            f"{self.manufacturer} {self.model} {self.type} "
            f"{self.year} {self.color}"
        )


def main():
    car1 = car("Sports", 2012, "Blue", "Coupe", "Acme Motors")
    car2 = car("Sedan", 2020, "Black", "Family", "Contoso Auto")

    # Original prints
    print(car1.get_color())
    print(car1.get_model())
    print(car2.get_color())

    # New attribute methods
    print(car1.get_type())
    print(car1.get_manufacturer())
    print(car2.get_type())
    print(car2.get_manufacturer())

    # Updated full specifications including new attributes
    print(car1.fullspecs())
    print(car2.fullspecs())


if __name__ == "__main__":
    main()