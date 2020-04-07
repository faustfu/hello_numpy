import math

test_price = 20

scale = [0, 1]
auction = [100, 200]

def x2angle(x):
  return float(90 * x)

def angle2radian(angle):
  return float(angle / 90 * math.pi / 2)

# for i in range(100):
#   angle = i/200*math.pi
#   print(math.sin(angle))
# print(f'price = {test_price}, angle = {price2angle(test_price)}, radian = {angle2radian(price2angle(test_price))}')
for i in range(0, 100):
  mi = float(i/100)
  x = math.cos(angle2radian(x2angle(mi)))
  y = math.sin(angle2radian(x2angle(mi)))
  print(f'price = {x}, angle = {x2angle(x)}, radian = {angle2radian(x2angle(x))}, x = {x}, y = {y}')