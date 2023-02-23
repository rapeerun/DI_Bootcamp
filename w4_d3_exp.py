# # ex1
# keys = ["Ten", "Twenty", "Thirty"]
# values = ["10", "20", "30"]
# x=zip(keys,values)
# print(tuple(x))

# ex2

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# ticket_price = {}

# for name, age in family.items():
#     if age < 3:
#         ticket_price[name] = 0
#     elif age >= 3 and age <= 12:
#         ticket_price[name] = 10
#     else:
#         ticket_price[name] = 15
        
# print(ticket_price)
#  having an issue for printing total cost for the family members
# for value in ticket_price:
#    qw= sum (str(ticket_price))
#    print(qw)

# # ex3
# brand={
#  "name": "Zara",
# "creation_date":1975,
# "creator_name": "Amancio Ortega Gaona",
# "type_of_clothes": ["men", "women", "children", "home", ],

# "international_competitors":["Gap", "H&M", "Benetton"],
# "number_stores": 7000,
# "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]},

# }
# brand["number_stores"]=2
# print(f"Zara clients are {brand['type_of_clothes']}")
# brand["country_creation" ]="spain"
# if "international_competitors" in brand:
#     brand["international_competitors"].append("Desigual")

# del brand["creation date"]
# print(brand["international_competitors"][-1])
# # having an issue to continue as an error msg that I have understand why the code is not working

# # ex4
# Given list
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# Result 1
disney_users_A = {}
for i, user in enumerate(users):
    disney_users_A[user] = i
print(disney_users_A)

# Result 2
disney_users_B = {}
for i, user in enumerate(users):
    disney_users_B[i] = user
print(disney_users_B)

# Result 3
disney_users_C = dict(sorted({user: i for i, user in enumerate(users)}.items()))
print(disney_users_C)

# Filtered result 1
disney_users_A_filtered = {}
for i, user in enumerate(users):
    if 'i' in user:
        disney_users_A_filtered[user] = i
print(disney_users_A_filtered)

# Filtered result 2
disney_users_A_filtered = {}
for i, user in enumerate(users):
    if user.startswith(('m', 'p')):
        disney_users_A_filtered[user] = i
print(disney_users_A_filtered)