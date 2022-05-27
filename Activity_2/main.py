


class ClubMembers:
    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def dispalay1(self):
        print("Name: ", self.name)
        print("Birthday :", self.birthday)
        print("Age :", self.age)
        print("Favorite food :", self.favorite_food)
        print("Goal :", self.goal)

class ClubOfficer(ClubMembers):
    def __init__(self, name, birthday, age, favorite_food, goal, position):
        self.position = position
        ClubMembers.__init__(self, name, birthday, age, favorite_food, goal)

    def dispalay2(self):
        print("Name: ", self.name)
        print("Birthday :", self.birthday)
        print("Age :", self.age)
        print("Favorite food :", self.favorite_food)
        print("Goal :", self.goal)
        print("Position :", self.position)


m_1 = ClubMembers("Tom", "January 16", 14, "Ice cream", "To be happy")
o_4 = ClubOfficer("Vera","June 22", 16, "Beef stroganoff", "To be the worls's greatest chief", "Treasurer")

m_1.dispalay1()
o_4.dispalay2()

