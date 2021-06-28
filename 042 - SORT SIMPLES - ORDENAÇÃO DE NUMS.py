"""
#SORT
nums = input().split()
list = [float(i) for i in nums]

list.sort()

print(*list, sep='\n')
print()
print(*nums, sep='\n')
"""
n1, n2, n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

list = [n1, n2, n3]

list.sort()

print(list[0])
print(list[1])
print(list[2])

print()

print(n1)
print(n2)
print(n3)