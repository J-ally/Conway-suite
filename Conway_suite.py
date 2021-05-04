"""
In mathematics, the look-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ... (sequence A005150 in the OEIS).
To generate a member of the sequence from the previous member, read off the digits of the previous member, 
counting the number of digits in groups of the same digit. For example:

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.
    1211 is read off as "one 1, one 2, then two 1s" or 111221.
    111221 is read off as "three 1s, two 2s, then one 1" or 312211.
"""

def cut_list (n) :   
    """
    take  a list as argument and cut it in chunks of the same number
    ex : [1,1,3,3,3] returns [ [1,1],[3,3,3] ]
    """
    L = []
    index = 0
    for i in range (len (n)-1) :
        if n[i] != n[i+1] : 
            L.append (n[index:i+1])
            index = i+1
    L.append (n[index :])      #adds the remaining part of the list
    return L
    
def assemblage (n) :     
    F = []
    C = cut_list (n)
    for i in range (len (C)) :
        F += [ len(C[i]) ] + [ C[i][0] ]
    return (F)
    
def suite_conway (x) :
    A = [1]             #initialises the suite
    print ("Assemblage of rank 1 = ",A ,"\n")
    for e in range (x-1) :
        A = assemblage (A)
        print ("Assemblage of rank ",e+2," = ",A,"\n")
    return
    
print (suite_conway (14))