
'''
Created on Oct 13, 2022

@author: CCaliboso24
'''


def leftShift(num, text):
    """
    Shifts all the characters of the string 'num' places to the left. Delete the leftmost 'num' characters and replace with #'s
    Arguments:
        num: the number of places the string will be shifted to the left
        text: the string that contains the word being manipulated
    Returns:
        finalWord: the resulting string
    """

    wrd = []  # wrd array will hold all letters of a word separate

    cnt1 = 0  # cnt1 is the counter for the while loop (while (cnt1 < len(word))
    while cnt1 < len(text):
        char = text[cnt1]
        wrd.append(char)
        cnt1 = cnt1 + 1

    # This while loop places all characters in the word into the wrd array

    cnt2 = 0  # cnt2 is the counter for the while loop (while (cnt2 < num)
    while (cnt2 < num):
        wrd.pop(0)
        cnt2 = cnt2 + 1

    # This while loop deletes the specific amount of characters that are pushed out of the array

    cnt3 = 0  # cnt3 is the counter for the while loop (while (cnt3 < num)
    while (cnt3 < num):
        wrd.append("#")
        cnt3 = cnt3 + 1
    '''
    This while loop appends the specific amount of # at the end  
    '''

    text = "".join(wrd)  # finalWord is the wrd array converted to a string
    return text


def main():

    data = "LS-1/OHIO"

    data = data.split("/")
    data_num = len(data)

    text = data[-1]

    count = 0
    while count < data_num:
        command = data[count]
        command = command.split("-")
        function = command[0]

        if function == "LS":
            num = int(command[-1])
            text = leftShift(num, text)


        count = count + 1

    return text


if __name__ == "__main__":
    main()