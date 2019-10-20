import csv
import re

with open("vote_result.txt", 'r') as f:
    rl = f.readlines()

csv_file = csv.reader(open("voter_registration.csv", 'r'))

voters = {}

for elem in csv_file:
    voters[elem[2]+' '+elem[3]+' '+elem[4]] = elem[0]

candidate_csv = csv.reader(open("candidates (1).csv", 'r'))

candidates = {}

for elem in candidate_csv:
    candidates[elem[2] + ' ' + elem[3] + ' ' + elem[4]] = elem[1]

# print(voters)
print(candidates)


i = 0
clock = 1
result = []
error_voters = []
while i < len(rl):
    if rl[i][:2] == '--':
        i += 1
    else:
        j = i
        s = ''
        while rl[j][:2] != '--':
            if rl[j-1][:2] == '--':  # names
                name = re.split(r'\sVOTES\s', rl[j])[0]
                s = name
            else:
                position = re.split(r':\s?', rl[j])[0]
                candidate = re.split(r':\s?', rl[j])[1][:-1]
                print(position)
                print(candidate)
            # s = s + ',' + position + ',' + voter
                t = s.split(' ')
                c = candidate.split(' ')
                id = t[0]+' '+t[1]+' '+t[2]
                cid = c[0]+' '+c[1]+' '+c[2]
                print(id)
                print(cid)
                label = True
                try:
                    voters[id]
                except KeyError as e:
                    print('voter_id error: ' + id)
                    if id not in error_voters:
                        error_voters.append(id)
                    label = False
                try:
                    candidates[cid]
                except KeyError as e:
                    print('candidate_id error: ' + cid)
                    label = False
                if label:
                    result.append(voters[id] + ',' + position + ',' + '1' + ',' + candidates[cid] + ',' + '1' + '\n')
            j += 1
            if j >= len(rl):
                break
        i = j
with open('result.txt', 'w') as f:
    for i in range(len(result)):
        f.write(result[i])
        print(result[i])

with open("error_voters.txt", 'w') as f:
    for i in range(len(error_voters)):
        f.write(error_voters[i])
        f.write('\n')