def main():
    
    out = reverseString(3,3, "COMPUTER")
    
    print(out)


def reverseString(position, length, text):
    """
    This function reverses the middle letters based on position and the length
    Arguments:
        position: starting position
        length: length of string being reversed
        text: the string that contains the word being manipulated
    Returns:
        text: A string which is reversed of the part
    """
    before_reverse = text[:position - 1]  # Keeping letters before the reverse letters
    after_reverse = text[position + length - 1:]  # Keeping letters after the reverse letters the same
    output = text.replace(before_reverse, '')  # delete before_reverse from string
    output = output.replace(after_reverse, '')  # delete after_reverse from string
    output = output[::-1]  # reverse resulting string
    text = before_reverse + output + after_reverse  # put everything back together

    return text


    