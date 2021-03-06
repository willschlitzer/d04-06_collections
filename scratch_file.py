from collections import defaultdict, namedtuple, Counter, deque
from timeit import timeit
import random
import csv


def createNamedTuple():
    """Demonstrate the use of named tuples"""
    # First field is the subclass (in this case User)
    # Second field can either be multple strings or a single string with whitespace/commas inbetween names
    User = namedtuple("User", "name role")
    user = User(name="Will", role="coder")
    # print(user.name)
    # print(user.role)


def createDefaultDict():
    """Demonstrates how defaultdicts work around errors that would happen with standard dicts"""
    missions_flown = [
        ("will", 50),
        ("matt", 10),
        ("oliver", 200),
        ("will", 75),
        ("matt", 20),
        ("oliver", 300),
    ]
    # Using a for loop to append the values would cause errors as keys are duplicated
    # Default dicts allow for a default data type to be added (in this case, lists)
    missions = defaultdict(list)
    for name, mission in missions_flown:
        missions[name].append(mission)
    print(missions)

def demoCounter():
    with open("Ground_Speed_Check.txt", "r") as f:
        story = f.read().split()
    print(Counter(story).most_common(25))

def demoDeque():
    """Demo to show the difference between deques and lists"""
    # Specifies max length for deque object
    # Default is no max length
    mydeque = deque(range(25), 25)
    print(mydeque)
    # Appending at the end of the deque removes the first value
    mydeque.append(100)
    print(mydeque)

# print(timeit("createNamedTuple()", setup="from __main__ import createNamedTuple", number=100))
#createDefaultDict()
#demoCounter()
demoDeque()