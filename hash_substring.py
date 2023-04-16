# python3

def read_input():
    a = input().rstrip()
    if a == 'f':
        with open(input().rstrip(), 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip() 
    else:
        pattern = input().rstrip()
        text = input().rstrip()
    
    return pattern , text

def print_occurrences(output):
  
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    e = len(pattern)
    f = len(text)
    g= hash(pattern)
    h = hash(text[:e])
    pos = []
    
    for i in range(f - e + 1):
        if g == h and pattern == text[i:i+e]:
            pos.append(i)
        if i< f - e:
            f = hash(pattern[i+1:i+1+e])
            
    
    return pos



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

