import test

s = """<entry>
    <id>tag:search.twitter.com,2005,1142881099</id>
    <published>2009-01-23T20:04:53Z</published>
  </entry> """

print s.find(">")
print len(s.split(':')) 
print len(s.split('>')[2].split(':'))

def h(x=1, y=3, z=4):

    return[x, y, z]

print h(1,2)
print h(1,z=5)
    
# test.testEqual(h(1, 2), [1, 2, 4])
# test.testEqual(h(1, z = 5), [1, 3, 5])

def enum(L):
    res = []
    n = 1
    for item in L:
        res.append((n, item))
        n = n + 1
    return res
    # 
# test.testEqual(enum(["a", "b", "c"]), [(1, "a"), (2, "b"), (3, "c")])
print enum(["a", "b", "c"])

students = [("Jamal", 98, "A+"),
            ("Eloise", 87, "B+"),
            ("Madeline", 99, "A+")]

outfile = open("grades.csv","w")
# output the header row
outfile.write("Name, score, grade\n")
# output each of the rows:
for student in students:
    outfile.write("%s, %d, %s\n" % student)
outfile.close()

s = """ Michelle
loves
to
play
ball"""
print s

s = """<entry>
    <id>tag:search.twitter.com,2005,1142881099</id>
    <published>2009-01-23T20:04:53Z</published>
  </entry> """
print (s.split(':')) 
print len(s.split(':')) 
print len(s.split('>')[2].split(':'))

# def f(list):
# 	newlist= []
# 	for x in list:
# 		if "z" in x:
# 			newlist=newlist.append(x.split[0])
# 	return newlist
# words= ['Amazing', 'corny', 'zany']
# print f(words)
# 
# 
# def f(list):
# 	newlist= []
# 	for x in list:
# 		s=x.split()
# 		first=s[0]
# 		newlist=newlist.append(first)
# 	return newlist
# 
# words= ['Amazing', 'corny', 'zany']
# print f(words)

def interp(x, y):

	mystr = 'That is %d in a row, %s. Congratulations!' %(x,y)
	return mystr

print interp(5,'sir')
test.testEqual(interp(5, "sir"), "That is 5 in a row, sir. Congratulations!")
test.testEqual(interp(6, "your highness"), "That is 6 in a row, your highness. Congratulations!")

def h(x=1,y=3 ,z=4):

    return[x, y, z]
print h()

def enum(L):
    res = []
    n = 1
    for item in L:
        res.append((n, item))
        n = n + 1
    return res
print enum(["a", "b", "c"])

def f(list):
	newlist= []
	for x in list:
		if 'z' in x:
			newlist.append(x[0])
	return newlist
words= ['Amazing', 'corny', 'zany']
print f(words)

# def function(sentence):
# 	#print input
# 	answer = []
# 	for word in sentence.split():
# 		if word not in answer:
# 			answer.append(word)

def f(list):
	newlist= []
	for x in list:
		if 'z' in x:
			newlist.append(x[0])
	# return newlist
	return [x[0] for x in list if 'z' in x]
	
words=['amazing', 'corny', 'zany']
print f(words)

print map ((lambda value: 5*value), [1,2,3])

def g(list):
	return sorted(list, key= lambda x: x[-1])
	
# PROBLEM SET 8

fall_list = ["leaves","apples","autumn","bicycles","pumpkin","squash","excellent"]

# Write code to sort the list fall_list in reverse alphabetical order. 
# Assign the sorted list to the variable sorted_fall_list.

sorted_fall_list= sorted(fall_list, reverse=True)
print sorted_fall_list

# Now write code to sort the list fall_list by length of the word, longest to shortest.
# Assign this sorted list to the variable length_fall_list.

length_fall_list= sorted(fall_list, key=lambda x: len(x), reverse=True)
print length_fall_list

food_amounts = [{"sugar_grams":245,"carbohydrate":83,"fiber":67},{"carbohydrate":74,"sugar_grams":52,"fiber":26},{"fiber":47,"carbohydrate":93,"sugar_grams":6}]

# Write code to sort the list food_amounts by the key "sugar_grams", from lowest to highest.
# Assign the sorted list to the variable sorted_sugar.

sorted_sugar= sorted(food_amounts, key = lambda x: x["sugar_grams"])
print sorted_sugar

# Now write code to sort the list food_amounts by 
#  the value of the key "carbohydrate" minus the value of the key "fiber" in each one, from lowest to highest.
# Assign this sorted list to the variable raw_carb_sort.

raw_carb_sort = sorted(food_amounts, key= lambda x: x["carbohydrate"]- x["fiber"])
print raw_carb_sort

# Convert this string concatenation to one using string interpolation.
# Assign the result to the variable t.
x = 12
fname = "Joe"
our_email = "scammer@dontfallforthis.com"
s = "Hello, " + fname + ", you may have won $" + str(x) + " million dollars. Please send your bank account number to " + our_email + " and we will deposit your winnings."
t = ""

print "hello, %s, you may have won $%d million dollars. Please send your bank account number to %s and we will deposit your winnings." %(fname, x, our_email)

# Write code, using string interpolation and the variables nm, min_mt, and mile_amt, to produce the string 
# "Albert walked 0.67 miles today in 50 minutes." Assign it to albert_str.
nm = "Albert"
min_amt = 50
mile_amt = 0.673892

albert_str= "%s walked %0.2f miles today in %d minutes." %(nm, mile_amt, min_amt)
print albert_str

# Define a function called walk_reporter, which takes as input: 
#  - a string that represents someone's name, 
#  - a float that represents the number of miles they walked,
#  - and an integer that represents the number of minutes they spent walking.
#
# The function should RETURN a string in the format:
# "[NAME STR] walked [MILE FLOAT with TWO digits after the decimal] miles in
# [MINUTES INT] minutes."
# You MUST use string interpolation in the function. 
# You should NOT use raw_input to get the inputs; they are passed in as parameters.

def walk_reporter(name, miles, minutes):
	return "%s walked %0.2f miles in %d minutes." %(name, miles, minutes)
print walk_reporter("michelle", 2.345, 10)
test.testEqual(walk_reporter("Jamie",5.233679,202), "Jamie walked 5.23 miles in 202 minutes.", "walk_reporter test 1")

def f(list):
	newlist= []
	for x in list:
		if 'z' in x:
			newlist.append(x[0])
	return newlist
words= ['Amazing', 'corny', 'zany']
print f(words)

def f(list):
	return [x[0] for x in list if 'z' in x] 
test.testEqual(f(['Amazing', 'corny', 'zany']), ['A', 'z'])


