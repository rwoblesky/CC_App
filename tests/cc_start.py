#check start


#this is an attempt to mock up the convict conditioning app via simple python

big_six = ["Chest", "Core (Abs)", "Back (Pull)", "Shoulders (Push)", "Lower Body", "Core (Back)"]
steps = [1,2,3,4,5,6,7,8,9,10]

def start():
	select = raw_input("Select Number 0-5 to select a body part \n0 = Chest\n1 = Core (Abs)\n2 = Back(Pull)\n3 = Shoulders (Push)\n4 = Lower Body\n5 = Core (Back)\n> ")
	if int(select) >= len(big_six):
		print "Sorry, 0-5 please"
		start()
	return big_six[int(select)]

workout = start()
step_today = raw_input("Which step? 1-10")