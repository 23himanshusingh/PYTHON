'''Sorting the Keys and Values in Alphabetical Order using the Key'''

# function calling
def dictionairy():
 
 # Declaring the hash function     
 key_value ={}   
  
# Initialize value
 key_value[2] = 56      
 key_value[1] = 2
 key_value[5] = 12
 key_value[4] = 24
 key_value[6] = 18     
 key_value[3] = 323
  
 print ("Task 2:-\nKeys and Values sorted in",
            "alphabetical order by the key  ") 
 
 # sorted(key_value) returns an iterator over the
 # Dictionary’s value sorted in keys. 
 for i in sorted (key_value) :
    print ((i, key_value[i]), end =" ")



