"""

写一个Bicycle（自行车）类，有run（骑行）方法，调用时显示骑行里程km（骑行里程为传入的数字）

再写一个电动自行车类EBicycle集成Bicycle，添加电池电量battery_level 属性通过参数传入，同时有两个方法：
1.fill_charge(vol)用来充电，vol为电量
2.run（km）方法用于骑行，每骑行10km消耗电量1度，当电量耗尽时调用Bicycle的run方法骑行，

通过传入的骑行里程数，显示骑行结果（就是当电量耗尽，需要你真正骑的里程数）

"""

class Bicycle:
    def run(self, km):
        print(f"骑行了{km}km")

class EBicycle(Bicycle):
    def __init__(self, battery_level):
        battery_level:str = battery_level

    def fill_charge(self, vol):
        print(f"充电:{vol}")

    def run(self, km):
        pass

