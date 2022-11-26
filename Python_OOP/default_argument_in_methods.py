class Bonus:

    def __init__(self, name):
        self.salary = 1800
        self.name = name

    def bonus_cal(self, bonus = 2):
        bonus_percentage = (bonus * self.salary) /  100
        print(f"{self.name} gets {bonus} % of bonus on his {self.salary} which is {bonus_percentage}")


bonus_one = Bonus("Johnathan")
bonus_one.bonus_cal()