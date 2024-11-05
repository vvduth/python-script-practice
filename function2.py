
import random
def martial_art_feeback(martialart, efficiency):
    print(f"{martialart} is having {efficiency}% in MMA")
    if (efficiency > 50) and (efficiency <=75):
        print(f"Seems not so effective, need for trials for MMA")
    if (efficiency > 75) and (efficiency < 90):
        print(f"This martail art can be considered as effective")
    if (efficiency >= 90) :
        print(f"This is good, learn this")
    else:
        print("Do not learn this, this does not help in MMA")
        


# non keywork argument with *args
def order_food(min_order, *args): 
    print(f"you have ordered: {min_order}")
    print(args)
    for item in args:
        print(f"you have ordered: {item}")
    print("your food will be delivered in 30 mins:")
    print("Enjoy the party")
    


#  keywork argument with *args
def time_activity(*args, **kargs):
    print(args)
    print(kargs)
    min = sum(args) + random.randint(0,60) 
    print(min)
    choice = random.choice(list(kargs.keys()))
    print(choice)
    print(f"You have decided to send {min} minutes for {kargs[choice]}")

