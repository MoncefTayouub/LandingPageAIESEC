



def FixdateForma(strg):
    arr = strg.split('/')
    arr.reverse()
    return '-'.join(arr)

def str_bool (value):
    if (value == 'true' or value == '1'):
        return True
    elif (value == 'false' or value == '0') :
        return False
