# python3

def read_input():
    a = input().rstrip().upper()
   
    
    if a == "I":
        pattern = input().rstrip()
        text = input().rstrip()
        
            
    elif a == "F":
        with open("input.txt", "r") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
        
    return pattern , text

def print_occurrences(output):
  
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 10**9 +7
    x = 26
    g = 0
    h =0
    
   
    
    for  i in range(len(pattern):
        g = (g * x + ord(pattern[i])) % p
        h = (h * x + ord(text[i])) % p
                    
    x_pow = pow(x, len(pattern), p) 
                    
    pos = []                
        
        
    if g == h:
        if pattern == text[:len(pattern)]:      
            pos.append(0)
    
    for i in range(1, len(text), len(pattern) + 1):
        h = ((h - ord(text[i - 1]) * x_pow) * x + ord(text[i+len(pattern) - 1])) % p
        
        if g == h:
            if pattern == text[i:i + len(pattern)]:
                    
                pos.append(i)
            
    
    return pos



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

