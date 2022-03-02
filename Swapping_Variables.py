# swapping variables
a = 5
b = 6

a = a ^ b  # a = a + b
b = a ^ b  # b = a - b
a = a ^ b  # a = a - b

print(a)
print(b)

a = 10
b = 15
a, b = b, a
print(a)
print(b)

# while loop

nb = 7
i = 0
while i < 10:
    print(i+1, "*", nb, "=", (i+1) * nb)
    i += 1

# a) 1+2+3+....+100
s = 0
for j in range(1, 101):
    s = j+s
    print((j, s))
