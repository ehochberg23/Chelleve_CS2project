
def rightShift(text,num):

    end= len(text)
    end = end-num
    word = text[0:end]
    
    print(word) 
    
    cnt = 0
    while cnt < length_hint
    data = "#" + data
    
    
def main():

    data = "RS-1/OHIO"

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