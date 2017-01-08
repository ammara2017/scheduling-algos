burst = []
process = []
wait = []
turn_around = []
priority = []
total = 0
sort = 0
avg_wait = 0
avg_turn_around = 0

print "enter total number of processes? "
number = input()


for x in range(number):
	print "For Process P",(x+1)
	print "Burst Time: "
	burst.append(input())
	print "Priority: "
	priority.append(input())
	process.append(x+1)

for y in range(number):
	sort=y
	for z in range((y+1) , number):
		if priority[z] < priority[sort]:
			sort = z

	priority[y] , priority[sort] = priority[sort] , priority[y]
	burst[y] , burst[sort] = burst[sort] , burst[y]
	process[y] , process[sort] = process[sort] , process[y]

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

