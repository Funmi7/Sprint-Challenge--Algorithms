'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    # pass
    if len(str(word)) == 1:
        return word
    return count_th(word.count("th"))
    
print(count_th("there"))