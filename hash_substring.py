# python3

def read_input():
    a = input().rstrip().lower()
    aa = input().rstrip().lower()
    
    if aa == 'f':
        with open('input,txt', 'r') as f:
            pattern = f.readline().rstrip().lower()
            text = f.readline().rstrip().lower() 
    else:
        pattern = input().rstrip().lower() 
        text = input().rstrip().lower() 
    
    return pattern , text

def print_occurrences(output):
  
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    e = 31
    f = 10**9 +9
    g = 0
    h = 0
    x = 1
    
    pos = []
    
    for  i in range(e):
        g = (g + (ord(pattern[i]) - ord('a') + 1) * x) % f
        h = (h + (ord(text[i]) - ord('a') + 1) * x) % f
        f = (x * e) % f
        
    if g == h and pattern == text[:len(pattern)]:
        pos.append(0)
    
    for i in range(len(pattern), len(text)):
        h = (h - (ord(text[i - len(pattern)]) - ord('a') + 1) * x) % f
        h = (h * e + (ord(text[i]) - ord('a') + 1)) % f
        if g == h and pattern == text[i - len(pattern) + 1:i + 1]:
            pos.append(i - len(pattern) +1)
            
    
    return pos



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

