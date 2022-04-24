import sys

print (len(sys.argv))
print (str(sys.argv))

print(sys.argv[0])
a = 1 + float(sys.argv[1])
print("<text%0.2f>.log"%(a))