#Define path
path = 'C:/Tomas/Text/test.txt'

#Open file, different modes
f = open(path)
print(f)
f = open(path,'rt')
print(f)
f.close()
f = open(path,'r+t')
f.close()

#Exception, wrong path
path = 'C:/Tomas/Test/test.txt'

#Open file + exceptions
try:
    f = open(path,'rt')
except IOError as e:
    print(e)
    
print(f)

#Open file: with
with open(path, 'rt'):
    pass

#Open file: with + try
try:
    with open(path, 'rt') as f:
        file_content_all = f.read()
        print(file_content_all)
        
        file_content_n = f.read(15)
        print(file_content_n)
        
except IOError as e:
    print(e)
    
#Open file: with + try, readline
try:
    with open(path, 'rt') as f:
        file_content_line = f.readline()
        print(file_content_line)
        file_content_line = f.readline()
        print(file_content_line)
    
except IOError as e:
    print(e)

#Open file: with + try, readlines
try:
    with open(path, 'rt') as f:
        file_content_all = f.readlines()
        print(file_content_all)
        c =file_content_all[1][2]
        print(c)
   
except IOError as e:
    print(e)
    
#Writing to file, append, do not close
f=open(path, 'ta')
text = 'I do not know'
f.write(text)
# f.close() Do not close

#Writing to file, append
f=open(path, 'ta')
text = '\nI do not know'
f.write(text)
f.close()

#Writing to file, new
f=open(path, 'tw')
text = '\nI do not know'
f.write(text)
f.close()

#Open binary file
path = 'C:/Tomas/Text/picture.png'
f = open(path,'br')
data = f.read()
print(data)