def rightCirc(num, text):
    """
    Circulates the rightmost 'num' characters to the left hand side of the string
    Arguments:
        num: the number of characters being moved to the left hand side
        text: the string that contains the word being manipulated
    Returns:
        text: the resulting string
    """
    num = len(text)-num
    circ = text[:num]                     #all the characters before 'num'
    text = text[num:]                     #all the characters 'num' and after
    text = text + circ                   #resulting string
    return text



def main():
    data = "RC-3/COMPUTER"
    data = data.split("/")
    data_num = len(data)

    text = data[-1]

    count = 0
    while count < data_num:
        command = data[count]
        command = command.split("-")
        function = command[0]

        if function == "RC":
            num = int(command[-1])
            text = rightCirc(num, text)

        count = count + 1

    print(text)


if __name__ == "__main__":
    main()