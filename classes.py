class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        return "Hello, my name is " + self.name + " and I'm " + str(self.age) + " years old."


def main():
    p1 = Person("Ein-Bar", 26)
    print(p1.name)
    print(p1.age)
    print(p1.hello())


if __name__ == "__main__":
   main()

    