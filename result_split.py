#cc workout.csv spliter
#this program will split the rows? sum the values? We'll see...

workoutfile = open('workout.txt', 'r')
yourResult = [line.split(',') for line in workoutfile]

print yourResult
print len(yourResult)
