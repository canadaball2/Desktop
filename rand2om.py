import random as rr

list_of_evil = ["67", "she", "alcohol", "gambling", "drugs", "napalm", "war crimes", "bad", "CLANREWORK", "jigglypuff", "calculator snake", "mean"]

random_evil = rr.choice(list_of_evil)
print(random_evil)

if random_evil == "she":
    print("Grab her head for it")
elif random_evil == "CLANREWORK" or random_evil == "jigglypuff":
    print("Where are you CLANREWORK")