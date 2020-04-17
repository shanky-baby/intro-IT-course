# Headings 
print(": Celestial Body : Mass Multiplier :")

# Data used for rows in table
nestedList = [["Mercury",0.378],
              ["Venus",0.907],
              ["Moon",0.166],
              ["Mars",0.377],
              ["Io",0.1835],
              ["Europa",0.1335],
              ["Ganymede",0.1448],
              ["Callisto",0.1264],]

for item in nestedList :
    print(":",item[0]," "*(13-len(item[0])),":",
              item[1]," "*(14-len(str(item[1]))),":",
         )   

print()

# Astronaught weight allowances 
print("Flight Crew: 100kg each (4 people)")
print("Mission Specialists: 150kg each (2 people)")

print()

# Personal weight allowance for Callisto travel
print("Flight Crew: 100kg * 0.1264")
print("=",100 * 0.1264,"kg")
print("Mission Specialists: 150kg * 0.1264")
print("=",150 * 0.1264,"kg")

print()

# Total weight allowance for callisto travel
print("Total weight: Flight Crew + Mission Specialists")
numbers = [100 * 0.1264,150 * 0.1264]
sum = sum(numbers)
print("=",sum,"kg")

print()

# Average weight allowance







