def chekStatus(a, b, flag):
    if (flag == False and ((a >= 0 and b < 0) or (a < 0 and b >= 0))) or (a < 0 and b < 0 and flag == True):
        return True
    return False
print(chekStatus(5, 3, True))