the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','aprocots']
change = [1,'pennies',2,'dimes',3,'quarters']


for number in the_count:
    print "this is count %d" % number
    

for fruit in fruits:
    print "A fruit of type:%s" % fruit
    
    
for i in change:
    print "I got %r"  % i
    
    
elements = []

for i in range(1,6):
    print "Adding %d to the list." % i
    
    elements.append(i)
    
    
for i in elements:
    print "Elements was %d" % i
    
    