def h():
    print ('Wen Chuan')
    m = yield 5  # Fighting!
    print ('m=', m)
    d = yield 12
    print ('We are together!')
    print (d)
    test = yield 35
    print (test)

if __name__ == '__main__':

    c = h()

    current = next(c)  # start generator, stop at the first yield

    print(current)

    current = c.send('Fighting!') # send current yield 'fighting', stop at the next yield
    print (current)
    c.send('got it')
    print (list(c))
    print (list(h()))