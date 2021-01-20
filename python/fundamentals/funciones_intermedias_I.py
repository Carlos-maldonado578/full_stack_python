import random
def randInt(min=0  , max=100  ):
    num = random.random()
    return num
print(randInt()) 		# should print a random integer between 0 to 100
print(randInt(max=50)) 	# should print a random integer between 0 to 50
print(randInt(min=50)) 	# should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

#Respuestas
# 0.036284680992570095
# 0.4764200473648649
# 0.6317589725816279
# 0.8701418910466693