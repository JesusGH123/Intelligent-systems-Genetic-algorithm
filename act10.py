# References: None, code made from scratch
import random

# Get the attitude of a single gene
# Input: A single gene (string)
# Output: The attitude of the gene to be selected (integer)
def attitude(gene):
  sum = 0
  for number in gene:
    sum = sum + int(number)

  return sum

# Cross two genes
# Input: Two different genes (strings)
# Output: Two new genes from the cross of the input ones (strings)
def cross(gene1, gene2):
  pos = random.randrange(1, len(genes[0])) #Generate a number between 0 and 9
  gene3 = gene1[:pos] + gene2[pos:len(gene1)]
  gene4 = gene2[:pos] + gene1[pos:len(gene2)]

  return gene3, gene4

# Mutate a single gene
# Input: A single gene (string)
# Output: The mutated gene, changing one of its bits (string)
def mutate(gene):
  gene = list(gene)
  gene[random.randrange(1, len(gene)-1)] = chr(random.choice([48, 49]))
  gene = "".join(gene)

  return gene
  
# Get the attitude of all the generation
# Input: None
# Output: The attitude of all the generation (integer)
def getGenerationAttitude():
  total = 0
  for gene in genes:
    total = total + attitude(gene)

  return total

# Driver code
n = 6   #Population
length = 10  #Length of each gene
gen = 0 
genes = []
tolerableAttitude = 55

for i in range(n):
  genes.append("")
  for j in range(length):
    genes[i] += chr(random.randrange(2) + 48)

better = 0
while(getGenerationAttitude() < tolerableAttitude-1):
  # Printint the values
  print()
  print("Generation ", gen)
  print("Generation attitude: ", getGenerationAttitude())
  print("Genes list", genes)

  # Cross and mutation
  genes.sort()
  print("Parents: ", genes[len(genes)-1], genes[len(genes)-2])
  print("Worst: ", genes[0], genes[1])
  child1, child2 = cross(genes[len(genes)-1], genes[len(genes)-2])
  child1 = mutate(child1)
  child2 = mutate(child2)

  genes[0], genes[1] = child1, child2

  gen = gen + 1
  
  if(getGenerationAttitude() > better):
    better, betterIndex = getGenerationAttitude(), gen

print("\n--------- Better generation ----------")
print("Generation ", betterIndex)
print("Generation attitude: ", better)
print("Genes", genes)