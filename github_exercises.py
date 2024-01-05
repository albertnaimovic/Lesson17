# 1. Create a Calculator class with main functionality: add, divide, multiply, subtract , etc.. Initiate class and show up some calculations.


from typing import Type, Union


class Calculator:
    def __init__(
        self, number_one: Union[int, float], number_two: Union[int, float]
    ) -> None:
        self.number_one = number_one
        self.number_two = number_two

    def add_two_numbers(self) -> Union[int, float]:
        return self.number_one + self.number_two

    def substract_two_numbers(self) -> Union[int, float]:
        return self.number_one - self.number_two

    def divide_two_numbers(self) -> Union[int, float]:
        try:
            return self.number_one / self.number_two
        except ZeroDivisionError:
            print("Divisor is zero; Division is impossible")

    def multiply_two_numbers(self) -> Union[int, float]:
        return self.number_one * self.number_two


calc = Calculator(number_one=5, number_two=3)

# print(f"Sum: {calc.add_two_numbers()}")
# print(f"Substraction: {calc.substract_two_numbers()}")
# print(f"Division: {calc.divide_two_numbers()}")
# print(f"Multiplication: {calc.multiply_two_numbers()}")


# 2.Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:
#   Form the fullname by simply joining the first and last name together, separated by a space.
#   Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.


class Employee:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.fullname = self.create_fullname()
        self.email = None

    def create_fullname(self) -> str:
        return self.name + " " + self.surname

    def create_email(self) -> str:
        self.email = (self.name + "." + self.surname + "@company.com").lower()
        return self.email


employee = Employee(name="Albert", surname="Naimovic")

# print(employee.fullname)
# employee.create_email()
# print(employee.email)


# 3. Create a Book class that has two attributes:

# title
# author
# and two methods:

# A method named .get_title() that returns: "Title: " + the instance title.
# A method named .get_author() that returns: "Author: " + the instance author.
# and instantiate this class by creating 3 new books:

# Pride and Prejudice - Jane Austen (PP)
# Hamlet - William Shakespeare (H)
# War and Peace - Leo Tolstoy (WP)
# The name of the new instances should be PP, H, and WP, respectively. For instance, if I instantiated the following book using this Book class:

# Harry Potter - J.K. Rowling (HP)


# HP.title ➞ "Harry Potter"
# HP.author ➞ "J.K. Rowling"
# HP.get_title() ➞ "Title: Harry Potter"
# HP.get_author() ➞ "Author: J.K. Rowling"


class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title: str = title
        self.author: str = author

    def get_title(self) -> str:
        return "Title: " + self.title

    def get_author(self) -> str:
        return "Author: " + self.author


PP = Book(title="Pride and Prejudice", author="Jane Austen")
H = Book(title="Hamlet", author="William Shakespeare")
WP = Book(title="War and Peace", author="Leo Tolstoy")

# print(PP.title)
# print(H.author)
# print(WP.get_title())
# print(H.get_author())


# 4. A country can be said as being big if it is:
#   Big in terms of population.
#   Big in terms of area.

# Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:
#   Population is greater than 20 million.
#   Area is larger than 3 million square km.

# Also, create a method which compares a country's population density to another country object. Return a string in the following format:
#   {country} has a {smaller / larger} population density than {other_country}

# australia = Country("Australia", 23545500, 7692024)
# andorra = Country("Andorra", 76098, 468)

# australia.is_big ➞ True
# andorra.is_big ➞ False
# andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"


class Country:
    def __init__(self, country: str, area: int, population: int) -> None:
        self.country = country
        self.area = area
        self.population = population

    def is_big(self) -> bool:
        if self.area > 20000000 or self.population > 3000000:
            return True
        else:
            return False

    def compare_pd(self, other_country: "Country") -> str:
        if self.population / self.area > other_country.population / other_country.area:
            return f"{self.country} has a bigger population density than {other_country.country}"
        else:
            return f"{self.country} has a smaller population density than {other_country.country}"


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

# print(australia.is_big())
# print(andorra.is_big())
# print(andorra.compare_pd(australia))
# print(australia.compare_pd(andorra))


# Create a Python class named Fraudster with the following attributes:
# email_domain: A string representing the email domain associated with fraudulent activities (e.g., "@gmail.com").
# amount: An integer representing the total amount fraudulently approved.
# number_of_users: An integer representing the number of users associated with the specified email domain.
# Implement two methods within the class:
# fraud_amount_by_domain(): This method should return a string indicating the amount that was fraudulently received with the specified email domain.
# users_by_domain(): This method should return a string indicating the number of users using the specified email domain.
# initiate three classes:
# Spain_fraud -> email_domain="@gmail.com", amount=100000, number_of_users=5
# French_fraud -> email_domain="@yahoo.com", amount=453295, number_of_users=19
# Latin_america_fraud = "@yandex.ru", amount=1036594, number_of_users=2

# implement methods created in the class to return various information about these fraud rings


class Fraudster:
    def __init__(self, email_domain: str, amount: int, number_of_users: int) -> None:
        self.email_domain = email_domain
        self.amount = amount
        self.number_of_users = number_of_users

    def fraud_amount_by_domain(self) -> str:
        return f"From {self.email_domain} we received {self.amount} fraud emails."

    def users_by_domain(self) -> str:
        return f"The {self.number_of_users} of users using {self.email_domain}"


spain_fraud = Fraudster(email_domain="@gmail.com", amount=100000, number_of_users=5)
french_fraud = Fraudster(email_domain="@yahoo.com", amount=453295, number_of_users=19)
latin_america_fraud = Fraudster(
    email_domain="@yandex.ru", amount=1036594, number_of_users=2
)

# print(spain_fraud.fraud_amount_by_domain())
# print(latin_america_fraud.users_by_domain())


# Create a program that user enters name, surname, email_provider, age (example: Thom, Nelson, gmail, 12 )
# Program should list options to choose:
#  - Generate some email variants from all data provided
#  - Get year of birth
#  - Return all personal info (including generic email and year of birth)


# Must use class for dealing with data. Error handling, types. Input should be invoked as a script (if __name__ ....)


class Person:
    CURRENT_YEAR: int = 2023

    def __init__(self, name: str, surname: str, email_provider: str, age: int) -> None:
        self.name = name
        self.surname = surname
        self.email_provider = email_provider
        self.age = age

    def email_generator(self) -> str:
        return f"Some email variants for you:\n{self.name.lower()}.{self.surname.lower()}@{self.email_provider.lower()}\n{self.surname.lower()}.{self.age}.{self.name.lower()}@{self.email_provider.lower()}"

    def get_year_of_birth(self) -> int:
        return self.CURRENT_YEAR - self.age

    def get_personal_info(self) -> str:
        return f"Name: {self.name}\nSurname: {self.surname}\nEmail: {self.name.lower()}.{self.surname.lower()}@{self.email_provider.lower()}\nAge: {self.age}"


def main_menu(person_info: str) -> None:
    person_info_list = person_info.replace(" ", "").split(",")
    name = person_info_list[0]
    surname = person_info_list[1]
    email_provider = person_info_list[2]
    age = int(person_info_list[3])

    person = Person(
        name=name,
        surname=surname,
        email_provider=email_provider,
        age=age,
    )
    menu_entries: str = "\n1. Generate some email variants\n2. Get year of birth\n3. Return all personal info\n4. End program.\nPlease enter number of your selection: "

    while True:
        menu_select: str = input(menu_entries)
        print()

        if menu_select.isnumeric() == True:
            if menu_select == "1":
                print(person.email_generator())
            elif menu_select == "2":
                print(person.get_year_of_birth())
            elif menu_select == "3":
                print(person.get_personal_info())
            elif menu_select == "4":
                print("Bye")
                break
            else:
                print("There is no such selection.")
        else:
            print(
                "Please enter number from list provided without any symbols and spaces."
            )


if __name__ == "__main__":
    person_info: str = input(
        "Enter name, surname, email_provider, age (example: Thom, Nelson, gmail.com, 12 ): "
    )

    try:
        main_menu(person_info)
    except Exception as err:
        print(f"You've got an {err} error.")
