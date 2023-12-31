# Object-Oriented Programming (OOP)
Object-Oriented Programming (OOP) is a programming paradigm that organizes and models real-world entities as objects. For example, you can represent people as objects of the class 'Person.' 

In OOP, objects are instances of classes, which serve as blueprints for creating these objects. Consider the class 'Person' as a blueprint for creating individual human objects, each with its unique characteristics, such as 'name' and 'age.'

## Classes

In OOP, a class is a blueprint or template for creating objects. It defines the properties (attributes) and behaviors (methods) that objects of that class will have. A class is a user-defined data type that serves as a foundation for creating objects with shared characteristics.

### Syntax for Defining a Class

```python
class ClassName:
    # Class attributes (variables)
    
    def __init__(self, parameters):
        # Constructor method
        # Initialize object attributes

    def some_method(self):
        # Define methods (functions) that operate on class attributes
```

- ClassName: The name of the class, which follows Python's naming conventions (usually capitalized).
- Class attributes: Variables that define the class's data or state.
- init: The constructor method, which is a special method used to initialize object attributes. It is called when an object is created.
- self: A reference to the object itself, and it must be the first parameter in all instance methods.
- Parameters: Values that can be passed to the constructor method to set initial values for object attributes.
- Methods: Functions that define the behaviors or actions associated with the class.

Example of a class structure below
```Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}, and I am {self.age} years old."
```

In this example, the Person class defines attributes (name and age) and methods (greet). Objects of the Person class, such as person1, encapsulate data and behavior. The constructor method (__init__) is used to initialize object attributes.

Classes are fundamental to OOP as they provide a structure for modeling real-world entities, enabling code organization, reuse, and encapsulation. They serve as a blueprint for creating objects, each with its own unique state and behavior, making OOP a powerful paradigm for software development.

## Objects
An object is an instance of a class. It represents a specific, tangible item or concept based on the class's blueprint. Objects encapsulate both data (attributes) and behavior (methods). Multiple objects of the same class can coexist, each with its unique state.

Syntax for Creating an Object:
```Python
# Create an instance of the class
object_name = ClassName()
```
Here, object_name is the variable representing the object, and ClassName is the name of the class from which the object is created. This process is known as instantiation.

Using our earlier example with the Person class, let's create an instance of an object.
```Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}, and I am {self.age} years old."

# Creating an object of the Person class
person1 = Person("Alice", 30)
print(person1.name, person1.age)    # Accessing attribute
```

In this Python code, we've defined a class called Person with a constructor method (__init__) that initializes the name and age attributes. We then create an instance of the Person class named person1 with the name "Alice" and age 30. When we use print(person1.name, person1.age), we're accessing and printing the values of the name and age attributes of the person1 object, which results in "Alice 30" being printed to the console.

```bash
Alice 30
```

Objects are used to interact with your program by invoking methods and accessing attributes. Each object maintains its own state, allowing you to work with multiple instances of the same class, each with distinct data.

## Methods
Methods are functions defined within a class that perform specific actions or provide behaviors associated with the class. They operate on the attributes of the class and can be called on objects of that class.

```Python
class ClassName:
    def method_name(self, parameters):
        # Method implementation
```

- ClassName: The name of the class where the method is defined.
- method_name: The name of the method.
- self: A special parameter that refers to the object itself and is passed as the first argument to every method within the class.
- parameters: Optional parameters that the method can accept to perform its task.
- Method implementation: The code inside the method that specifies what actions it should take.

Using our Person class, let's call the method.
```Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}, and I am {self.age} years old."

# Creating an object of the Person class
person1 = Person("Alice", 30)

# Accessing attributes and calling methods
print(person1.greet()) # Calling a method
```
The greet method is defined within the Person class, and when we call it on an instance of the class, it generates and returns a greeting string that includes the name and age attributes of that instance. In this case, it uses the name "Alice" and the age 30 from the person1 object to generate the greeting:

```bash
Hello, my name is Alice, and I am 30 years old.
```

Methods play a central role in defining the behavior of objects. They enable you to interact with and manipulate the object's attributes and properties, making objects dynamic and functional entities.

## The Four Pillars of OOP
Object-Oriented Programming is based on four fundamental principles, often referred to as the "Four Pillars of OOP." These principles are:

### Encapsulation
Encapsulation is the concept of bundling data (attributes) and methods (functions) that operate on that data into a single unit (a class). It helps protect the internal state of an object by controlling access to its attributes.

```Python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        if new_age > 0:
            self.age = new_age

# Creating an object
student1 = Student("Alice", 20)

# Accessing attributes and methods
print(student1.name)        # Accessing attribute
print(student1.get_age())   # Accessing age using a method
student1.set_age(21)       # Modifying age using a method
```

In the above example, the Student class encapsulates data (name and age) and provides methods (get_age and set_age) to control access to the age attribute. Encapsulation ensures that the age attribute is not directly modified inappropriately.

### Inheritance
Inheritance allows a new class (subclass or derived class) to inherit properties and behaviors from an existing class (superclass or base class). It promotes code reusability and hierarchy in class structures.

```Python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating objects
dog = Dog()
cat = Cat()

# Calling the speak method
print(dog.speak())  # Output: "Woof!"
print(cat.speak())  # Output: "Meow!"
```

In this example, both the Dog and Cat classes inherit the speak method from the base class Animal. This demonstrates code reuse through inheritance.

3. Polymorphism
Polymorphism enables objects of different classes to be treated as objects of a common base class. It allows for flexibility and dynamic behavior based on the actual class of an object. Polymorphism can be achieved through method overriding and method overloading.

```Python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Parrot(Animal):
    def speak(self):
        return "Squawk!"

# Creating a list of animals
animals = [Dog(), Cat(), Parrot()]

# Polymorphic behavior: Calling the speak method on different animals
for animal in animals:
    print(animal.speak())

```

In this example, we have a hierarchy of animal classes with a speak method. We create a list of different animals (instances of Dog, Cat, and Parrot classes), and then we use polymorphism to call the speak method on each animal. This demonstrates that objects of different classes can be treated as objects of a common base class, and their behavior is determined by their specific class, showcasing polymorphism.

5. Abstraction
Abstraction simplifies complex systems by highlighting only the relevant details and hiding unnecessary complexities. It provides a high-level view of an object or class and focuses on what an object does rather than how it does it.

```Python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")

# Creating objects
car = Car()
bike = Bike()

# Using abstraction to start and stop vehicles
car.start()
car.stop()
bike.start()
bike.stop()
```

These four pillars of OOP help create efficient, modular, and maintainable code, making OOP a powerful paradigm for software development.
