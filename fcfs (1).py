burst_time = []
wait = []
turn_around = []
avg_wait = 0
avg_turn_around = 0

print "Enter number of Processes?"

number = input()

print "Enter Processes BT \n"

for x in range(number):
	print "for P [" , (x+1) , "] = "
	burst_time.append(input())


wait.append(0)

for x in range(1 ,number):
	wait.append(0)
	for y in range(x):
		wait[x] = wait[x] + burst_time[y]


print "\nProcess \tBurst Time\tWaiting Time\tturn_around Time"

for x in range(number):
	turn_around.append(burst_time[x] + wait[x])
	avg_wait = avg_wait + wait[x]
	avg_turn_around = avg_turn_around + turn_around[x]
	print "\nP[",(x+1),"]\t\t",burst_time[x],"\t\t",wait[x],"\t\t",turn_around[x]



avg_wait = avg_wait / number
avg_turn_around = avg_turn_around / number

print "\n Average Waiting Time : " , avg_wait
print "\n Average Turn Around Time : " , avg_turn_around



