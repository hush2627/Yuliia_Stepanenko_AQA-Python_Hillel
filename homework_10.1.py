class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = departament


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        self.name = name
        self.salary = salary
        self.programming_language = programming_language


class TeamLead(Manager, Developer)
    def __init__(self, name, salary, department, programming_language, team_size):
        self.name = name
        self.salary = salary
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size


lead = TeamLead("Anna", 5000, "Backend", "Python", 4)

print(hasattr(lead department))
print(hasattr(lead, "programming_language"))
```

**Задание 2 (с ошибками):**

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side)
        self.__side = side

    def get_area(self):
        return self.__side + self.__side

    def get_perimeter(self):
        return self.__side * 4


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return (self.__width + self.__height) * 2


shapes = [Square(3), Rectangle(4, 6)]

for shape in shapes
    print(shape.get_area())
    print(shape.get_perimeter())
```