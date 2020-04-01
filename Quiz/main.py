#import country
import state

values = 0
def process_file(file, austria): # This is the process_file function. 
 	oldfile = open(austria.txt, "r+") # This reads the file. 
 	newfile = open(austria2.txt, "w") #This writes to the new file 

 	newfile.write("State, Population, \n") # This creates the headers to the new file 

for line in oldfile:
 	 values = (line.strip().split(',')) # This strips the comma. 
 	 print(values[0], values[1]) # This prints the two values 
 	 newfile.write(newline+"\n")

def main():
    austria = country.Country("Austria")
    process_file("austria.txt", austria)
    print("Information about", austria.get_name(), "\n")
    print(austria)
    print("Total Population:", austria.estimate_population())
    
main()  