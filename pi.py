import re 

if __name__ == "__main__":
    bday = "199546"
    file_name = "pi.txt"
    read_mode = "r" 
    
    pointer = open(file_name, read_mode)
    pi = pointer.read()
    occurence = re.findall(bday, pi)
    
    if len(occurence) > 0:
        index = pi.find(bday)
        index = index - 2
        print (index )
	
    else:
        print ("Sorry, we could not find your birthday in the first billion digits of pi")
   							
