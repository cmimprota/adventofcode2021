with open('SonarSweepInput.txt', 'r') as file:
    measurements = file.readlines()
    measurements = [int(i) for i in measurements]

# PART 1
increase_counter = 0
for i in range(1, len(measurements)):
    if(measurements[i] > measurements[i-1]):
        increase_counter +=1
print(f'Part 1: {increase_counter}')

# PART 2
increase_counter = 0
for i in range(2, len(measurements)-1):
    common = measurements[i-1] + measurements[i]
    current = common + measurements[i+1]
    prev = common + measurements[i-2]
    if(current>prev):
        increase_counter +=1
print(f'Part 2: {increase_counter}')
