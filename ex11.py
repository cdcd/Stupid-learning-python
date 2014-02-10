#encoding=utf-8
print "How old are you?",
age = int(raw_input())  #加int就是输入数字格式。raw_input默认是字符串形式输入
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So,you're %d old.%r tall and %r heavy." % (age,height,weight)
