#Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

def solution(text, ending):
    if text.find(ending) > 0 and text[-1] == ending[-1] or text == ending:
        return True
    else:
        return False