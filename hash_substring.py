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
    len_1 = len(pattern)
    len_2 = len(text)
    hash_1 = hash(patern)
    hash_2 = hash(text[:len_1])
    s = 1
    for _ in range(len_1 - 1):
        s = (len_1 * base) % prime
        
    pos = []
    for i in range(len_2 - len_1 + 1):
        if hash_1 == hash_2:
            if pattern == text[i:i + len_1]:
                pos.append(i)
        if i < len_2 - len_1:
            hash_2 = ((hash_2 - ord(text[i]) * s) * base + ord(text[i + len_1])) % prime
            hash_2 = (hash_2 + prime) % prime
    return pos    
    
    


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
