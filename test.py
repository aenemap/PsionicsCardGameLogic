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

# from time import sleep

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




# def actions(currentAction, totalActions):
#     while currentAction <= totalActions:
#         yield print(currentAction)
#
# currentAction = 1
# for action in range(1,5):
#     next(actions(currentAction, 5))
#     currentAction += 1
#
#
#
# class Turn(object):
#
#     def __init__(self, totalActions):
#         self.totalActions = totalActions
#
#     def actions(currentAction, totalActions)

def turns(totalTurns):
    
