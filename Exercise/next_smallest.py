# Function to print element and NSE pair for all elements of list 
def printNSE(arr): 
  
    for i in range(0, len(arr), 1): 
  
        next = -1
        for j in range(i + 1, len(arr), 1): 
            if arr[i] > arr[j]: 
                next = arr[j] 
                break
              
        print(str(arr[i]) + " -- " + str(next)) 
  
# Driver program to test above function 
arr = [11, 13, 21, 3] 
printNSE(arr) 
  
# This code is contributed by Sunny Karira