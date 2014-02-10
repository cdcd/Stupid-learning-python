#encodng=utf-8
#字符串和文本     %r 用来做 debug 比较好，因为它会显示变量的原始数据，
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary,do_not)

print x
print y

print "I said:%r." % x
print "I also said:'%s'." % y

hikarious = False
joke_evalution = "Isn't that joke so funny?! %r"

print joke_evalution % hikarious
w = "This is the ledt side of ..."
e = "a string with a right side."

print w +  e


'''
result:

There are 10 types of people.
Those who know binary and those who don't.
I said:'There are 10 types of people.'.
I also said:'Those who know binary and those who don't.'.
Isn't that joke so funny?! False
This is the ledt side of ...a string with a right side.

'''

