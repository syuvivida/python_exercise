import sys
def subtract(a,b):
#    print(a'-'b'=?')
    c=int(a)
    d=int(b)
    e=c-d
    print('('+a+')-('+b+')='+str(e))

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2],sys.argv[3])
