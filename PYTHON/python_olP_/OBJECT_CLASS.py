class Monster:
    #class attribute
    color = "black"
    def __init__(self, age, name):
        #instant attributed
        self.age = age
        self.name = name

        self._is_innocent = None
    #instaent Method
    def steal(self, warrior):
        warrior.lose_stick()
    #creating an instent
monster1 = Monster(15,"mon1")
print(monster1.age)
monster1.age=10
#creating another instent
monster2=Monster(10,"mon2")

    #construcors
def __init__(self, age, name):
    #instent attribute
    self.age = age
    self.name = name
    self._number_of_stickes = 0
    #construcors
def __init__(self, age, name="mon1"):
    #instent attribute
    self.age = age
    self.name = name
    self._number_of_stickes = 0
    #construcors
def __init__(self):
    #instent attribute
    self.age = 10
    self.name = "mon1"
    self._number_of_stickes = 0

#method
#instence mothod in monster class
def change_warrior_age(self, warrior):
    new_age = 5
    warrior.age = new_age
    print(new_age)

#instence method in monster  class
def steal(self, warrior):
    warrior.lose_stick()
    self._number_of_sticks += 1



car_count = 0
def calculate_car_count():
class car:
    manufactur="temp"
    def __init__(self, chassi_number):
        self.chassi_number = chassi_number
        self.model = "temp"
    def run(self):
        