def rightShift(num, text):
    # rightShift -
    # text - the word
    # num -number of letters you are removing from the word


    cnt = 0  # the counter for the while loop
    end = len(text)
    end = end - num
    word = text[0:end]

    while cnt < num:  # Determining how many hashtags it needs to add to the front so it runs the loop that many times

        word = "#" + word  # Adds the hashtags that removed the letters to the beginning of the word
        cnt += 1

    print(word)  # Returns the finished word


def main():

    data = "RS-3/COMPUTER"

    data = data.split("/")
    data_num = len(data)

    text = data[-1]

    count = 0
    while count < data_num:
        command = data[count]
        command = command.split("-")
        function = command[0]

        if function == "RS":
            num = int(command[-1])
            text = rightShift(num, text)


        count = count + 1

    return text


if __name__ == "__main__":
    main()


