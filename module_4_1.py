from true_math import divide as true_div
from false_math import divide as fake_div

result1 = true_div(69, 3)
result2 = true_div(3, 0)
result3 = fake_div(49, 7)
result4 = fake_div(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)
