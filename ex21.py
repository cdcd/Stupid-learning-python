#encoding=utf-8

def add(a,b):
    print "Adding %d + %d" % (a,b)
    return a + b
    
def subtract(a,b):
    print "Subtracting %d - %d" % (a,b)
    return a - b
    
def multiply(a,b):
    print "Multiply %d * %d" % (a,b)
    return a * b
    
def divide(a,b):
    print "Divide %d / %d" % (a,b)
    return a / b

print "Let's do some math with just function"
age = add(30,5)
height=subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age:%d,Height:%d,Weight:%d,IQ:%d" % (age,height,weight,iq)

print "Here is a puzzle."

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print "That becomes:",what,"can you do it hand?"
    
