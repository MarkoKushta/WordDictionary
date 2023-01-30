
#Main Function
def call(idx, w):

    tmp = ""
    
    for i in range(idx, len(arr)):      # go through the arr
        
        tmp += arr[i]                   # add current char/words to tmp
        
        try:
            
            dictionary[tmp]             # call dictionary
            call(i + 1, w + tmp + " ")  # print(temp, end=" ")
            
        except:
            
            continue    
             
    if idx == len(arr):
        print(w)                        # print all possible combinations


strings = []                            # read input
with open('test.txt') as s:             # rename text file -------------------------------
    
    strings = s.readlines()         

dictionary = {}                         # initialize dictionary and counter
c = 0

for s in strings:                       # loop through the array
                                        
    if c == 0:                          # check counter
        
        size = int(s)
        c += 1
        
        continue
        
    if c== 1:                           # if, 1 remove spaces
        
        c += 1
        arr = s.strip()
        
        continue
        
    dictionary[s.strip()] = 1           # give val 1 to dictionary when string has no spaces
    c += 1

call(0, "")                             # call func
