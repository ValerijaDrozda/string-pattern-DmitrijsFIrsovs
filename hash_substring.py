# python3

def read_input():
    input_in = input().strip()
    if input_in == 'F':
        with open ('input.txt', 'r') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        pattern = input().strip()
        text = input().strip()
    
    return pattern , text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 1000000007
    x =263
    len_1 = len(pattern)
    len_2 = len(text)
    hash_pattern = poly_hash(pattern, p, x)
    base = pow(x, len_1 - 1, p)
    hash_values = [None] * (len_2 - len_1 +1)
    hash_values[-1] = poly_hash(text[len_2 - len_1:], p , x)
    
    for i in range (len_2 - len_1 - 1, -1, -1):
        hash_values[i] = (x * hash_values[i+1] + ord(text[i]) -ord(text[i+len_1] * base)) % p
    pos = []
    
    for i in range (len_2 - len_1 +1):
        if hash_pattern != hash_values[i]:
            continue
        if text[i:i+len_1] == pattern:
            pos.append(i)
    return pos

def poly_hash(s, p, x):
    hash_value =0
    for i in range(len(s)-1, -1, -1):
        hash_value = (hash_value * x + ord(s[i])) % p
    return hash_value

    
    
    
    


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
