
#this is an attempt to mock up the convict conditioning app via simple python


#to-do; build file checker. if workout.txt (need to convert to .csv when I can test on my comp) doesn't exist, create it.  

#import datetime module for timestamping when writing to workout.txt
import datetime



#define body parts for workout 
big_six = ["Chest", "Core (Abs)", "Back (Pull)", "Shoulders (Push)", "Lower Body", "Core (Back)", "Grip (Hang)"]
def print_big_six():
	print "What are we going to work out?"
	step = 0
	for body_part in big_six:
		print "%s = %s" % (step, body_part)
		step += 1
#to-do, build in exception checker if user does not select a number

#define steps (not sure why yet?)
steps = [1,2,3,4,5,6,7,8,9,10]

# asks user to select a body part
def start():
	print_big_six()
	select = raw_input("Select Number 0-"+(str(len(big_six)-1))+" to select a body part\n>")
	if int(select) >= len(big_six):
		print "Sorry, 0-5 please"
		select = 4
		start()
	return big_six[int(select)]

#ask user for number of reps done in one set
def how_many_reps():
	print "OK let's go!"
	reps = raw_input("How many reps did you do?\n>")
	return reps

#some exercises don't require 3 sets....will need to build in some branching logic. Check master data sheet for which should branch....
def reps():
	reps_record = []
	i = 0
	while i < 3:
		reps_record.append(how_many_reps())
		i += 1
	return reps_record

#really need to clean this up...look into csv module in the future as it will need to be converted anyways
def write_to_file(user, workout, step_today, set_record):
	date_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
	date = datetime.datetime.now().strftime("%Y-%m-%d")
	time = datetime.datetime.now().strftime("%H-%M")
	target = open('workout.txt', 'a')
	target.write("\n")
	target.write(date)
	target.write(",")
	target.write(time)
	target.write(",")
	target.write(date_time)
	target.write(",")
	target.write(user)
	target.write(",")
	target.write(workout)
	target.write(",")
	target.write(step_today)
	target.write(",")
	target.write(set_record[0])
	target.write(",")
	target.write(set_record[1])
	target.write(",")
	target.write(set_record[2])
	target.close

def rep_workflow():
	workout = start()
	step_today = raw_input("Which step? 1-10\n>")

	print "OK you want to work out your %s at step %s, right?" % (workout,step_today)
	raw_input()

	print "Ok we'll do 3 sets (just to make things simple)"

	set_record = reps()
	
	
	print "OK, awesome! We're all done with 3 sets of the exercise. Here are your results"

	print set_record

	print "Let's export the results to a text file"

	print "We're going to name the file workout.txt for now" 


	write_to_file(user, workout, step_today, set_record)
	print "Done!"
	

#loop to keep program running WITHOUT re-asking for users name
def reppin():
	run_workflow = raw_input("Add Reps? y/n\n>").lower()
	if "y" == run_workflow:
		rep_workflow()
		reppin()
	else:
		print "Good workout! We'll keep track of your reps going forward!"

user = raw_input("Hi! Welcome to the CC Python App. First, who am I talking to? \n>").lower()
reppin()




