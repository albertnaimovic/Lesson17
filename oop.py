# class Calculator:
#     def __init__(self) -> None:
#         print("Testaz")

#     def add_two_numbers(self, number_one: int, number_two: int) -> int:
#         return number_one + number_two

#     def substract_two_numbers(self, number_one: int, number_two: int) -> int:
#         return number_one - number_two

#     def divide_two_numbers(self, number_one: int, number_two: int) -> float:
#         return number_one / number_two

#     def multiply_two_numbers(self, number_one: int, number_two: int) -> int:
#         return number_one * number_two


# calc = Calculator()
# calc_2 = Calculator()


# print(calc.add_two_numbers(5, 3))
# print(calc.substract_two_numbers(5, 3))

# class People:
#     def __init__(self, name: str, surname: str) -> None:
#         self.name = name
#         self.surname = surname

#     def get_name_and_surname(self) -> str:
#         return self.name + " " + self.surname

# if __name__ == "__main__":

#     people = People(name = "Albert", surname = "Naimovic")
#     print(people.name)
#     print(people.surname)
#     print(people.get_name_and_surname())


# create a class, which represents a car.


# class Car:
#     def __init__(self, model: str, made_date: int, engine_capacity: float) -> None:
#         self.model = model
#         self.made_date = made_date
#         self.engine_capacity = engine_capacity

#     def get_car_name(self) -> str:
#         return self.model

#     def get_car_made_date(self) -> str:
#         return self.made_date

#     def get_engine_capacity(self) -> str:
#         return self.engine_capacity

#     def return_all_data(self) -> tuple:
#         return self.model, self.made_date, self.engine_capacity


# car = Car(model="Mercedes", made_date=1997, engine_capacity=2.3)

# car2 = Car(model="BMW", made_date=2023, engine_capacity=0.9)

# print(car.get_car_name())

# print(car2.get_car_name())

# print(car.return_all_data())


# UZDAVINYS 1
# Create a class which represents your family. Class should take your mom,dad,sister ,broters names and ages.
# Create instance methods that would return :
#  - All names and ages as dict data structure
#  - The sum of all ages
#  - Would print the names depending on your relatives(sister,brother etc)
#  - Would list all family members from youngest to oldest (Choose return type by yourself.)


class Family:
    def __init__(
        self,
        sister_name: str,
        brother_name: str,
        mother_name: str,
        father_name: str,
        sister_age: int,
        brother_age: int,
        mother_age: int,
        father_age: int,
    ) -> None:
        self.sister_name = sister_name
        self.brother_name = brother_name
        self.mother_name = mother_name
        self.father_name = father_name
        self.sister_age = sister_age
        self.brother_age = brother_age
        self.mother_age = mother_age
        self.father_age = father_age

    def family_data(self) -> dict:
        try:
            family_dictionary: dict = {
                self.sister_name: self.sister_age,
                self.brother_name: self.brother_age,
                self.mother_name: self.mother_age,
                self.father_name: self.father_age,
            }
            return family_dictionary
        except Exception as err:
            print(f"You got {err} error!")

    def age_sum(self) -> int:
        return self.sister_age + self.brother_age + self.mother_age + self.father_age

    def return_sister_name(self) -> str:
        return self.sister_name

    def return_brother_name(self) -> str:
        return self.brother_name

    def return_mother_name(self) -> str:
        return self.mother_name

    def return_father_name(self) -> str:
        return self.father_name

    def sorted_by_age_family_list(self) -> list:
        family_dict: dict = self.family_data()
        return sorted(family_dict)


family_info = Family(
    sister_name="Evelina",
    brother_name="Andrius",
    mother_name="Irena",
    father_name="Juozas",
    sister_age=31,
    brother_age=12,
    mother_age=55,
    father_age=54,
)

print(family_info.family_data())
print(family_info.age_sum())
print(family_info.return_sister_name())
print(family_info.return_brother_name())
print(family_info.return_mother_name())
print(family_info.return_father_name())
print(family_info.sorted_by_age_family_list())
