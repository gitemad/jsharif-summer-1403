class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def move(self):
        print('Person moved')

class Student(Person):

    def __init__(self, first_name, last_name, university):
        Person.__init__(self, first_name, last_name)

        self.university = university
    
    # override move method in Person class
    def move(self):
        print('Student moved')

class FootballPlayer(Person):

    def __init__(self, first_name, last_name, club):
        Person.__init__(self, first_name, last_name)

        self.club = club
    
    # override move method in Person class
    def move(self):
        print('Football player moved')


class FootballPlayerStudent(Student, FootballPlayer):

    def __init__(self, first_name, last_name, club, university):
        FootballPlayer.__init__(self, first_name, last_name, club)
        Student.__init__(self, first_name, last_name, university)
    


# football_player_student = FootballPlayerStudent('f_name', 'l_name', 'club', 'uni')

# print(football_player_student.university)

# football_player_student.move()


class A:

    def __init__(self) -> None:
        super().__init__()
        print('A')

class B(A):

    def __init__(self) -> None:
        super().__init__()
        print('B')

class C(A):

    def __init__(self) -> None:
        super(C, self).__init__()
        print('C')

class D(A):

    def __init__(self) -> None:
        super().__init__()
        print('D')

class E(D, C, B):

    def __init__(self) -> None:
        super(C, self).__init__()
        print('E')

# E()
# print()
# C()

football_player_student = FootballPlayerStudent('f_name', 'l_name', 'club', 'uni')

print(isinstance(football_player_student, FootballPlayerStudent))
print(isinstance(football_player_student, FootballPlayer))
print(isinstance(football_player_student, Person))
print(isinstance(football_player_student, E))

print(issubclass(FootballPlayer, Person))
print(issubclass(FootballPlayer, Student))