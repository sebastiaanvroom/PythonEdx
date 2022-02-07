# This script counts vowels in a given variable 's'
s = "azcbobobegghakl"
#i = 0
#count = 0
#print(len(s))
#f = s[i]
#print(f)
count = 0
for x in range(len(s)):
  print(s[x])
  if (s[x]) == 'a' or (s[x]) == 'e' or (s[x]) == 'i' or (s[x]) == 'o' or (s[x]) == 'u' :
      count = count + 1
print(count)

#while (i <= len(s)):
#    f = s[i]
#    if(f == "a"):
#        count =+ 1
#        print(count)
#        i =+ 1
#        print(i)
#    else:
#        i =+ i+1
#print("Number of vowels: " + count)