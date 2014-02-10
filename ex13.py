#encoding=utf-8
from sys import argv

script,frist,second,third = argv

print "The script is called:",script
print "Your first variable is:",frist
print "Your second variable is:",second
print "Your third variable is:",third

s = raw_input("Enter your String:")
print s

'''
argv 和 raw_input() 有什么不同？
不同点在于用户输入的时机。如果参数是在用户执行命令时就要输入，那就是 argv，如果是在
脚本运行过程中需要用户输入，那就使用 raw_input()。
'''


