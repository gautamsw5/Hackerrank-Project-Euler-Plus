arr=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100,1000,1000000,1000000000,1000000000000]
brr=['','One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety','Hundred','Thousand','Million','Billion','Trillion']
dct={0:'', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
     7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven',
     12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
     16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
     20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
     70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'Hundred',
     1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion',
     1000000000000: 'Trillion'}
def get3D(n):
    if n<=20:
        return dct[n]
    elif n<100 and n in dct:
        return dct[n]
    elif n%100==0:
        return dct[n//100]+" "+dct[100]
    a=n-n%10
    b=n%10
    if n<100:
        return dct[a]+" "+dct[b]
    c=n-n%100
    return dct[c//100]+" "+dct[100]+" "+get3D(n%100)
def get3D2(n):
    if n==1000:
        return dct[1]+dct[n]
    if n<=20:
        return dct[n]
    elif n<100 and n in dct:
        return dct[n]
    elif n%100==0:
        return dct[n//100]+dct[100]
    a=n-n%10
    b=n%10
    if n<100:
        return dct[a]+dct[b]
    c=n-n%100
    return dct[c//100]+dct[100]+"and"+get3D2(n%100)
t=int(input())
for k in range(t):
    n=int(input())
    s=""
    if n>=10**12:
        x=n//10**12
        s=s+get3D(x)+" "+dct[10**12]+" "
        n=n%10**12
    if n>=10**9:
        x=n//10**9
        s=s+get3D(x)+" "+dct[10**9]+" "
        n=n%10**9
    if n>=10**6:
        x=n//10**6
        s=s+get3D(x)+" "+dct[10**6]+" "
        n=n%10**6
    if n>=10**3:
        x=n//10**3
        s=s+get3D(x)+" "+dct[10**3]+" "
        n=n%10**3
    s=s+get3D(n)
    print(s.strip())
