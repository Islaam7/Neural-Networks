import numpy as np

def step(x):
    return 1 if x >= 0 else 0
def neuron(inputs, weights, bias):
    return step(np.dot(inputs, weights) + bias)
## OR Gate
def OR_P(inputs):
    return neuron(inputs, [1, 1], -1)

## NOT Gate
def NOT_P(input):
    return neuron(input, [-1], 0)

## AND Gate
def AND_P(inputs):
    return neuron(inputs, [1, 1], -2)

## XOR Gate
# def XOR_P(inputs):
#     x, y = inputs
#     n1 = OR_P([x, y])
#     n2 = OR_P([NOT_P(x), NOT_P(y)])
#     n3 = AND_P([n1, n2])
#     return n3

## XOR Gate V2
def XOR_P(inputs):
    n1 = neuron(inputs, [1, 1], -1)
    n2 = neuron(inputs, [-1, -1], 1)
    n3 = neuron([n1, n2], [1, 1], -2)
    return n3

inputsList = [[a, b] for a in range(2) for b in range(2)]
for x in inputsList:
    print(f"AND_P({x}) = {OR_P(x)}")

print("-" * 50)

inputList = [0 ,1]
for x in inputList:
    print(f"NOT_P({x}) = { NOT_P(x)}")

print("-" * 50)

inputsList = [[a, b] for a in range(2) for b in range(2)]
for x in inputsList:
    print(f"OR_P({x}) = { OR_P(x)}")

print("-" * 50)

inputsList = [[a, b] for a in range(2) for b in range(2)]
for x in inputsList:
    print(f"XOR_P({x}) = { XOR_P(x)}")











