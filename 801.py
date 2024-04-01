t = int(input())

while t > 0:
    n = int(input())
    s = input()
    new_s = ''
    # Your code goes here
    for i in range(0,n,2):
        if s[i] =='0' and s[i+1]=='0':
            new_s += 'A'
        elif s[i] == '0' and s[i+1] == '1':
            new_s += 'T'
        elif s[i] == '1' and s[i+1] == '0':
            new_s += 'C'
        elif s[i] == '1' and s[i+1] == '1':
            new_s += 'G'
    print(new_s)
            
    t -= 1
    