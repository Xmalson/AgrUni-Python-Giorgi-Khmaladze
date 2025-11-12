s = "azcbobobegghakl"

longest_string = s[0]
temp_string = s[0]

for i in range(1,len(s)):
    if s[i] >= s[i-1]:
        temp_string += s[i]
    else:
        temp_string = s[i]
    if len(temp_string) > len(longest_string):
        longest_string = temp_string

print(longest_string)