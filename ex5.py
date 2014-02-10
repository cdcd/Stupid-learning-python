#encoding=utf-8
#更多变量和打印
my_name = 'Zed A. Shaw'
my_age = 35 #not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Le's talk abut %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pound heavy. " % my_weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line tricky,try to get it exactly right
print "If I add %d,%d,and %d I get %d." % (my_age,my_height,my_weight,my_age + my_height + my_weight)

'''
result:

Le's talk abut Zed A. Shaw.
He's 74 inches tall.
He's 180 pound heavy. 
Actually that's not too heavy
He's got Blue eyes and Brown hair.
His teeth are usually White depending on the coffee.
If I add 35,74,and 180 I get 289.

''' 
