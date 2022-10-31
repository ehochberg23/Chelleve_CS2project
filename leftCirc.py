def leftCirc(num, text):
    """
    Circulates the leftmost 'num' characters to the right hand side of the string
    Arguments:
        num: the number of characters being moved to the right hand side
        text: the string that contains the word being manipulated
    Returns:
        text: the resulting string
    """
    circ = text[num:]                       #all the characters 'num' and after
    text = text[:num]                       #all the characters before 'num'
    text = circ + text                      #resulting string
    return text



def main():
    data = "LC-3/COMPUTER"
    data = data.split("/")
    data_num = len(data)
    
    text = data[-1]
    
    count = 0
    while count < data_num:
        command = data[count]
        command = command.split("-")
        function = command[0]
        

            
        if function == "LC":
            num = int(command[-1])
            text = leftCirc(num, text)
            

              
        count = count + 1
        
    print(text)
    
if __name__ == "__main__":
    main()