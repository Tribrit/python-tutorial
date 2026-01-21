import math

def exponential_function(x):
  return math.exp(x)

for x in range(-5, 6):
  y = exponential_function(x)
  print('f"x = {x}, y = {y:.2f}"')