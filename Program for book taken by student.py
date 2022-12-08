"""This  mini project is created to teach new begineers how to program and
learn about python program """
import numpy as np
import pandas as pd
# FUnctions
def cls(n):
    print ("--"*n)
    
def s():
    print ("-------------------------------------------------------------------------------")


# MAIN
con=True
while con:
    print ("################################################################################")
    print (" ")
    print ("                                 PYTHON TUTORIAL                                ")
    print (" ")
    print ("################################################################################")
    print (" ")
    print (" Welcome to python tutorial!!!!!!!!")
    print ( " ")
    print ("  1. GET STARTED with PYTHON")
    print ("  2. ABOUT PYTHON AND PROJECT")
    print ("  3. EXIT")
    try:
        i1=int(input("enter your choice(1-3):"))
    except IOError:
        print (" No Input!")
        print (" ")
        print ("PROGRAM WILL RESTART")
        cls(20)
    if i1==1:
        con2=True
        while con2:
            cls(20)
            print (" Lets start with python")
            print ("Choose anyone of the module to start")
            cls(20)
            print (" 1. Working with Srings")
            print (" 2. Simple Input and Output Statements")
            print (" 3. Python Functions and Modules")
            print (" 4. Loops in Python")
            print (" 5. Data Types and Usage")
            print (" 6. Working on Series")
            print (" 7. Working on DataFrame")
            print (" 8. Working on CSV files")
            print (" 9. Working on Graphs(Visualization)")
            print ("10. Get back to main menu")
            try:
                i2=int(input("Enter your choice(1-10): "))
            except IOError:
                print (" No input given")
            
#WORKING ON STRINGS
                
            if i2==1: 
                con3=True
                while con3:
                    cls(20)
                    s()
                    print ("Strings :-A data type are any number of valid characters into a set of quotion marks.")
                    print ("Operations that can be performed with string are::")
                    print ("1.Traversing of string")
                    print ("2.String opeartors  on string")
                    print ("3.String Functions")
                    print ("4.Slicing a string")
                    print ("5.Get Back to previous menu")
                    try:
                        i3=int(input("Enter your choice(1-5):"))
                    except IOError:
                        print ("No input given")
                    if i3==1:
                        print ("Traversing can be performed in a following way")
                        a="Python"
                        print (">>>a='Python'")
                        print (">>>for i in a:")
                        print ("      print i,end='\t'" )
                        print ("_______________")
                        for i in a :
                            print (i,end="\t")
                        print('\n')
                        print (" *** ")
                        input("Press Enter to Continue") 
                    
                    elif i3==2:
                        print ("String operators are")
                        print ("1.String Concatenation operator (+):")
                        print ("  eg.")
                        print ("     'ram' + 'shayam'")
                        print ("  will result into")
                        print ("     'ramshayam' ")
                        print ("2. String replication operator  (*):")
                        print ("  eg.")
                        print ("     'DSS'*3")
                        print ("  will result into) ")
                        print ("     'DSSDSSDSS'")
                        print ("3. Mermbership operator:")
                        print ("in : Returns True if sub string  exist in given string, otherwise False")
                        print ("not in: Returns True if sub string   not exist in given string, oterwise False")
                        print (" eg.")
                        print ("   >>> 'a' in 'ram'")
                        print ("       True")
                        print ("   >>> 'a' not in 'ram'")
                        print ("4.Comparison operator(<,>,>=,<=,==,!=):")
                        print (" eg.")
                        print ("   'a'=='a' will give True")
                        print ("   \'a\'==\"a\" will give False")
                        input("Press Enter to Continue")
                    elif i3==3:
                        q=open("S_FUN.txt")
                        w=q.read()
                        print (w)
                        del q,w
                        input("Press Enter to Continue")
                    elif i3==4:
                        cls(20)
                        print ("Slicing a string can be performed  as follow,")
                        print ("")
                        print (">>a=ramayan")
                        a='ramayan'
                        print (">>>print a[0:3]")
                        print ("  ",a[0:3])
                        input("Press Enter to Continue")
                    elif i3==5:
                        con3=False
                    else:
                        print ("INvalid input !!!!!!!!!!!")
            
            elif i2==2:   #Simple I/O Statement
                print ("Smple input and output statement can be given bu using")
                print ("1. For input :")
                print ("  1.input() and")
                print ("  2.raw_input()")
                print ("  Following are sample programs to illustrate")
                print ("    eg.")
                print ("       >>> a=raw_input('Enter your  number:' )")
                print ("           Enter your number: 25")
                cls(20)
                print ("2.For output Python use 'print' key word")
                print ("")
                print (">>>For i in 'Python':")
                print ("      print i    ")        # print is output keyword
                print ("   Output will be as")
                print ("   P \n   y\n   t\n   h\n   o\n    n\n")
                input("Press Enter to continue...")
            elif i2==3: # FUNctions and modules
                 con4=True
                 while con4:                 
                     print ("Python offers 3 type of Functions")
                     print ("1.In-built functions")
                     print ("2.Function defined in Modules")
                     print ("3.User  defined functions")
                     print ("4.Get back to previous menu")
                     try:
                         i4=input(" Enter your choice(1-4):")
                     except IOError:
                         print ("No input provided")
                     if i4==1:
                        print ("Python offers some builtin functions which are always availabel to use")
                        print (" eg. len(),type(),int()")
                        cls(20)
                        print (">>> a=Python")
                        print (">>>len(a)")
                        print ("   6")
                        input("Press Enter to continue...")
                     elif i4==2:
                         q=open("M_FUN.txt")
                         w=q.read()
                         print (w)
                         q.close()
                         del q,w
                         input("Press Enter to continue...")
                     elif i4==3:
                         print ("These are the functions defined by programmer.And can be defined using 'def' keyword. ")
                         print ("How to create a function is illustrated in following eample")
                         print()
                         print ("def sum(x,y):")
                         print ("    r= x+y")
                         print ("    return r")
                         print ("a=input('Enter number1:')")
                         print ("b=input('Enter number 2:)")
                         print ("c=sum(a,b)")
                         print ("print c")
                         input("Press Enter to continue...")
                     elif i4==4:
                         con4=False       
                     else:
                        print ("Invalid in put")
            elif i2==4:
                con5=True
                while con5:
                    print ("Python offers  2  type of loop statement")
                    print ("1. The for loop")
                    print ("2. The while loop")
                    print ("3. Get back to previous menu")
                    try:
                        i4=int(input("Enter your choice(1-3):"))
                    except IOError:
                        print ("No input provided ")
                    if i4==1:
                        print ("The general form of 'for loop' is as given below:")
                        print (" for <variable> in <sequence> :")
                        print ("     statements_to_repeat")
                        cls(20)
                        print ("eg.")
                        print ("    for element in [10,15,20,25]:")
                        print ("        print (element +2),")
                        print ("Or for loop can be also used wiht range()function")
                        print ("eg.")
                        print ("   for val in range(3,10):")
                        print ("      print val")
                    elif i4==2:
                        print ("The general form of while loop is given below")
                        print (" while <logicalExpression>:")
                        print ("    loop-body")
                    elif i4==3:
                        con5=False
                    else:
                        print ("Invalid Input")
            
            elif i2==5:
                con6=True
                while con6:
                    print ("Python offers  following data types")
                    print ("1. int & float")
                    print ("2. Mutable & ImMutable")
                    print ("3. Get back to previous menu")
                    try:
                        i5=int(input("Enter your choice(1-3):"))
                    except IOError:
                        print ("No input provided ")
                    if i5==1:
                        print ("Integers are for non fractional values\n")
                        print ("whereas floats are for fractional values\n:")
                        cls(20)
                        print ("eg.")
                        print ("  a=75")
                        print ("        print type(a) will generate output as :")
                        print ("type <int>")
                        print ("eg.")
                        print ("   b=75.8:")
                        print ("      print type(b) will generate output as :")
                        print ("type <float>")
                    elif i5==2:
                        print ("Mutable maens data/size can be changed whereas;\n")
                        print ("ImMutable maens data/size cannot be changed")
                    elif i5==3:
                        con6=False
                    else:
                        print ("Invalid Input")
                    
            elif i2==6:
                con7=True
                while con7:
                    print ("___________________ Working On Series__________________")
                    print ("1. Basics Of Series")
                    print ("2. Slicing")
                    print ("3.Return to previious menu")
                    try:
                        i6=int(input("Enter your choice(1-3):"))
                    except IOError:
                        print( "Input error")
                    if i6==1:
                        #data=np.array([7,5,np.nan,67])
                        print("Creation & Basics of series")
                        data=np.array([7,5,45,67])
                        print(data)
                        s=pd.Series(data,dtype = np.int16)
                        print (s) 
                        print(s.ndim) 
                        print (s.itemsize, "Bytes") 
                        print (s.size) 
                        print (s.nbytes)       
                        print (s.hasnans) 
                        print (len(s))          #With NaNs 
                        print(s.count())        #Without NaNs
                        data=np.array([7,5,45,67])
                        s=pd.Series(data,index=[10,20,30,40]);
                        print (s)
                        input("Press Enter to continue...")
                    elif i6==2:
                        s=pd.Series([1,5,7,4],index=[10,20,30,40])
                        print(s[s>5])
                        #Slicing
                        print (s[20])
                        print (s[[10,30]])
                        print (s[10],s[30])
                        print (s[:3])
                        print (s[2:])
                        print (s[10:30])              #Empty Series
                        print (s[1:7])                 #All emements from 1 onwards    
                        print (s[:-2])             
                        print (s[-2:])
                        print (s)
                        print (s.values)
                        print (s.head(2))
                        print (s.tail(1))
                        print( " ")
                        input("Press Enter to continue...")
                    elif i6==3:
                        con7=False
                    else:
                        print ("Invalid input")
                    
            elif i2==7:
                con8=True
                while con8:
                    print( "1.Basics of DataFrame")
                    print( "2.Operations & Slcing")
                    print( "3.Return to previous menu")
                    try:
                        i7=int(input("Enter your choice(1-3)"))
                    except IOError:
                        print ("Input error")
                    if i7==1:
                       data=[["sachin",20],["virat",50],["dhoni",30]]
                       df=pd.DataFrame(data)
                       df=pd.DataFrame(data,columns=['player','matches'])
                       df=pd.DataFrame(data,columns=['player','matches'],
                                   index=["Gen1","Gen2","Gen3"])
                       print (df)
                       print (df.ndim)
                       
                    elif i7==2:
                       data=[["sachin",20],["virat",50],["dhoni",30]]
                       df=pd.DataFrame(data)
                       df=pd.DataFrame(data,columns=['player','matches'],index=["Gen1","Gen2","Gen3"])
                       print (df)
                       #print (df[2:4])1
                       print (df.iloc[0:2])
                       #print (df.loc[0:4])
                       #print (df.iloc[2:4,0:2])
                    elif i7==3:
                        con8=False
                    else:
                        print ("Invalid Input")
            elif i2==10:
                con2=False
            else:
                print(" Invalid input!")
    elif i1==2:
        cls(20)
        a=open("ABOUT.txt")
        b=a.read()
        a.close()
        print( b)
        del a,b
        cls(20)
        print ("*****************************************************************")
    elif i1==3:
        con=False
        print( "Thank u for using program")
    else:
        print(" ")
        print( " INVALID INPUT !!!!")
        print(  " ")
        print( "PROGRAM WILL RESTART")
        for i in range (10000):
            a=i
        del a
        

