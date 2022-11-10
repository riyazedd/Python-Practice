print("Travel Destinations:\n1.Swoyambhu\n2.Balaju\n3.Chabahil\n4.Koteshwor\n5.Satdobato\n6.Balkhu\n7.Kalanki")
location=int(input("Choose your destination: "))
std=int(input("Are you student?\n1.Yes\n2.No\nChoose Your Option:"))

if location==1:
    print("Your fare is Rs 10.")
elif location==2:
    if std==1:
        print("Your fare is Rs.",20-10/100*20)
    else:
        print("Your fare is Rs.20")
elif location==3:
    if std==1:
        print("Your fare is Rs.",30-10/100*30)
    else:
        print("Your fare is Rs.30")
else:
    print("Your option is  not available.")