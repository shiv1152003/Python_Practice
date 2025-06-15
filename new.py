# for i in  range(12):
#     if (i == 10):
#         print("Skip the iteration")
#         continue
#     print("5 X", i , "=", 5 * i)
   
# i = 0    
# while True:
#     print(i)
#     i = i + 1
#     if (i % 100 == 0):
#         break


def calculateGmean(a, b):
    mean = ( a * b ) / ( a + b)
    print(mean)
    

def isGreater(a, b):
    if ( a > b ):
        print(f"{a} is Greater than {b}")
    else:
        print(f"{b} is Greater than {a}")
     
a = 9
b = 8
# gmean = (a*b)/(a+b)
# print(gmean)

calculateGmean( a , b )
isGreater(a,b)


c = 8 
d = 7
# gmean2 = (c*d)/(c+d)
# print(gmean2)
calculateGmean( c , d )
isGreater(c, d)