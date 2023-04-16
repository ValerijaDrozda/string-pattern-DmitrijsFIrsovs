# python3

def read_input():
    a = input().rstrip()
    if a == 'f':
        with open(input().rstrip(), 'r') as f:
            b = f.readline().rstrip()
            c = f.readline().rstrip() 
    else:
        b = input().rstrip()
        c = input().rstrip()
    
    return b,c

def print_occurrences(output):
  
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    e = len(b)
    f = len(c)
    g= hash(b)
    h = hash(c[:e])
    pos = []
    
    for i in range(f - e + 1):
        if g == h and b == c[i:i+e]:
            pos.append(i)
        if i< f - e:
            f = hash(b[i+1:i+1+e])
            
    
    return pos



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

