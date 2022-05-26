import random

def attitude(gene):
  sum = 0
  for number in gene:
    sum = sum + int(number)

  return sum

def cross(gene1, gene2):
  pos = random.randrange(1, 10) #Generate a number between 0 and 9
  print("Pos value is: ", pos)
  gene3 = gene1[:pos] + gene2[pos:len(gene1)]
  gene4 = gene2[:pos] + gene1[pos:len(gene2)]

  return gene3, gene4

def mutate(gene):
  gene = list(gene)
  gene[random.randrange(1, len(gene)-1)] = chr(random.choice([48, 49]))
  gene = "".join(gene)

  return gene
  
def getGenerationAttitude():
  total = 0
  for gene in genes:
    total = total + attitude(gene)

  return total

def getParents():
  parent1, parent2 = genes[0], genes[0]
  
  for gene in genes:
    if(attitude(gene) > attitude(parent1)):
      parent1 = gene

  for gene in genes:
    if(gene != parent1):
      continue
    if(attitude(gene) > attitude(parent2)):
      parent2 = gene

  return parent1, parent2

def getWorst():
  worst1, worst2 = genes[0], genes[0]
  for gene in genes:
    if(attitude(worst1) > attitude(gene)):
      worst1 = gene

  for gene in genes:
    if(gene == worst1):
      continue
    if(attitude(worst2) > attitude(gene)):
      gene = worst2

  return worst1, worst2
  
# Driver code
n = 4  #Population
length = 10
gen = 0
hasChanged = []
genes = []
tolerableAttitude = 35

for i in range(n):
  genes.append("")
  for j in range(length):
    genes[i] += chr(random.randrange(2) + 48)

better = 0
print("Initial elements: ", genes)
while(getGenerationAttitude() < tolerableAttitude):
  hasChanged = genes
  print("Generation ", gen)
  print("Generation attitude: ", getGenerationAttitude())
  print("Parents of this generation ", getParents())
  print("Genes list", genes)

  parent1, parent2 = getParents()
  child1, child2 = cross(parent1, parent2)
  child1 = mutate(child1)
  child2 = mutate(child2)

  worst1, worst2 = getWorst()

  #Replace the worsts genes with the mutated childs
  for i in range(len(genes)):
    if(genes[i] == worst1):
      genes[i] = child1
    if(genes[i] == worst2):
      genes[i] = child2

  if(getGenerationAttitude() > better):
    better, betterIndex = getGenerationAttitude(), gen
  
  gen = gen + 1

print("----------------------- Better generation ---------------------------")
print("Generation ", gen)
print("Generation attitude: ", getGenerationAttitude())
print("Parents of this generation ", getParents())
print("Genes list", genes)