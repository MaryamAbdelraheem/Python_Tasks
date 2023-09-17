
#Using the names list create a python code that :

'''
1.Transform all names to uppercase
using [normal list - list comprehension - functional programming]
'''
Names = ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha']

# Using normal list
upper_names_normal = []
for name in Names:
    upper_names_normal.append(name.upper())
print("Upper names using normal list:", upper_names_normal)

# Using list comprehension
upper_names_lc = [name.upper() for name in Names]
print("Upper names using list comprehension:", upper_names_lc)

# Using functional programming - map()
upper_names_fp = list(map(str.upper, Names))
print("Upper names using functional programming:", upper_names_fp)


'''
2.Get the names that contains ‘a’ in a list using
[normal list - list comprehension - functional
programming]
'''

# Using normal list
names_with_a_normal = []
for name in Names:
    if 'a' in name:
        names_with_a_normal.append(name)
print("Names with 'a' using normal list:", names_with_a_normal)

# Using list comprehension
names_with_a_lc = [name for name in Names if 'a' in name]
print("Names with 'a' using list comprehension:", names_with_a_lc)

# Using functional programming - filter()
names_with_a_fp = list(filter(lambda name: 'a' in name, Names))
print("Names with 'a' using functional programming:", names_with_a_fp)

'''
3.Get the names that starts with ‘t’ in a list using
[normal list - list comprehension - functional
programming]
'''

# Using normal list
names_starting_with_t_normal = []
for name in Names:
    if name.startswith('t'):
        names_starting_with_t_normal.append(name)
print("Names starting with 't' using normal list:", names_starting_with_t_normal)

# Using list comprehension
names_starting_with_t_lc = [name for name in Names if name.startswith('t')]
print("Names starting with 't' using list comprehension:", names_starting_with_t_lc)

# Using functional programming - filter()
names_starting_with_t_lambda = list(filter(lambda name: name.startswith('t'), Names))
print("Names starting with 't' using functional programming:", names_starting_with_t_lambda)

'''
4.Get the names that contains 2 or more ‘a’ letter using
[normal list - list comprehension - functional
programming]
'''

# Using normal list
names_normal = []
for name in Names:
    if name.count('a') >= 2:
        names_normal.append(name)
print("Names containing 2 or more 'a' using normal list:", names_normal)

# Using list comprehension
names_lc = [name for name in Names if name.count('a') >= 2]
print("Names containing 2 or more 'a' using list comprehension:", names_lc)

# Using functional programming - filter()
names_fp = list(filter(lambda name: name.count('a') >= 2, Names))
print("Names containing 2 or more 'a' using functional programming:", names_fp)

'''
5.Print a list contains the len of each word
in the list using [normal list - list comprehension -
functional programming]
'''

# Using normal list
word_lengths_normal = []
for name in Names:
    word_lengths_normal.append(len(name))
print("Word lengths using normal list:", word_lengths_normal)

# Using list comprehension
word_lengths_lc = [len(name) for name in Names]
print("Word lengths using list comprehension:", word_lengths_lc)

# Using functional programming - map()
word_lengths_fp = list(map(len, Names))
print("Word lengths using functional programming:", word_lengths_fp)


'''
6.Unpack the list in a,b
'''
'''
    6.1. a=the first index , b = rest of the list
'''
a1 = Names[0]
b1 = Names[1:]

'''
    6.2. a=the first index , b = the last index
'''

a2 = Names[0]
b2 = Names[-1]

'''
    6.3. a = the first index , b = the second index
'''
a3 = Names[0]
a3 = Names[1]


