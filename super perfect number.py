import datetime
while True:
    
    def divisors(num):
        l=[]
        for i in range(num):
            i = i+1
            r = num%i
            if r == 0 :
                l.append(i)
        return(l)

    def summation(l):
        s = 0
        for i in l:
            s = s + i
        return(s)

    def superperfect(num, sdivs2):
        if sdivs2 == 2 * num:
            print(datetime.datetime.now(),f"\n {num} is a superperfect number")
    
    num = int(input('num :\n  >  '))

    divs1 = divisors(num)
    sdivs1 = summation(divs1)
    divs2 = divisors(sdivs1)
    sdivs2 = summation(divs2)

    superperfect(num, sdivs2)
