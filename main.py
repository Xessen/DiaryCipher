from math import prod

def numbercaesar(secretcode):
    print(prod(map(int,str(secretcode))))

def remaining(number,limit):
    while number>limit:
        number=number%limit
    return number
def encoder():
    secretcode=int(input())
    secretcode_2=secretcode
    #text=input()
    alph={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
    rev_alph={v: k for k, v in alph.items()}
    beth=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    count=0

    with open('test.txt') as f:
        f1=open("text1","w+")
        print('aa')
        while count<4800:
            print("bb")
            if secretcode!=0:
                change=prod(map(int,str(secretcode)))
                print("cc")

                for line in f.read():
                    print(line)
                    for char in line:
                        print(char)
                        if char in beth:  
                            f1.write(alph[remaining(change+rev_alph[char.capitalize()],26)])
                            print('a')
                        elif char==' ':
                            f1.write(" ")
                            print("b")
                        else:
                            f1.write("\n")
                            print("c")
                        
            elif secretcode==0:
                secretcode=secretcode_2
            count+=1

encoder()      
            
    
