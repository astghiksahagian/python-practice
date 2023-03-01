#Shant's example:
# class Person(object):

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def printDetails(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

#     def happyBirthday(self):
#         self.age += 1
#         print("Happy Birthday!")
    

# person = Person("Ast", 25)
# person.printDetails()
# person.happyBirthday()
# person.printDetails()


class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy Birthday to you", "I don't want to get sued, So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


class Song2(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def print_song(self):
        for line in self.lyrics:
            print(line)

lyrics = ["You are my sunshine", "My only sunshine", "You make me happy when the skies are grey"]

sunshineSong = Song2(lyrics)

sunshineSong.print_song()

