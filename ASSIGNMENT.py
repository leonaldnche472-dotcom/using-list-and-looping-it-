#naming the sandwich list
sandwich_orders=['tuna','rice','fish','egg']

#naming the completed orders
completed_orders=[]
for sandwich in sandwich_orders:
    print("i made your",sandwich,"sandwich")
    completed_orders.append(sandwich)


#while sandwich_orders:
#   sandwich=sandwich_orders[0] 
#   print("i made your",sandwich,"sandwich")
#   completed_orders.append(sandwich)

print("\nsandwiches made and ready;")
for sandwich in completed_orders:
    print(sandwich)

#uploading the list with pastrami appearing many times
sandwich_orders=['pastrami','tuna','pastrami','rice','pastrami','egg']
completed_orders=[]

#removing all pastrami sandwitches
print("sorry,we are out of pastrami today")
while'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#makeing  the remaining sandwiches
for sandwich in sandwich_orders:
    print('i made your',sandwich,'sandwich')
    completed_orders.append(sandwich)
print("\n your sandwiches have been made ")
for sandwich in completed_orders:
    print(sandwich)