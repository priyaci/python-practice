'''
Series of questions from Strivers DSA
Ref - https://github.com/kunal-kushwaha/DSA-Bootcamp-Java/blob/main/assignments/09-patterns.md
Ref youtube - https://www.youtube.com/watch?v=lsOOs5J8ycw
https://www.youtube.com/watch?v=tNm_NNSB3_w
'''
def pattern1():
    '''
    *
    * *
    * * *
    * * * *
    * * * * *
    '''
    n =5
    for row in range(0,n):
        for col in range(0,row+1):
            print("* ",end="")
        print("\r")


def pattern2():
    '''
    *****
    ****
    ***
    **
    *
    '''
    n = 5
    for row in range(0,n):
        for col in range(n,row,-1):
            # for col in range(0,n-r):
            print("* ", end = "")
        print("\r")


def pattern3():
    '''
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    '''
    n = 5
    for row in range(1,n+1):
        for col in range(1,row+1):
            # for col in range(0,n-r):
            print(str(col) +" ", end = "")
        print("\r")

def pattern4():
    '''
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
    '''
    n = 5
    for row in range(0,n*2):
        if(row<=n):
            for col in range(0,row+1):
                print("* ", end="")
        else :
            for col in range(0,n*2-row):
                print("* ", end="")
        print("\r")


def pattern5():
    '''
         *
        **
       ***
      ****
     *****
    '''
    n = 5
    for row in range(0,n):
        for col in range (0,n+1):
            if(col>=n-row):
                print("*", end = "")
            else:
                print(" ", end ="")
            
        print("\r")

def pattern6():
    '''
    *****
    ****
    ***
    **
    *
    '''
    n = 5
    for row in range(0,n+1):
        for col in range (0,n+1):
            if(col<=n-row):
                print("*", end = "")
            else:
                print(" ", end ="")
            
        print("\r")

def pattern7():
    '''
        *
       ***
      *****
     *******
    *********
    '''
    n = 4
    # number of spaces
    k = n
 
    # outer loop to handle number of rows
    for row in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for colSp in range(0, 2*k -1):
            print(" ", end="")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for colStr in range(0, 2*row+1):
         
            # printing stars
            print("* ", end="")
     
        # ending line after each row
        print("\r")
 

def pattern8():
    '''
    *********
     *******
      *****
       ***
        *

    '''
    n = 5
    k = n
    for row in range(0,n):
        for colSp in range(0,2*row+1):
            print(" ", end="")
        for colStr in range(0, 2*k -1):
            print("* ", end = "")
        k = k-1
            
        print("\r")

def pattern9():
    '''
         *
        * *
       * * *
      * * * *
     * * * * *


    '''
    n = 5
    k = n
    for row in range(0,n):
        for colSp in range(0,k-1):
            print(" ", end="")
        for colStr in range(0, row +1):
            print("* ", end = "")
        k = k-1
            
        print("\r")


def pattern10():
    '''
    * * * * *
     * * * *
      * * *
       * *
        *
    '''
    n =5
    k =n
    for row in range(0,n):
        for colSp in range(0,row):
            print(" ", end = "")
        for colStr in range(0,k):
            print("* ", end="")
        k = k-1
        print("\r")



def pattern11():
    '''
    * * * * *
      * * * *
       * * *
        * *
         *
         *
        * *
       * * *
      * * * *
     * * * * *
    '''
    n = 4
    k =n
    j=n
    
    for row in range(0,n*2):
        if (row<n):
            for colSp in range(0,row):
                print(" ",end="")
            for colStr in range(0,k):
                print("* ",end="")
            k=k-1
        else:
            for colSp in range(0,j-1):
                print(" ",end ="")
            
            for colStr in range(0,row-n+1):
                print("* ",end="")
            j = j-1
        print("\r")


def pattern12():
    '''
         *
        * *
       *   *
      *     *
     *********

    '''
    





    






#pattern1()
#pattern2()
#pattern3()
#pattern4()
#pattern5()
#pattern6()
#pattern7()
#pattern8()
#pattern9()
#pattern10()
#pattern11()
pattern12()





