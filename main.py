def close10(x,y):
    if abs(x - 10) < abs (y - 10):
        return x
    elif abs(x-10) == abs(y-10):
        return "0"
    else:
        return y

print (close10(5,15))