import os

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
    except EOFError:
        print("Error: No input provided.")
        pattern = ''
        text = ''
        
    return pattern, text

def get_occurrences(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = hash(pattern)
    text_hash = hash(text[:pattern_len])
    pos = []

    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i + pattern_len]:
                pos.append(i)

        if i < text_len - pattern_len:
            text_hash = hash(text[i + 1:i + 1 + pattern_len])

    return pos

if __name__ == '__main__':
    pattern, text = read_input()
    pos = get_occurrences(pattern, text)
    output_str = ' '.join(map(str, pos))
    print(output_str)
    
    # Write output to environment file
    with open(os.environ['GITHUB_ENV'], 'a') as f:
        f.write(f'OUTPUT_STRING={output_str}\n')
   
