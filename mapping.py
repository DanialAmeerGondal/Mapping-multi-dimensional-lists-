# The following list will contain the IDs of four people. The program will pack the separate sections (name, age (date of birth), height) into 
# three different lists of information.

data = [('Alberto Franco', '15/05/2002', '175cm'), ('Gino Mcneill', '17/05/2002', '182cm'), ('Ryan Parkes', '16/02/1999', '186cm'), ('Eesha Hinton', '25/09/1998', '170')]

names = list(map(lambda element:element[0], data)) # What this does is traverses through each element and returns the first info of that element, packing it into a list.
dob = list(map(lambda element:element[1], data)) # This piece of code is similar, only does it return the second piece of info of each element. 
height = list(map(lambda element:element[2][:2], data)) # The significance of the parallel indices is to get only the height number of the info. It does this by accessing
                                                        # the third info's index and slices it by the first two characters (hence the [:2]). 
                                                        
print(names)
print(dob)
print(height)
