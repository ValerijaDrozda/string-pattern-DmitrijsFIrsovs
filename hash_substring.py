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
    g = 0
    h = 0
    a_x = 263
    b_x = 1000000007
    pos = []
    
    for  i in range(e):
        g = (g * a_x + ord(pattern[i])) % b_x
        h = (h * a_x + ord(text[i])) % b_x
    
    for i in range(f - e +1):
        if g == h and pattern == text[i:i+e]:
            pos.append(i)
        if i < f - e:
            
            f = (f - ord(text[i]) * pow(a_x - 1 , b_x)) % b_x
            f = (f  * a_x + ord(text[i + e] )) % b_x
    
    return pos



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

