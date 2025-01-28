def find_max(list):
    a,b,c,d,e = list

    if a > b:
        if a > c:
            if a > d:
                if a > e:
                    return a
                else:
                    return e
            else:
                if d > e:
                    return d
                else:
                    return e    
    else:
        if b > c:
            if b > d:
                if b > e:
                    return b
                else:
                    return e
            else:
                if d > e:
                    return d
                else:
                    return e    
        else:
            if c > d:
                if c > e:
                    return c
                else:
                    return e
            else:
                if d > e:
                    return d
                else:
                    return e                                                  

print(find_max([1,2,3,4,5]))