from random import random

def randomValue(fromValue=0, limit=10):
    return (1+(fromValue + int(random() * limit)))