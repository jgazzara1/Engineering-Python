loginName = 20

import myModule #this pollues the namespace, rewrites login name

#instead put an underscore in front of a variable name, this stops importing

myModule.simpleFunction()
print myModule._loginName
print loginName
