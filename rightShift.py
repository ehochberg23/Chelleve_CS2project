

def rightShift(text, num ):   
    #rightShift - 
    #text - the word
    #num -number of letters you are removing from the word
   
    cnt = 0                                             #the counter for the while loop
    end= len(text)                                      
    end = end-num                                       
    word = text[0:end]                                  
    
    while cnt < num:                                    #Determining how many hashtags it needs to add to the front so it runs the loop that many times
        
        word = "#" + word                               #Adds the hashtags that removed the letters to the beginning of the word
        cnt +=1
    
    return word                                         #Returns the finished word
    

    