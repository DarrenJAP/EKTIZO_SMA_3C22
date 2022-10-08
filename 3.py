topPopulation = {
    "Bangladesh" : 168.48,
    "Brazil"     : 216.02,
    "China"      : 1451.98,
    "Mexico"     : 132.06,
    "Pakistan"   : 231.03,
    "Indonesia"  : 280.21,
    "Nigeria"    : 218.39,
    "Russia"     : 146.07,
    "USA"        : 335.44,
    "India"      : 1411.35}

def sortByCountryName(dict):

  # Sorting
  sortedDict = sorted(dict)

  # Printing
  print("Top 10 World Population")
  print("Alphabetically Order")
  for i in range(len(sortedDict)):
    population = str(round(dict[sortedDict[i]] * 1000000))
    if (len(population) == 9):
      population_pemisah = population[0:3] + "," + population[-6:-3] + "," + population[-4:-1]
    else:
      population_pemisah = population[0] + "," + population[1:4] + "," + population[-6:-3] + "," + population[-4:-1]

    print(f"{i+1}. {sortedDict[i]}  : {population_pemisah}")

def sortByPopulation(dict):

  # Sorting
  unsortedNames = list(topPopulation.keys())
  
  # 10 is the number of iteration of sorting
  for i in range(10):
    sortingIndex = 0
    for i in range(len(unsortedNames)-1):
      if (topPopulation[unsortedNames[sortingIndex]] < topPopulation[unsortedNames[sortingIndex + 1]]):
        unsortedNames[sortingIndex], unsortedNames[sortingIndex + 1] = unsortedNames[sortingIndex + 1], unsortedNames[sortingIndex]
      sortingIndex+=1
  
  # Printing
  print("Top 10 World Population")
  print("Population Order")
  for i in range(len(unsortedNames)):
      population = str(round(dict[unsortedNames[i]] * 1000000))
      if (len(population) == 9):
        population_pemisah = population[0:3] + "," + population[-6:-3] + "," + population[-4:-1]
      else:
        population_pemisah = population[0] + "," + population[1:4] + "," + population[-6:-3] + "," + population[-4:-1]

      print(f"{i+1}. {unsortedNames[i]}  : {population_pemisah}")
  

sortByCountryName(topPopulation)
print("\n\n")
sortByPopulation(topPopulation)

# Top 10 World Population
# Alphabetically Order
# 1. Bangladesh  : 168,480,000
# 2. Brazil  : 216,020,000
# 3. China  : 1,451,980,000
# 4. India  : 1,411,350,000
# 5. Indonesia  : 280,210,000
# 6. Mexico  : 132,060,000
# 7. Nigeria  : 218,390,000
# 8. Pakistan  : 231,030,000
# 9. Russia  : 146,070,000
# 10. USA  : 335,440,000



# Top 10 World Population
# Population Order
# 1. China  : 1,451,980,000
# 2. India  : 1,411,350,000
# 3. USA  : 335,440,000
# 4. Indonesia  : 280,210,000
# 5. Pakistan  : 231,030,000
# 6. Nigeria  : 218,390,000
# 7. Brazil  : 216,020,000
# 8. Bangladesh  : 168,480,000
# 9. Russia  : 146,070,000
# 10. Mexico  : 132,060,000