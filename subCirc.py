'''
Created on Oct 25, 2022

@author: CCaliboso24
'''
def subCirc(position,length,num,direction,text):

    circ = []                                           #This array will hold the letters that will be circulated and inserted in the final 
    wrd = []                                            #This array will hold all the letters of text

    position = position - 1                             #Position variable takes the position and properly formats the number for arrays by subtracting 1
    trueLength = position + length                      #trueLength takes the length and formats the number in termns of the wrd array
    letters = text[position:trueLength]                 #letters will hold all letters selected to circulate in the form of a string
  
    cnt1 = 0                                            #cnt1 is the counter for the loop "for letter in text"
    for letter in text:
        wrd.append(text[cnt1])
        cnt1 = cnt1 + 1
    
    '''
    This loop appends all letters from text into the wrd array 
    '''
    
    cnt2 = 0                                            #cnt2 is the counter for the loop "while cnt2 < len(letters)"
    while cnt2 < len(letters):
        circ.append(letters[cnt2])
        cnt2 = cnt2 + 1 
        
    ''' 
    This loop appends all selected letters from text to be circulated in the circ array 
    '''
    
    cnt3 = 0                                            #cnt3 is the counter for the loop "while cnt3 < length"                             
    while cnt3 < length:
        newPlace = position + num + cnt3
        if newPlace >= (length + num):                  #newPlace is the new index for the circulated letters
            while newPlace > length:
                newPlace = newPlace - length
        char = circ[cnt3]                               #char represents the each letter from circ as they are being reinserted
        wrd[newPlace] = char
        cnt3 = cnt3 + 1
        
    '''
    This loop finds the correct circulated spot for the letters selected to be circulated, 
    Then it inserts the letters in their new place
    '''    
        
    finalWord = "".join(wrd)
    print(finalWord)

    
