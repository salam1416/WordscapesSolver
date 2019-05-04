
import string
# this file is aimed to find you the needed vocabularies for Workscapes game

def open_file():
    """
    Ask for file name and make sure this file exists
    Open file for reading
    """
    fp = open('dictionary.txt', 'r')
    return fp

    
def create_dict(fd):
    """
    This function takes the openned file pointer from open_file(), it creates a dictionary. 
    Keys are letters positions in each word in the file; 
    Values are words associated with each key
    Return: full_dict. completion dictionary words for each letter and position
    """
    # initialize an empty dictionary
    full_dict = {}
    # loop through file
    for line in fd:
        # lowercase everything in line, then split line into a list
        line = line.lower().split()
        # loop through elements in the list of words in the splitted line
        for word in line:
            # strip words from puncuation using string module
            word = word.strip(string.punctuation)
            # if words contains only alphabatic characters and of length > 1
            if word.isalpha() and len(word)!= 1:
                if len(word) in full_dict:
                    full_dict[len(word)].add(word)
                else:
                    full_dict[len(word)] = set()
                    full_dict[len(word)].add(word)
    return full_dict

def check_letters(word, char_list, n):
    lst = []
    for char in char_list:
        if word.count(char) > 0:
            lst.append(1)
    if sum(lst) >= n:
        return True
    else:
        return False

def find_words(full_dict):
    word_set = set()
    number_of_letters = int(input('how many letters? '))
    contains = input('what letters do you have? ')
    contains = contains.split()
    for word in full_dict[number_of_letters]:
        if check_letters(word, contains, number_of_letters) == True:
            word_set.add(word)
    #print(full_dict[number_of_letters])
    return word_set

    
def main():
    """ This main function is used to organize the code and eliminate global variable """
    # call open_file() to get file pointer 
    fd = open_file()
    # call fill completion to get dict, then close the openned file
    full_set = create_dict(fd)
    wrds = find_words(full_set)
    print(wrds)
    fd.close()
    # ask for a prefix in while loop

        
# call the main function to do the magic, lool :)
main()
