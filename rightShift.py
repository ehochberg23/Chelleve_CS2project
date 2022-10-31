

def rightShift(num, text):
    """
    Shifts all the characters of the string 'num' places to the right. Delete the rightmost 'num' characters and replace with #'s
    Arguments:
        num: the number of places the string will be shifted to the right
        text: the string being manipulated
    Returns:
        word: the resulting string
    """

    cnt = 0  # the counter for the while loop
    end = len(text)
    end = end - num
    word = text[0:end]

    while cnt < num:  # Determining how many hashtags it needs to add to the front so it runs the loop that many times

        word = "#" + word  # Adds the hashtags that removed the letters to the beginning of the word
        cnt += 1
        text = word
    return text  # Returns the finished word


