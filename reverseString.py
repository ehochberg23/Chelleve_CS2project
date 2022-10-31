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
    output = ""
    string = text
    before_reverse = text[:position - 1]  # Keeping letters before the reverse letters
    after_reverse = text[position + length - 1:]  # Keeping letters after the reverse letters the same
    for i in range(len(string) - 1, -1, -1):  # Reversing the middle letters
        output = output + string[i]
    position = position + 1
    end = position + length
    output = output[position:end]

    text = before_reverse + output + after_reverse

    return text



    