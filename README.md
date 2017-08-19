# Evaluating-Base--Background on Permutations
The number of permutations of N distinct elements is N factorial, denoted as N!. The factorial
of N is the product of all positive integers less than or equal to N: N! = 1 × 2 × 3 × · · · × N.
Denote the set of all permutations of N (distinct) elements in a set by SN . For example, the
permutation set S4 corresponding to a set made up of English letters {a,b,c,d} has 4! = 24
permutations in it, and these are:

0 abcd 		6 bacd 		12 cabd 	18 dabc
1 abdc 		7 badc 		13 cadb 	19 dacb
2 acbd 		8 bcad 		14 cbad 	20 dbac
3 acdb 		9 bcda 		15 cbda 	21 dbca
4 adbc 		10 bdac 	16 cdab 	22 dcab
5 adcb 		11 bdca 	17 cdba 	23 dcba

Observe that these permutations are printed in the lexicographic order of the letters. Notice
also that a decimal number/index is listed in order associated with each permutation. That is,
the permutation number 0 represents a fully-ordered permutation, abcd, in the above example.
For any N, there are several ways to print all the permutations in SN in the lexicographic
order. One way relies on converting the permutation number from a decimal system (or base-10

system) into a number in a new number system, which we will call here the F-number
system. Numbers in the F-number system are denoted here as base-! numbers. In any given
permutation set SN , each permutation number/index D in base-10 – (D)10, in short – where
0 ≤ D < N!, can be represented uniquely as:

(D)10 = CN−1 × (N − 1)! + CN−2 × (N − 2)! + · · · + C1 × 1! + C0 × 0! (1)
where CN−1, CN−2, · · · C0 form the digits in the base-! system.

If the property in Equation 1 holds, then the base-! number (CN−1CN−2 · · · C0)! in Fnumber
system is equivalent to (D)10 in the base-10 number system. As a concrete example,
below is a table that shows all the base-10 permutation numbers and their corresponding
base-! numbers for permutations in S4 over the letters {a, b, c, d}.
        BASE-10 BASE-! PERMUTATION | BASE-10 BASE-! PERMUTATION
-----------------------------------|------------------------------------
	     ( 0)_10 (0000)_! abcd | (12)_10 = (2000)_! cabd
	     ( 1)_10 (0010)_! abdc | (13)_10 = (2010)_! cadb
	     ( 2)_10 (0100)_! acbd | (14)_10 = (2100)_! cbad
	     ( 3)_10 (0110)_! acdb | (15)_10 = (2110)_! cbda
	     ( 4)_10 (0200)_! adbc | (16)_10 = (2200)_! cdab
	     ( 5)_10 (0210)_! adcb | (17)_10 = (2210)_! cdba
	     ( 6)_10 (1000)_! bacd | (18)_10 = (3000)_! dabc
	     ( 7)_10 (1010)_! badc | (19)_10 = (3010)_! dacb
	     ( 8)_10 (1100)_! bcad | (20)_10 = (3100)_! dbac
	     ( 9)_10 (1110)_! bcda | (21)_10 = (3110)_! dbca
	     (10)_10 (1200)_! bdac | (22)_10 = (3200)_! dcab
	     (11)_10 (1210)_! bdca | (23)_10 = (3210)_! dcba
For instance, we can work out one of the base-10 to base-! conversion (shown above) as:
(15)10 = 2{C3}×3! + 1{C2}×2! + 1{C1}×1! + 0{C0}×0! = (2110)!
Further, the digits CN−1, CN−2, · · · C0 have a very special meaning. Notice, from the example
above, there are as many base-! digits as there are letters in the permutation string. Each
digit in this system gives the number of inversions of each letter in the permutation compared
to the fully-ordered permutation. What does this mean? Let us see using the same example as
above:
(15)_10 = (2110)_! c b d a
For a better (visual) understanding, the base-! digits are arranged right
under this permutation:
c b d a
2 1 1 0
Then, these base-! digits have the following meaning:
For the 1st letter ‘c’, there are 2 letters to the right of it (i.e., ‘b’ and ‘a’)
that are lexicographically LESS than ‘c’.
For the 2nd letter ‘b’, there is 1 letter to the right of it (‘a’) that
is lexicographically LESS than ‘b’.
2
For the 3rd letter ‘d’, there is 1 letter to the right of it (‘a’) that
is lexicographically LESS than ‘d’.
For the 4th letter ‘a’, there are 0 letters to the right of it that
are lexicographically LESS than ‘a’.
In fact, the sum of these base-! digits gives the total number of transpositions (or swaps
between adjacent letters) needed to convert the permutation into a fully sorted order. In the
example we have been considering so far, the sum of digits in (2110) ! = 2 + 1 + 1 + 0 = 4,
implying that this permutation needs 4 transpositions to convert from cbda to abcd. Let us
see how! Working from right to left and applying the number of successive swaps as indicated
by the base-! digit under each symbol:
c b d a
2 1 1 0
SWAPS: #1 #2 #3 #4
cbda --> cbad --> cabd --> acbd --> abcd
It is also straightforward to construct a permutation string from just the base-! digits (and
the total ordering of the N letters in the permutation). Let’s follow this with the same example:
N = 4
Below is the total ordering of the letter in S_4
Index: 0 1 2 3
Total ordering: a b c d
Our goal now is to generate the permutation given the following
base_! digits : 2 1 1 0
First digit is 2; find the symbol at index=2 in the total ordering set
and place it as the first symbol of the permutation:
c
Remove c from the total ordering:
Index: 0 1 2
Total ordering: a b d
Next digit is 1; find the symbol at index=1 in this new total ordering set
and place it as the second symbol of the permutation:
c b
Remove b from the total ordering:
Index 0 1
Total ordering: a d
Next digit is 1 again; find and place the symbol at index=1
as the third symbol of the permutation:
c b d
Remove d from the total ordering:
Index 0
Total ordering: a
3
Next digit is 0; find and place the symbol at index = 0
as the fourth symbol of the permutation:
c b d a

Computing matrix determinant using permutations
In linear algebra, the determinant of a square matrix is a value that is commonly computed
for various purposes. Coincidentally, since this prac deals with permutations and inversions,
one of the ways of computing the determinant of an N × N real square matrix is using the
information of all permutations of the set {1, 2, . . . , N}. Consider the matrix for the form:
A =

|A(1, 1) A(1, 2) · · · A(1, N)|
|A(2, 1) A(2, 2) · · · A(2, N)|
|.	..		  .   |
|.		..	  .   |
|A(N, 1) A(N, 2) · · · A(N, N)|

Then its determinant, denoted by det(A), is given by a formula:

For example, for a 3 × 3 matrix, it is easy to see:
det(A) = 
	+ A(1, 1)A(2, 2)A(3, 3) − A(1, 1)A(3, 2)A(2, 3)
	− A(2, 1)A(1, 2)A(3, 3) + A(2, 1)A(3, 2)A(1, 3)
	+ A(3, 1)A(1, 2)A(2, 3) − A(3, 1)A(2, 2)A(1, 3)


where the 6 permutations of S3 appear within the 6 terms on the right hand side, shown in red,
and the evaluated sign of each term (based on the parity of the total number of inversions) via
sgn(perm) is shown in blue.



Programs:


CreatePermutations.py:
Given a user input (n), the program outputs all permutations of the first (n) letters of the alphabet. The program also outputs to the file
permutations.txt all the base-! conversions for these permutations, and a frequency table for the sums of the base-! conversions.

DistanceBetweenPermutations.py:
User input provides 2 permutations of the first n letters of the alphabet. The program then, using the background information, calculates
and outputs the number of steps required to change one permutation into the other. This is outputted into distance.txt

