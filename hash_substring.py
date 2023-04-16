# Python 3

def read_input():
   input_type = input().strip()
    if input_type == 'I':
        return input().strip(), input().strip()
    elif input_type == 'F':
        with open(input().strip()) as f:
            return f.readline().strip(), input().strip()

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
            if pattern == text[i:i + pattern_len]:
                pos.append(i)

        if i < text_len - pattern_len:
            text_hash = hash(text[i + 1:i + 1 + pattern_len])

    return pos


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
   
