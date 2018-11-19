import random
import matplotlib.pyplot as plt

def hello_world():
    print('Hello, World!\n')
    
def draw_stars(n):
    return ('*' * n)

def fib(n):
    assert n >= 0
    return n if n < 2 else fib(n-1) + fib(n-2)

def gcd(m,n):
    return m if (n == 0) else gcd(n, m % n)

def ratings():
    courses = ['Python for Quants'
           , 'Monte Carlo Methods'
           , 'Financial Engineering for Pedestrians'
           , 'LIBOR/SABR Pricing Models'
           , 'Advanced Financial Engineering'
           , 'Least Square Monte Carlo Methods...'
           ]

    ratings = "5 4 3 2 1".split()
    print('\nPRINTING COURSE RATINGS...\n')
    for course in courses:
        if course == 'Python for Quants':
            print('[| {ratings:5s} |]. {course_title}'.format(ratings= draw_stars(5), course_title = course))
        else:
            print('[| {ratings:5s} |]. {course_title}'.format(ratings= draw_stars(int(random.choice(ratings))), course_title = course))
            
def lowest_divisor(n):
    def iter(n,d): return d if n%d == 0 else iter(n, d+2)
    if n <= 1: return n
    elif n % 2 == 0: return 2
    else: return iter(n,3)

def add(*args):
    return sum(args)

def multifns(**args):
    try:
        if args['op'] == '+':
            return sum(args['vals'])
        else:
            raise NotImplementedError
    except NotImplementedError:
        print('Implementation left as exercise')

def egcd(a, b):
    assert a > 0, "condition (a >= 0) is violated"
    assert b > 0, "condition (b >= 0) is violated"
    def iter(a, b, mat):
        [(u,v), (w,x)] = mat
        if (a > 0) and (b > 0):
            if (a >= b):
                (q, a) = divmod(a, b)
                return iter(a, b, [(u-q*w, v-q*x), (w, x)])
            else:
                return iter(b, a, [(w, x), (u, v)])
        elif (b == 0):
            return (a, (u, v))
        else:
            return (b, (w, x))
    return iter(a,b, [(1, 0), (0, 1)])   

def dot_product(xs,ys):
    assert len(xs) == len(ys), "length mismatch"
    sum = 0
    for (x,y) in zip(xs,ys):
        sum += x*y
    return sum

def make_dna(len):
    codons = list('ACTG')
    return ''.join([random.choice(codons) for _ in range(len)])

def count_codons(strand):
    dict = {}
    for base in strand:
        try:
            dict[base] += 1
        except KeyError:
            dict[base] = 1
    return dict

def memoise(fn):
    dict = {}
    def iter(*args):
        try:
            return dict[args]
        except KeyError:
            dict[args] = val = fn(*args)
            return val
    return iter

def traceit(fn):
    def iter(*args):
        print('calling {fun}{args}'.format(fun=fn.__name__,args=args))
        return fn(*args)
    return iter
            
@traceit
def gcd_t(m,n):
    return m if (n == 0) else gcd_t(n, m % n)

@traceit
def fib_t(n):
    assert n >= 0
    return n if n < 2 else fib_t(n-1) + fib_t(n-2)

@memoise
def fibm(n):
    assert n >= 0
    return n if n < 2 else fibm(n-1) + fibm(n-2)
    
def compose(*args):
    (*fns,inp) = args
    for fn in fns[::-1]:
        inp = fn(inp)
    return inp

add1 = lambda n: n+1
add2 = lambda n: n+2
add3 = lambda n: n+3
mul2 = lambda n: n*2
mul3 = lambda n: n*3

def walk(n):
    pos = 0
    acc = [pos]
    for _ in range(n):
        pos += random.choice([-1,1])
        acc.append(pos)
    return acc

def rot(string, shiftby):
    """
    rot: (String, Int) -> String
    rot takes a string and an integer, named shiftby, and moves the characters in the string by that number
    
    Examples
    -----------
    > rot('hal',  1) == 'ibm'
    > rot('ibm', -1) == 'hal'
    > rot('abCD', 1) == 'bcDE'
    """
    def shift(c):
        return shift(c.lower()).upper() if c.isupper() else chr((((ord(c)-97)+shiftby)%26)+97)
    return ''.join([(lambda c: shift(c) if c.isalpha() else c)(c) for c in string])

def readfile(fname):
    with open(fname, 'r') as f:
        return f.readlines()

def writefile(ifile, ofile, n):
    out = rot(readfile(ifile)[0], n)
    with open(ofile, 'w') as f:
        f.writelines(out)
