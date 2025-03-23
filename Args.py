#*args
def product_details(Component, *usage):
    print(f"Component: {Component}")
    print(f"power: {', '.join(usage)}")

product_details("Resistor", "powerController")

#Kwargs
def student_details(name, **kwargs):
    print(f"Student Name: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_details("Guna", age=25, grade="O", subject="Science")
