data = []

# Read the text file
with open('files/subs-unraw-calcd.txt', 'r') as file:
    lines = file.readlines()

# Process each line in the file
for i in range(0, len(lines), 3):
    name = lines[i].strip('[]\n')
    startTime, endTime = map(float, lines[i + 1].split(' --> '))

    entry = {
        'index': i // 3,
        'name': name,
        'startTime': startTime,
        'endTime': endTime
    }

    data.append(entry)

