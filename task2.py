#!python3
"""
Create a function that calculates the amount of compound interest 
earned.
t = time in years
P = amount invested
n = # of compounding periods per year (how often interest is calculated)
Output should be rounded to 2 decimal places
r = rate of interest as a percentage
"""

def compoundInterest(P,r,t,n):
    P=float(P)
    r=float(r)/100.0
    n=float(n)
    t=float(t)
    compoundInterest=P*(1+r/n)**(n*t)
    compoundInterest=round(compoundInterest,2)
    print(compoundInterest)
    return compoundInterest

if __name__ == "__main__":
    assert compoundInterest(1000,4,2,4) == 1082.86
    assert compoundInterest(2500,4.2,20,12) == 5782.43
    assert compoundInterest(83,7,5,365) == 117.78
    assert compoundInterest(10000,3,10,2) == 13468.55