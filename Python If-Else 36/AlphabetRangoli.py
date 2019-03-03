def print_rangoli(size):
    N = size
    M = 4*N - 3
    if 0 <= N <= 27 :
        for a in range(N ) :  #for lines
            b = str()
            for _ in range(a +1) :  #for characters of first half
                b = b + chr(96 + N - _) + '-'
            for __ in range(a, 0, -1 ) :  # characters of second half
                b = b + chr(97 + N - __ ) + '-'
            b = b.center( M , '-')
            print(b[0 : M])
            
        for a in range(N-1 , 0 , -1) :
            b = str()
            for _ in range(a) :
                b = b + chr(96 + N - _) + '-'
            for __ in range(a-1, 0, -1 ) :  # characters of second half
                b = b + chr(97 + N - __ ) + '-'
            b =b.center( M , '-')
            print(b[0 : M])
