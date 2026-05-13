import datetime
while True:
    print("\n\n.\n..\n...\n..\n.\n")
    f = []
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
            print(datetime.datetime.now(),f" - Found!\n > {num} is a super perfect number\n")
            f.append(num)
            
    limit = int(input('maximum num :\n  >  '))
    print("\n")

    for n in range(limit):
        n = n+1
        print(datetime.datetime.now(),f" - solving for {n} ..")

        divs1 = divisors(n)
        sdivs1 = summation(divs1)
        divs2 = divisors(sdivs1)
        sdivs2 = summation(divs2)

        superperfect(n, sdivs2)

    print(f"\nsuperperfect numbers in the given range are:\n   {f}")    
    print("done.")
