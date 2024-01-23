def decodeMessages(filePath):
    file = open(filePath, "r")
    lines = file.readlines()

    count = 0
    hm = {}
    for l in lines:
        count += 1
        line = l.split(" ")
        hm[line[0]] = line[1]  
    file.close()

    i, c = 0, 1
    s = ""
    while i<count: 
        i += c
        s += hm[str(i)].strip()+ " "
        c += 1   
    return s    

s = decodeMessages("coding_qual_input.txt")
print(s)

# Explanation: 
# 1. Open the file and read each line. While reading, split each line into two parts: number and corresponding string. Store as a key value pair in a hash map called hm where key = number and value = corresponding string.
# 2. We only need the last number in the pyramid. Since each new line in the pyramid has one plus element from the last line, we can create this sequence with a while loop by adding one plus number from the last line,
# 3. Since we have the numbers sequence, we use the as key in the hashmap and get the values for corresponding strings and add them with a white space.