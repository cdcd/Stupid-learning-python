#encoding=utf-8
#'\'是转义符号  \n换行   \t Horizontal Tab (TAB) 水平制表符

print "I am 6'2\" tall."
print 'I am 6\'2" tall.'

tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backsalash_Cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backsalash_Cat
print fat_cat




'''
reslut:

I am 6'2" tall.
I am 6'2" tall.
     I'm tabbed in.
I'm split
on a line.
I'm \ a \ cat.

I'll do a list:
    * Cat food
    * Fishies
    * Catnip
    * Grass


'''
