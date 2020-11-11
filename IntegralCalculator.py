
class IC:
    def __init__(self, func):
        self.func = func
    
    def simpson(self, n, a, b):
        if(n % 2 != 0):
            return float('inf')
        
        delta = (b-a)/n
        ret = 0
        ret += self.func(a) + self.func(b)
        flip = True
        for i in range(n-2):
            if flip:
                ret += 4 * self.func(a+delta * (i+1))
            else:
                ret += 2 * self.func(a + delta * (i+1))
            flip = not flip
        ret += 4 * self.func(b-delta)
        return ret * delta / 3
        
    def trapezoidal(self, n, a, b):
        delta = (b-a)/n
        ret = 0
        ret += self.func(a) + self.func(b)
        for i in range(n-1):
            ret += 2 * self.func(a + delta * (i+1))
        return ret * delta / 2
        
    def midpoint(self, n, a, b):
        delta = (b-a)/n
        ret = 0
        for i in range(n):
            ret += self.func(a + delta * i + delta / 2)
        return ret * delta
        
    def left(self, n, a, b):
        delta = (b-a)/n
        ret = 0
        for i in range(n):
            ret += self.func(a + delta * i)
        return ret * delta
        
    def right(self, n, a, b):
        delta = (b-a)/n
        ret = 0
        for i in range(n):
            ret += self.func(a + delta * (i+1))
        return ret * delta
        
def test(func, n, a, b):
    ic = IC(func)
    res = ic.simpson(n, a, b)
    print("simpson : {}, {} - {} : {}".format(n, a, b, res))
    
    res = ic.trapezoidal(n, a, b)
    print("trapezoidal : {}, {} - {} : {}".format(n, a, b, res))
    
    res = ic.midpoint(n, a, b)
    print("midpoint : {}, {} - {} : {}".format(n, a, b, res))
    
    res = ic.left(n, a, b)
    print("left : {}, {} - {} : {}".format(n, a, b, res))
    
    res = ic.right(n, a, b)
    print("right : {}, {} - {} : {}".format(n, a, b, res))