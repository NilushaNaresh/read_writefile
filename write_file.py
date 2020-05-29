#with open('test.txt','r') as rf:
#with open('test.txt','w') as wf:
 #   wf.write('11.Citizen:')
#for adding picture files use 'wb' as to open the pic.jpg in binary mode
with open('test.txt','r') as rf:
    with open('test_copy.txt','w') as wf:
        for i in rf:
            wf.write(i)
