# python3

def read_input():
    input_type = input().rstrip()  
    if input_type == 'i':
        
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'f':
       
        file_name = input().rstrip()
        with open(file_name, 'r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    else:
        raise ValueError("Invalid input type")

    return pattern, text
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = len(pattern)
    t = len(text)
    p_hash = hash(pattern)
    t_hash = hash(text[:p])
    result = []

    for i in range(t - p + 1):
        if p_hash == t_hash and text[i:i+p] == pattern:
            result.append(i)
        if i < t - p:
            t_hash = hash(text[i+1:i+p+1])
    return result
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
   


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
