from _operator import length_hint

def rightShift(text,num ):   
    
   
    
    end= len(text)
    end = end-3
    word = text[0:end]
    
    print(word) 
    
    cnt = 0
    while cnt <length_hint
    data= "#" + data 
    
    
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
            num = command[-1]
            leftShift(num, text)
            
        elif function == "RS":
            num = command[-1]
            rightShift(num, text)
            
        elif function == "LC":
            num = command[-1]
            leftCirc(num, text)
            
        elif function == "RC":
            num = command[-1]
            rightCirc(num, text) 
            
        elif function == "SC":
            func_commands = command[-1]
            num1 = func_command[-1]
            num2 = func_command[-2]
            num3 = func_command[-3]
            num4 = func_command[-4]
            subCirc(num1, num2, num3, num4, text)
        
        elif function == "REV":
            func_command = command[-1]
            num1 = func_command[-1]
            num2 = func_command[-2]
            rev(num1, num2, text)
              
        count = count + 1
        
    return text
    
if __name__ == "__main__":
    main()