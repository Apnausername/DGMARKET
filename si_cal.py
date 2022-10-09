ef simple_interest(p,t,r):
    print('Principal : ', p)
    print('Duration :', t)
    print('Rate of interest :',r)
     
    si = (p * t * r)/100
     
    print('Calculate Simple Interest is :', si)
    return si
     
simple_interest(8, 6, 8)
