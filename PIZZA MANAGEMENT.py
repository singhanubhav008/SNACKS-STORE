menu ={
    'PIZZA': 40,
    'BURGER': 50,
    'COFFEE LATEE': 60,
    'CHIKEN PATIS':35
}
print("HERE IS OUR MENU SIR :)")
print('')
print("PIZZA: 40,\nBURGER: 50,\nCOFFEE LATEE: 60,\nCHICKEN PATIS:35")
order1 = input("SIR CAN I HAVE YOUR ORDER PLEASE!: ")

order2 = input("ANYTHING ELSE SIR?: ")
if order1 and order2 != menu:
    print("Not Available Sorry :)")

elif order1 != "COFFEE LATEE" and order2 == "NO":
     bill = print("the total bill is : ",menu[order1])
elif  order1 == "NO" and order2 == "NO":
      print("THANK YOU VISIT AGAIN :)")
else :
     print("THE TOTAL BILL IS : ",menu[order1] + menu[order2])





