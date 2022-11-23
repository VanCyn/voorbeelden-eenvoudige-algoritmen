getal_1 = int(input("Geef een eerste getal in: "))
getal_2 = int(input("Geef een tweede getal in: "))
x,y = getal_1,getal_2
while y!=0:
    x,y=y,x%y
print("De grootste gemene deler van {} en {} = {}".format(getal_1,getal_2,x))