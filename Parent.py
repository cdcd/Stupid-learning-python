class Parent(object):
    def implicit(self):
        print "PARENT implicit()"
        
    def altered(self):
        print 'PARENT altered()'
        
class Child(Parent):
    def implicit(self):
        print 'CHILD implicit()'
        
    def altered(self):
        print 'CHILD,BEFORE PARENT altered()'
        super(Child,self).altered()
        #super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.altered()
son.altered()
