# Python 3

def read_input():
    
   try:     
        input_type = input().rstrip()
        if input_type == 'I':           
            pattern = input().rstrip()
            text = input().rstrip()
        elif input_type == 'F':       
            filename = input().rstrip()
            with open(filename) as f:
                pattern = f.readline().rstrip()
                text = f.readline().rstrip()
        else:
            raise ValueError('Invalid input type')

       
        return pattern, text

    except EOFError:
       
        raise ValueError('Not enough input provided')
        
def print_occurrences(output):
    
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    

    
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = hash(pattern)
    text_hash = hash(text[:pattern_len])
    pos = []

    
    for i in range(text_len - pattern_len + 1):   
        if pattern_hash == text_hash:   
            if pattern == text[i:i+pattern_len]:
                pos.append(i)

        
        if i < text_len - pattern_len:
            text_hash = hash(text[i+1:i+1+pattern_len])

    return pos

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
