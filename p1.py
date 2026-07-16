class Student:
    def __init__(self, name, age):
        self.name = name      # Attribute
        self.age = age        # Attribute

    def introduce(self):      # Method
        print(f"My name is {self.name} and I am {self.age} years old.")

# Object creation
student1 = Student("Alice", 20)

# Access attributes
print(student1.name)

# Call method
student1.introduce()
