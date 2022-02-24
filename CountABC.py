i = s[0]
a = s[0]
for c in s[1:]:
    if c >= a[-1]:
        a += c
        if len(a) > len(i):
            i = a
    else:
        a = c
print("Longest substring in alphabetical order is:", i)