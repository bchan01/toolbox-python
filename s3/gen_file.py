f = open("emails.dat","w+")

size = 12
000
000
#size = 500000
for i in range(size):
   if i > 0:
      f.write('\n') 
   f.write("{}|test@abc.com|test".format(i+1))
