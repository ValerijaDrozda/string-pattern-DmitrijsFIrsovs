# python3

def read_input():
    a = input().strip().upper()
    pattern = input().strip()
    text = input().strip()
     
    if a == 'F':
        with open(text, "r") as f:
            
            text = f.read().strip()
        
    return pattern , text

def print_occurrences(output):
  
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 1000000007
    x = 263

    for  i in range(len(pattern):
        g = sum([ord(pattern[i]) * x**i for i in range(len(pattern))]) % p
        h = sum([ord(text[i]) * x**i for i in range(len(pattern))]) % p
                   
    pos = []                
   
    for i in range( len(text), len(pattern) + 1):
        if  g == h and text[i:i + len(pattern)] == pattern:
             pos.append(i)
        if i < len(text) - len(pattern):
            hash = 0
            for j in range(len(pattern)):
                hash += ord(text[i+j+1]) * x**j
            h =  (h - ord(text[i] * x**(len(pattern)-1) )  * x + hash    
            h = h % p
    return pos



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

