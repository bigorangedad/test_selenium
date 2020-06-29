"""
创建一个Person 类
    属性：姓名，性别，年龄，存款金额
    方法：吃，睡，跑，赚钱
创建 FunnyMan类（ 喜剧 演员 ）
    继承父类Person的所有属性和方法
    新增一个方法， fun()搞笑
创建 SingerMan类 (歌手演员）
    继承父类Person的所有属性和方法，
    覆写方法，赚钱，传参(monkey)

"""


class Person:
    """
    :str  :int 表示指定他的类型，帮助ide识别字符类型，不起到验证作用
    """
    name: str = "default"
    gental: str = "default"
    age: int = 20
    __money: float = 1000

    def __init__(self, name, gental, age, money):
        self.name = name
        self.gental = gental
        self.age = age
        self.__money = money
        """
        变量名前+ __ 私有化一个属性或一个方法
        """

    # def set_name(self, name):
    #     self.name = name
    def get_money(self):
        return self.__money
        """
        :return一个私有属性后，可以被父类访问
        """
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def run(self):
        print(f"{self.name}is running")

    def make_money(self):
        print(f"{self.name} could make money")


class FunnyMan(Person):
    def fun(self):
        print(f"{self.name} is funny")

class SingerMan(Person):
    def make_money(self, moneynum:str=150000):
        print(f"{self.name} could make money {moneynum}")
        return 2

p = Person("jacky", "man", "28", "20000")
# print(p.name, p.age)
# print(p.eat())
# print(p.name, "is", p.eat())
p.eat()
p.make_money()

FunnyMan = FunnyMan("Karry", "women", 25, 15000)
print(FunnyMan.name)
FunnyMan.eat()
FunnyMan.fun()
print(p._Person__money)
print(dir(p))
"""
dir(p) 打印一个实例可以调用的方法和属性
"""

singer = SingerMan("hanhong", "women", 30, 25000)

print(singer.make_money())