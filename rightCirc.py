def rightCirc(num, text):
    circ = text[:num]
    text = text[num:]
    text = text + circ
    print(text)


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

    return text


if __name__ == "__main__":
    main()