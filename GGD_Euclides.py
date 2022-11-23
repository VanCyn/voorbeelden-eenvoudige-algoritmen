getal_1 = int(input("Geef een eerste getal in: "))
getal_2 = int(input("Geef een tweede getal in:"))
x,y = getal_1,getal_2
while x!=y:
    if x>y:
        x=x-y
    else:
        y=y-x
print("De grootste gemene deler van {} en {} ={}".format(getal_1,getal_2,x))