#We are given a string and we need to reverse words of a given string

s="hello my name is gopal agrawal"
for i in s.split()[::-1]:
    print(i,end=" ")