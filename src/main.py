def outer_f(x,y):
    def inner_f():
        return x**y
    return inner_f

if __name__=="__main__":
    x = 3
    y = 4
    a = outer_f(x,y)
    print(a())