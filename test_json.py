import json

class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender =gender

    def eat(self):
        print( f" name : {self.name}, age : {self.age}, gender : {self.gender}  我在吃 ")

    def run(self):
        print( f" name : {self.name}, age : {self.age}, gender : {self.gender}  我在跑 ")

    def drink(self):
        print( f" name : {self.name}, age : {self.age}, gender : {self.gender}  我在喝 ")

dazhang = person("dazhang","30","man")

print(dazhang.name)
dazhang.eat()
