# challenge 1
# user_1=input("enter a word:")

# dic_letter={
    
# }


# for i, items in enumerate(user_1):
#     tr_05=str(items)
#     if tr_05 not in dic_letter.keys():
#         dic_letter[tr_05]=[i]
#     else:  
#         dic_letter[tr_05]+=[i]

   
# print(dic_letter)

#  challenge 2

by_purchase1 = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}
items_pur=(list)
wallet_1 = "$300"
print(by_purchase1.items())
for key,value in  by_purchase1.items():
    print(key,value)
    sanitized_value = value.replace("$", "")
    sanitized_value = sanitized_value.replace(",", "")
    print(sanitized_value)
    # print(key.replace["TV"](',',''))
    # wallet_1sanitized_value =sanitized_value.replace("$", "")
    sanitized_wallet=wallet_1.replace("$","")
    print(sanitized_wallet)
    for x_01 in by_purchase1.items_pur():
        if sanitized_wallet>=sanitized_value:
            items_pur.append(x_01)
            if items_pur:
                 sorted(items_pur)
            else: print ("You can't afford anything")
    print(items_pur)
    # else:
    #     print("you can't afford anything from the store")


    






# loop through items_purchase1 and obtain key and value
#     Remove $ and , from values
#     Convert remaining value string to an int
#     Compare int(wallet) >= value
#         if True:
#             add key to list


 

# items_purchase2 = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }

# wallet = "$100" 

 

# items_purchase3 = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }

# wallet = "$1"



