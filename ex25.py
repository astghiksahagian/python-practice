#in this lesson, we ran the below functions directly in python in the terminal. We did this by using the following text:
    # import ex25 
        #(shortcut = from ex35 import *)
        #this will streamline the process of not having to add ex25.function_name() for every call. We can just write down function function_name()
    # sentence = "All good things come to those who wait."
    # words = ex25.break_words(sentence)
    # words 
        #note: the above prints any variable or function without having to write print(), as long as the function returns something or specifically has a print statement inside of it
    # ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']



def break_words(stuff):
    """This function will break up words for us."""
        #the 3 double quote surrounded sentence above is called a documentation comment. This helps list out what each function does when we use the help() function inside the terminal ---> help(ex25.break_words) = This function will break up words for us.
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


