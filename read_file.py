#f=open('test.txt','r')

#contextmanager
with open('test.txt','r') as f:
    size_read=10
    f_content=f.read(size_read)
    #f_content=f.read(10)
    print(f_content)
    #print(f.tell())
    f.seek(0)

    f_content=f.read(50)
    print(f_content)
    #while len(f_content)>0:
     #   print(f_content)
      #  f_content=f.read(size)


#print(f.readline(),end='')
#print(f.readline(),end='')
#print(f.readlines())
#print(f.read())
