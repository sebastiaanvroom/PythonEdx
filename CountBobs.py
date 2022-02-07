# This script counts vowels in a given variable 's'
s = "azcbobobegghaklbob"
#i = 0
#count = 0
#print(len(s))
#f = s[i]
#print(f)
count = 0
for x in range(len(s)):
    if x == len(s) - 2:
        break
    if (s[x]) == 'b' and (s[x+1]) == 'o' and (s[x+2]) == 'b':
        count = count + 1
print('Number of times bob occurs is: ' + str(count))

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