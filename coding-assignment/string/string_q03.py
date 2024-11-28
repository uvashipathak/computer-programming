'''Given the string, the task is to capitalize the first and last character of each word in a string. 

Examples:

Input: hello world 
Output: HellO WorlD
Input: welcome to geeksforgeeks
Output: WelcomE TO GeeksforgeekS'''

s="hello my name is mark ruffalo"
l=""
for i in s.split():
    h=""
    for k in i:
        if k==i[0] or k==i[-1] :
            h+=k.upper()
            continue
        h+=k
    h+=" "
    l+=h
print(l)