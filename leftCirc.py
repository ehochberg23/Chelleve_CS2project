def leftCirc(num, text):
    
    circ = text[num:]
    text = text[:num]
    text = circ + text
    return text


def main():
    
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
            
        elif function == "RS":
            num = int(command[-1])
            text = rightShift(num, text)
            
        elif function == "LC":
            num = int(command[-1])
            text = leftCirc(num, text)
            
        elif function == "RC":
            num = int(command[-1])
            text = rightCirc(num, text) 
            
        elif function == "MC":
            func_commands = command[-1]
            position = int(func_commands[-1])
            length = int(func_commands[-2])
            num = int(func_commands[-3])
            direction = str(func_commands[-4])
            text = subCirc(position, length, num, direction, text)
        
        elif function == "REV":
            func_commands = command[-1]
            position = int(func_commands[-1])
            length = int(func_commands[-2])
            text = rev(position, length, text)
              
        count = count + 1
        
    return text
    
if __name__ == "__main__":
    main()