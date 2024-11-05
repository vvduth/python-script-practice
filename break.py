import random
for i in "devops":
    if i == "o":
        print("Found my data")
        break
    print(f"value of i is {i}")

print("-------------------------------")

for i in "devops":
    if i == "o":
        print("Found my data")
        continue
    print(f"value of i is {i}")
    
print("Out of loop")


SKILLS2 = ["Muay Thai", "Wrestling", "Boxing", "Ju Jitsu", "Kickboxing"]
random.shuffle(SKILLS2)
print(SKILLS2)

LUCKY = random.choice(SKILLS2)
print(LUCKY)
print()
for martial in SKILLS2: 
    print(f"********* Leaning  {martial} ****************")
    if martial == LUCKY:
        print("-----------------------------------")
        print(f"{LUCKY} has successgully learned")
        print("-----------------------------------")
        print()
        continue
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("Failed to laern this art")
    print()