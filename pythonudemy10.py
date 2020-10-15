# Python program to illustrate
# while loop
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")

print()

# checks if list still
# contains any element
a = [1, 2, 3, 4]
while a:
    print(a.pop())



# Python program to illustrate
# Single statement while block
count1 = 0
while (count1 < 5): count1 += 1; print("Hello Geek")

# Prints all letters except 'e' and 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    print('Current Letter :', a[i])
    i += 1

# break the loop as soon it sees 'e'
# or 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break
    print('Current Letter :', a[i])
    i += 1

