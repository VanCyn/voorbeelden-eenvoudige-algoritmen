getal_1 = int(input("Geef een eerste getal in: "))
getal_2 = int(input("Geef een tweede getal in: "))


def ggd(p, q):
    if q == 0:
        return p
    else:
        return ggd(q, p % q)


print(
    "De grootste gemene deler van {} en {} ={}".format(
        getal_1, getal_2, ggd(getal_1, getal_2)
    )
)
