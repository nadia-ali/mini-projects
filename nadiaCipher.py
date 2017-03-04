import os





def write_content(filename, input_content):
    """
        This function takes in filename and content, and writes the content to the file.
        New file is created if the filenames does not already exist. 

        params
        filename : string, complete path to the output file  
        input_content : string, content that goes into the given file name  
    """
    there = os.path.isfile(filename)
    
    if there: #if the file is there 
        pointer = open(filename, "r+")
        old_content = pointer.read()
        new_content = old_content + input_content
        pointer.write(new_content)
        pointer.close()
    
    else:     #if the file is not there 
        pointer = open(filename, "w")
        pointer.write(input_content)
        pointer.close()
        
        
def decipher(text, shift_key):
    order = ord(text.lower())
    deciphered_code = order + shift_key 
    deciphered_code = chr(deciphered_code)
    return deciphered_code


def MI6(cipher):
    
    for shift_key in range(1, 10, 1):
        output= ""
        for letter in cipher:
            if letter == " ":
                output = output + letter
            else:
                 output = output + decipher(letter,(shift_key*-1))
            
        f_name = "mi6_op/ceasar_{}".format(shift_key)
        write_content(filename = f_name, input_content = output)
        
    
if __name__ == "__main__" :
    cipher = input("Enter the cipher here: ")
    MI6(cipher)
        
        

    
    
    

    

    
 
