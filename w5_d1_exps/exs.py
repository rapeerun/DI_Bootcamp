# # # ex1

# # class Cat:
# #     def __init__(self, cat_name, cat_age):
# #         self.name = cat_name
# #         self.age = cat_age

# # cat_personality1=Cat("Greyfield",8)
# # print(cat_personality1.name)
# # print(cat_personality1.age)

# # cat_personality2=Cat("Remy",12)
# # print(cat_personality2.name)
# # print(cat_personality2.age)

# # cat_personality3=Cat("Marie",3)
# # print(cat_personality3.name)
# # print(cat_personality3.age)

# # def _finds_oldest_cat(**cat_personality):
# #     oldest_cat=None
# #     for cat in cat_personality:
# #         if oldest_cat is None or cat_personality.age > oldest_cat.age:
# #             oldest_cat=cat
# #             return oldest_cat

# #     oldest_cat =_finds_oldest_cat(cat_personality1,cat_personality2,cat_personality3)

# #     print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


# # # ex2
# class Dog():
#    def __init__(self,name,height):
#     self.name=name
#     self.height=height
    

#    def _bark(self):
#     print(f"{self.name} goes woof! ")

#    def _jump(self):
#     print(f"{self.name} jumps {self.height*2} cm high!")

# david_dog=Dog("Rex",50)
# print(david_dog.name)
# print(david_dog.height)
# david_dog._bark()
# david_dog._jump()
# sarah_dog=Dog("Teacup",20)
# print(sarah_dog.name)
# print(sarah_dog.height)
# sarah_dog._bark()
# sarah_dog._jump()

# #  if statement
# if david_dog.height >sarah_dog.height:
#     print(david_dog.name)

# else: print(sarah_dog.name)
 
#  ex3
# class Song():
#     def __init__(self,name,lyrics):
#         self.name=name
#         self.lyrics=lyrics
#         # creating a list
    
#     def sing_me_a_song(self):
#         for lyric in self.lyrics:
#             print(lyric)

#     # def sing_me_a_song(self):
#     #     for line in self.lyrics:
#     #         print(line)

# class Songs():
#      def __init__(self,name,lyrics):
#         self.name=name
#         self.lyrics=lyrics

   

# # appending list

# list=['David_Guetta','Just_one_last_time','Matin_Garix','Animals','The_Weekend','I_feel_it_coming']

# #  having an issue with 3 part of the question for displaying information in different line.

# stairway =(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song() 


# syle=Song('mysong',list)
# syle.sing_me_a_song()

# ex4

class Zoo():
    def __init__(self,zoo_name):
        self.zoo_name=zoo_name
        self.animal=[]

    def add_animal(self,new_animal):
        
        
        self.animal.append(new_animal)
            


    def get_animals(self):
        print(self.animal)


    def sell_animal(self,animal_sold):
        
        self.animal.remove(animal_sold)

    def sort_animal(self):
        self.animal=sorted(self.animal)

    # def get_groups(animal_groups):
    #     for group, animals in animal_groups.items():
    #         print(f"Group {group}: {', '.join(animals)}")
    #         animal_groups = { 
    # 1: "Ape",
    # 2: ["Baboon", "Bear"],
    # 3: ['Cat', 'Cougar'],
    # 4: ['Eel', 'Emu']
    

#  having an issue with part  7 and 8


             

my_zoo = Zoo("My Zoo") 
my_zoo.add_animal("lion")
my_zoo.add_animal("tiger")
my_zoo.add_animal("A")
my_zoo.add_animal("Q")
my_zoo.get_animals()
my_zoo.sell_animal("lion")
my_zoo.get_animals() 
my_zoo.sort_animal()
my_zoo.get_animals()
# my_zoo.get_groups()




    








        


























