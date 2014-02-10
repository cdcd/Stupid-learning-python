#encoding=utf-8
from sys import argv
script,input_file = argv

def print_all(file):
    print file.read()
    
def rewind(file):
    file.seek(0)   #标记，从0开始 ，如果是输入4,，就会从bb开始
    
def print_a_line(line_count,file):
    print line_count,file.readline()
    
    
 
    
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)


print "Now let's rewind,kind of like a tape"
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)



'''
txt文档的内容是
aa
bb
cc
dd


result:

First let's print the whole file:

aa
bb
cc
dd

Now let's rewind,kind of like a tape
Let's print three lines:
1 aa

2 bb

3 cc

'''

