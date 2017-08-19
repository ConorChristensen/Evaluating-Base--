#Conor Christensen
#Last edited 14/04/17

while True: #input check
    n = int(input("Please input your N value between the values 0 and 10: "))
    if n >=0 and n <= 10:
        break
    else:
        print("Invalid N value, please try again...")

def factorial(a): #Simple factorial function as apposed to importing math
    if a == 0:
        return 1
    else:
        return a*factorial(a-1)

def create_permutations(n):
    all_perms = []
    for m in range(0, factorial(n)):
        perm_num = m + 1
        permutation = []
        for o in range(n-1, -1, -1):
            for p in range(n):
                if perm_num != sum(permutation) or len(permutation) != n:
                    if perm_num - p*factorial(o) <= factorial(o):
                        permutation.append(p)
                        perm_num -= p*factorial(o)
                        break
                    elif p == n-1:
                        permutation.append(0)
        all_perms.append(permutation)
    return(all_perms)

def convert_to_letters(permutation):
    alph_list = ['a','b','c','d','e','f','g','h','i','j'] #only ten letter maximum
    output_list = []
    for i in range(len(permutation)):
        output_list.append(alph_list[permutation[i]])
        alph_list.pop(permutation[i]) #removing the letter from the list to suppor the given indexing convention
    return output_list


def print_permutations(perm_list, n):
    output_file = open("permutations.txt","w")
    output_file.write("Input into the script: " + str(n) + '\n')
    output_file.write("Total number of permutations = " + str(factorial(n)) + '\n')
    output_file.write("Base_10      " + "Base_!       " + "Sum       " + "Permutation    " + '\n')
    sum_freq = []
    for j in range(50):
        sum_freq.append(0)
    for i in range(len(perm_list)):
        output_file.write("(" + str(i) + ")_10   " + str(perm_list[i]) + "_!    " + str(sum(perm_list[i])) + "    " + str(convert_to_letters(perm_list[i])) + '\n')
        sum_freq[sum(perm_list[i])] += 1
    output_file.write("\n \n Frequency      Table \n ------------------- \n" )
    output_file.write("        " +str(0)+"        " + str(sum_freq[0]) + "\n")
    p = 1
    while sum_freq[p] != 0:
        output_file.write("        " +str(p)+"        " + str(sum_freq[p]) + "\n")
        p += 1
    weighted_av = 0
    for l in range(p):
        weighted_av += sum_freq[l]*l
    weighted_av = weighted_av//p
    output_file.write("Weighted Average = " + str(weighted_av))
    print(weighted_av)

print_permutations(create_permutations(n), n)




