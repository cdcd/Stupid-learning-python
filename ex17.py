#encoding=utf-8


from sys import argv
from os.path import exists

script,from_file,to_file = argv

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready,hit ENTURE to continue,CTRL+C to abort."
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)
print "Alright,all done."

in_file.close()
out_file.close()
