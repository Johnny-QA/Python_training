lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer('Rolf')
player_one.numbers = (1, 2, 3, 6, 7, 8)
player_two = LotteryPlayer('John')
# print(player_two.total())
# print(player_one.numbers == player_two.numbers)

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

anna = Student('Anna', 'MIT')
anna.marks.append(18)
anna.marks.append(10)
anna.marks.append(33)
anna.marks.append(51)
print(anna.name, anna.school, anna.marks, anna.average())