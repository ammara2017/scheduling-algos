burst = []
wait = []
turn_around = []
process = []
avg_wait =0
avg_turn_around =0
pos =0
total = 0

print "Enter number of processes? "
number = input()

print "Enter Burst Time: "
for x in range(number):
	print "for P" , (x+1)
	burst.append(input())
	process.append(x+1)

for i in range(number):
	pos=i
	for j in range((i+1) , number):
		if burst[j] < burst[pos]:
			pos = j

	
	burst[i] , burst[pos] = burst[pos] , burst[i]
	process[i] , process[pos] = process[pos] , process[i]


wait.append(0)
for y in range(1, number):
	wait.append(0)
	for z in range(y):
		wait[y] = wait[y] + burst[z]

	total = total + wait[y]

avg_wait = total / number
total = 0

print "\nProcess \tBurst Time \tWaiting Time \tTurnAround Time"

for w in range(number):
	turn_around.append(burst[w] + wait[w])
	total = total + turn_around[w]
	print "\nP", process[w], "\t\t", burst[w], "\t\t", wait[w], "\t\t", turn_around[w]

avg_turn_around = total/number
print "\n\nAverage Waiting Time = " , avg_wait
print "\nAverage Turn Around Time = " , avg_turn_around


