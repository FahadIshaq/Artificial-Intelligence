# Name: Fahad Ishaq
# Reg. No: FA20-BCS-017

# --------------- ACTIVITIES ----------------
# ACTIVITY 1 (Accept two lists from user and return their join)

list1 = []
list2 = []
print("Enter 3 elements for list 1")
for i in range(3):
    number = input("Enter element "+str(i+1)+": ")
    list1.append(number)

print("Enter 3 elements for list 2")
for j in range(3):
    number = input("Enter element "+str(j+1)+": ")
    list2.append(number)
print("List 1: ", list1)
print("List 2: ", list2)
print("The joined list is: ", list1+list2)


# ACTIVITY 2 (A palindrome is a string which can be read forward or backwords)

def is_Palindrome(n):
    for i in range(len(n)):
        if n[i] != n[len(n)-i-1]:
            return False
    return True


def main():
    n = input("Enter a word: ")
    if (is_Palindrome(n) == True):

        print(n + " is palindrome")
    else:
        print(n + " is not a palindrome")


main()

# ACTIVITY 3 (Imagine two matrices given in the form of 2D lists as under; a = [[1, 0, 0], [0, 1, 0], [0, 0, 1] ]
# b = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
# )


def product(a, b):
    c = [[]]
    # a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    # b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    for i in range(3):
        c.append([])
        for j in range(3):
            c[i].append(0)
            for k in range(3):
                c[i][j] += a[i][k]*b[j][i]

    print(c)


def main():
    a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    product(a, b)


main()


# ACTIVITY 4 (A closed polygon with N sdes can be represented as a list of touples of N connected coordinates. )
# Write a python function that takes a list of N tuples as input and returns the perimeter of the polygon. Remember that your code should work for any value of N.

def perimeterOfPolygon(number):
    perimeter = 0
    length = len(number)
    for i in range(0, length-1):
        distance = math.sqrt(
            (number[i+1][0]-number[i][0])**2+(number[i+1][1]-number[i][1])**2)
        perimeter = perimeter+distance
    perimeter = perimeter+math.sqrt((number[0][0]-number[length-1][0])**2)
    return perimeter


def main():
    l = [(0, 0), (0, 5), (3, 5), (3, 0)]
    print(perimeterOfPolygon(l))


main()

# ACTIVITY 5 (Symmetric Difference of two sets is the set of elements which are in either of the sets and not in their intersection. )


def summetricDifference(a, b):
    e = set()
    for i in a:
        if i not in b:
            e.add(i)
    for i in b:
        if i not in a:
            e.add(i)
    return e


def main():
    set1 = {0, 1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8, 9}
    print(summetricDifference(set1, set2))


main()


# ACTIVITY 6 (Create a Python Program that contains a name of dictionary of names and phone numbers...)
dictionary = {
    ("Fahad", "Ishaq"): "012516211",
    ("Kumail ", "Hussain"): "012516212",
    ("Ali", "Ahmed"): "012516213",
}

firstName = input("Enter first name: ")
lastName = input("Enter last name: ")

search = (firstName, lastName)
if (search in dictionary):
    print(dictionary[search])
else:
    print("Person Not Found")


# ----------------------------GRADED ACTIVITIES---------------------------

# LAB TASK 1  (Create two lists based on the user values. Merge both the lists and display in sorted order)

list1 = []
list2 = []

print("Enter elements for list 1")
for i in range(3):
    n = input("Enter number " + str(i+1) + ": ")
    list1.append(n)

print("Enter elements for list 2")

for j in range(3):
    n = input("Enter number " + str(j+1) + ": ")
    list2.append(n)


list3 = list1+list2
list3.sort()
print("The sorted list is: ", list3)


# LAB TASK 2 (Repeat the above activity to find the smallest and largest element of the list. (Suppose all the elements are integer values)
list1 = []
list2 = []

print("Enter elements for list 1")
for i in range(3):
    n = input("Enter number " + str(i+1) + ": ")
    list1.append(n)

print("Enter elements for list 2")

for j in range(3):
    n = input("Enter number " + str(j+1) + ": ")
    list2.append(n)


list3 = list1+list2
list3.sort()
print("The Smallest Integer: ", list3[0])
print("The Largest Integer: ", list3[len(list3)-1])


# TASK 3 (For this exercise, you will keep the track of when your friend's birthday...)
dictionary = {
    "Fahad": "21/08/2001",
    "Kumail": "9/09/2000",
    "Ali": "7/10/2001",
    "Zain": "7/10/2001",
    "Idrees": "6/1/2008",

}

print("We know the birthdays of: ")
for key in dictionary.keys():
    print(key)

birthday = input("Whose birthday do you want to look up? ")
if (birthday not in dictionary):
    print("Birthday Does Not Exists")
else:
    print(birthday + "'s birthday is " + dictionary[birthday])

# TASK 4 (Create a dictionary by extracting the keys from the given dictionary...)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]

new_dictioinary = {}

for i in range(len(keys)):
    new_dictioinary[keys[i]] = sample_dict[keys[i]]

print(new_dictioinary)
