#!/usr/bin/python3

a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a + b
print("Goodbye.")
