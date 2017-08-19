
#Conor Christensen
#Last edited 14/04/17

import math

perm1Input = input("Please enter the first permutation: ")
perm2Input = input("Please enter the second permutation: ")

perm1 = []
perm2 = []

for letter in perm1Input:
    perm1.append(letter)
for letter in perm2Input:
    perm2.append(letter)


while len(perm1) != len(perm2): #a check for correct permutation dimensions
    print('Please enter equal sized permutations')

    perm1Input = input("Please enter the first permutation: ")
    perm2Input = input("Please enter the second permutation,: ")

    for letter in perm1Input:
        perm1.append(letter)
    for letter in perm2Input:
        perm2.append(letter)

perm1_base = [] #new lists for each permutation in base_!
perm2_base = []
letter_indexes = []

for i in range(len(perm1)):
    perm1_base.append([perm1[i]]) #append the list of the permutation numbers

for j in range(len(perm1_base)):
    for k in range(len(perm2)):
        if perm2[k] == perm1_base[j][0]: #This if conditionality matches the letters in order to organise the data.
            letter_indexes.append([perm2[k], j, k]) #This gives a list showing eash item
                                                    # as a letter with its before and after index. Additionally it
                                                    #maintains the order of the second permutation.

change_in_permutation = [] #The base_! letter code for the difference in the permutations

l_loops = len(letter_indexes) #This is done because the length of letter_indexes will change during the loop

for l in range(l_loops):
    next_letter = l_loops #Keeps the next_letter at a maximum with every iteration
    for m in range(len(letter_indexes)):
        if letter_indexes[m][2] < next_letter: #Check which letter is 'next' in the new permutation
            next_letter = letter_indexes[m][2]
            next_letter_index = m
    change_in_permutation.append(next_letter_index) #append the index of the 'next letter' relative to the final permutation
    letter_indexes.pop(next_letter_index)

steps = sum(change_in_permutation)
output_file = open("distance.txt","w")
output_file.write("The minimum number of steps between the two permutations is:  \n" + str(steps))
output_file.close()
