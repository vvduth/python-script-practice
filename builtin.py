# string method
message = "duc is an MMA fighter, MMA is the great sport, combine striking and grappling"
print(message)
print(message.capitalize())
text = message.capitalize()
print(text)

# dir functino
print(message.upper())
print(message.islower())
print(message.isupper())

print(message.find("MMA"))
print(message[18:24])
print(message.find("unemployed"))

seq1=("MuayThai", "Boxing", "Wrestling")
print(".".join(seq1))
print("/".join(seq1))
print("-".join(seq1))

SKILLS2 = ["Muay Thai", "Wrestling", "Boxing", "Ju Jitsu", "Kickboxing"]
print(SKILLS2)

SKILLS2.append("Sambo")
print(SKILLS2)

SKILLS2.extend(["Judo", "Karate"])
print(SKILLS2)

SKILLS2.insert(2, "Teakwondo")
print(SKILLS2)


person1= {"Name": "Santa", "Skill": "Blockchain", "code": 1024}
person2 = {"Name": "Rocky", "Skill": "AI", "code": 1218}

print(person1.keys())
print(person2.keys())
