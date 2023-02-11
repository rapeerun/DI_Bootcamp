# # ex1 set
# my_fav_numbers={1,28,77,85,45,88,888,888888}
# my_fav_numbers.update([3],[18])
# my_fav_numbers.pop()
# print(my_fav_numbers)

# friend_fav_numbers={"raees","saajid","kqwmkq"}

# print(friend_fav_numbers)

# az=my_fav_numbers.union(friend_fav_numbers)
# print(az)

# # ex2 
# # Given a tuple which value is integers, is it possible to add more integers to the tuple?
# # Answer: In py once they are created we can't add or remove element from the tuple. The only way to add integer is to create a new tuple.

# # ex3

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# # print(basket)
# basket.remove("Blueberries")
# # print(basket)
# basket.insert(3,"Kiwi")
# # print(basket)
# basket.insert(0,"Apples")
# # print(basket)
# aq=basket.count("Apples")
# # print(aq)
# basket.clear()
# print(basket)


# # ex4
# # floats are numbers which contain decimal places. The difference between a float and a integer is that an integer takes whole value whereas a float contain whole value and decimals.

# current_num=1.5
# while current_num <=5:
#     print(current_num)
#     current_num+=0.5

# # ex5
# num_rt=range(1,21)
# for number in num_rt:
      
#     print(number)

# # second part

# for fg_1 in range(1,21):
#     if fg_1 % 2 == 0:
#         print(fg_1)


# # ex6

# username= ""
# while username != "Raees":
#     username= input("Enter your username:").capitalize()
# print("This is the end")


# #  ex7
# favorite_fruit=(input("Enter your favorite fruits:"))
# favorite_fruits_to_list=favorite_fruit.split()
# user_input=(input("Enter a fruit:"))

# if user_input in favorite_fruit:
#     print("You chose one of your favorite fruits! Enjoy")
# else: print("You chose a new fruit.I hope u enjoy")

# ex9
# input_age=int(input("Enter family age"))
# if input_age < int(3):
#     print("$0")
# elif input_age < int(12):
#   else:
# print("$15")










# # ex10
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# finished_sandwish=[]
# while sandwich_orders:
#     finished_sandwish=sandwich_orders.pop(0)

#     print(f"I made your {finished_sandwish}")
#     sandwich_orders.append(finished_sandwish)
# else:
#  print("finish")

# # ex11

# sandwich_orders = [
#     "Tuna sandwich",
#     "Avocado sandwich",
#     "Pastrami sandwich",
#     "Egg sandwich",
#     "Sabih sandwich",
#     "Pastrami sandwich",
#     "Pastrami sandwich",
# ]
# finished_sandwiches = []

# print("We ran out of Pastrami!")
# while "Pastrami sandwich" in sandwich_orders:
#     sandwich_orders.remove("Pastrami sandwich")

# while sandwich_orders:
#     current_order = sandwich_orders.pop()
#     print(f"I made your {current_order}")
#     finished_sandwiches.append(current_order)



 

















