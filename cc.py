#this is an attempt to mock up the convict conditioning app via simple python

#to-do; build file checker. if workout.txt (need to convert to .csv when I can test on my comp) doesn't exist, create it.  

#import datetime module for timestamping when writing to workout.txt
import datetime

#define body parts for workout 
big_six = ["Chest", "Core (Abs)", "Back (Pull)", "Shoulders (Push)", "Lower Body", "Core (Back)", "Grip (Hang)"]

#define chest exercises. is there a better way to manage all this data? we'll have essentially 6 lists w/ 10 steps...lots of data to hard code....csv?
#i bet i could store this data in a csv, then have the file read a line based on the selection....
chest = ["Wall Pushups", "Incline Pushups", "Kneeling Pushups","Half Pushups","Full Pushups","Close Pushups","Uneven Pushups","Half One-Arm Pushups","Lever Pushups","One Arm Pushups"]
core_abs = ["Knee Tucks","Flat Knee Raises","Flat Bent Leg Raises","Flat Frog Raises","Flat Straight Leg Raises","Hanging Knee Raises","Hanging Bent Leg Raises","Hanging Frog Raises","Partial Straight Leg Raises","Hanging Straight Leg Raises"]
lower =["Shoulderstand Squats","Jackknife Squats","Supported Squats","Half Squats","Full Squats","Close Squats","Uneven Squats","Half One Leg Squats","Assisted One Leg Squats","One Leg Squats"]
back = ["Vertical Pulls","Horizontal Pulls","Jackknife Pulls","Half Pullups","Full Pullups","Close Pullups","Uneven Pullups","1/2 One Arm Pullups","Assisted One Arm Pullups","One Arm Pullups"]
shoulders = ["Wall Headstands","Crow Stands","Wall Handstands","Half Handstand Pushups","Hand Stands Pushups","Close Handstand Pushups","Uneven Handstand Pushups","1/2 One Arm Handstand Pushups","Lever Handstand Pushups","One Arm Handstand Pushups"]
core_back =["Short Bridges","Straight Bridges","Angled Bridges","Head Bridges","Half Bridges","Full Bridges","Wall Walking Bridges (Down)","Wall Walking Bridges (Up)","Closing Bridges","Stand to Stand Bridges"]

# simple function that we'll use to print values of list (gives user mapping of list contents to file). Maybe in future remove 0 value.
def print_list_for_mapping(a):
	step = 0
	for value in a:
		print "%s = %s" % (step, value)
		step += 1
	
#to-do, build in exception checker if user does not select a number

#define steps (not sure why yet?)
steps = [1,2,3,4,5,6,7,8,9,10]

# asks user to select a body part
def start():
	print "What are we going to work out?"
	print_list_for_mapping(big_six)
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
	if workout == "Chest":
		print "Select a Chest Step:"
		print_list_for_mapping(chest)
	elif workout == "Core (Abs)":
		print "Select a Core (Abs) Step:"
		print_list_for_mapping(core_abs)
	elif workout == "Back (Pull)":
		print "Select a Back Step:"
		print_list_for_mapping(back)
	elif workout == "Shoulders (Push)":
		print "Select a Shoulders Step:"
		print_list_for_mapping(shoulders)
	elif workout == "Lower Body":
		print "Select a Lower Body Step:"
		print_list_for_mapping(lower)
	elif workout == "Core (Back)":
		print "Select a Core Back Step:"
		print_list_for_mapping(core_back)
	else:
		print "Sorry, values not defined yet. Look for an update soon!"
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




