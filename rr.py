time = 0
remain = 0
flag = 0
count = 0
quantum_time = 0
wait_time = 0
turn_around_time = 0
burst = []
arrival = []
remaining = []

print "enter number of processes ? "
number = input()
remain = number

for a in range(number):
	print "Process P",(a+1)
	print "Arrival Time: "
	arrival.append(input())
	print "Burst Time: "
	burst.append(input())
	remaining.append(burst[a])

print "Enter Quantum Time: \t"
quantum_time = input()

print "\n\nProcess|\tTurnaround|\tWaiting Time\n"

while remain!=0:
	if remaining[count] <= quantum_time and remaining[count]>0:
		time = time + remaining[count]
		remaining[count] = 0
		flag = 1

	elif remaining[count]>0:
		remaining[count] = remaining[count] - quantum_time
		time = time + quantum_time

	if remaining[count]==0 and flag==1:
		remain = remain - 1
		print "P",(count+1),"\t ",time-arrival[count],"\t ",time-arrival[count]-burst[count]
		wait_time = wait_time + (time-arrival[count]-burst[count])
		turn_around_time = turn_around_time + (time-arrival[count])
		flag = 0

	if count == number-1:
		count = 0
	elif arrival[count+1] <= time:
		count = count +1
	else:
		count=0


print "\nAverage Waiting Time = " , wait_time/number
print "\nAverage Turnaround Time = " , turn_around_time/number

