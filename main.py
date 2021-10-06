#WRITE YOUR CODE IN THIS FILE
def countA(w):
    y=0
    for i in range(0, len(w)):
        if w[i] == "a":
            y=y+1
    return y 
        
    
print(countA("caat"))