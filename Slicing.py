planet1="closest to the sun"
print(planet1)

print(planet1[0])
print(planet1[1])
print(planet1[2])

# slicing a string, get the substring

print(planet1[1:4])
print(planet1[:])
print(planet1[:7])
print(planet1[12:])

# slice a tuple
devops =("Linux", "Vagraant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")
print(devops[0])
print(devops[-1])

print(devops[2:5]) # return a tuple
print(devops[2:5][0])

print(devops[2:5][0][5:11])
print("-------------------------------------------------------------------------------------")

# slice a list
devopsList =["Linux", "Vagraant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]
print(devopsList[0])
print(devopsList[-1])

print(devopsList[2:5]) # return a lisy
print(devopsList[2:5][0])

print(devopsList[2:5][0][5:11])

print("-------------------------------------------------------------------------------------")
# Dictionary
Skills = {"devops": ("Linux", "Vagraant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"), "Devlopment" : ["Java", "NodeJS", ".NET"]}

print(Skills)
print(Skills["devops"])

print(Skills["devops"][-1][:3])