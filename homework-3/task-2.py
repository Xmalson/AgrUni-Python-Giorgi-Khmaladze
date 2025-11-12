print("Input first string: ")
s1 = input().lower().replace(' ','')
print("Input second string: ")
s2 = input().lower().replace(' ','')

if sorted(s1) == sorted(s2):
    print("YES")
else:
    print("NO")