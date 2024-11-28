#Given a String, compute all the characters, except spaces.
s="hey hello world"
count=0
for i in s:
    if i==' ':
        continue
    count+=1
print(count)