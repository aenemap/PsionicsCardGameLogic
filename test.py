# def grep(pattern):
#     print('Searching for ', pattern)
#     while True:
#         line = (yield)
#         if pattern in line:
#             print(line)
#
# search = grep('coroutine')
# next(search)
# search.send("I love you")
# search.send("Dont you love me?")
# search.send("I love coroutines instead")


# def turns(totalTurns):
#     currentTurn = 1
#     while currentTurn <= totalTurns:
#         yield currentTurn
#         currentTurn += 1
#
#
# while True:
#     for action in turns(5):
#         print('Action {0}'.format(action))

# def func1():
#     print('I am func1')
#
# def func2():
#     print('I am func2')
#
# functions = []
# functions.append(func1)
# functions.append(func2)
#
# for func in functions:
#     func()

# from collections import deque
# def func1():
#     print('I am func1')
#
# def func2():
#     print('I am func2')
#
#
# functions = deque([])
# functions.append(func2)
# functions.append(func1)
#
# function = functions.popleft()
# function()
# function = functions.popleft()
# function()

def ability1():
    print('Resolving ability 1')

def ability2():
    print('Resolving ability 2')

def ability3():
    print('Resolving ability 3')

def ability4():
    print('Resolving ability 4')

def ability5():
    print('Resolving ability 5')

abbilitiesList = []
abbilitiesList.append({'priority': 2, 'ability': ability1})
abbilitiesList.append({'priority': 5, 'ability': ability2})
abbilitiesList.append({'priority': 1, 'ability': ability3})
abbilitiesList.append({'priority': 3, 'ability': ability4})
abbilitiesList.append({'priority': 4, 'ability': ability5})

sortedAbilities = sorted(abbilitiesList, key=lambda k: k['priority'])

for ab in sortedAbilities:
    ab['ability']()
