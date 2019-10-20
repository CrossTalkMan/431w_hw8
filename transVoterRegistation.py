import re

with open('registeredvoters.xml', 'r') as f:
    rl = f.readlines()

for i in range(len(rl)):
    rl[i] = rl[i].strip()

voters = []
clock = 0

for i in range(len(rl)):
    if '<REGISTERED>' in rl[i]:
        clock += 1
        while '</REGISTERED>' not in rl[i]:
            i += 1
            if '<FNAME>' in rl[i]:
                first_name = re.findall(r'>.+<', rl[i])[0][1:-1]
            elif 'MNAME' in rl[i]:
                middle_name = re.findall(r'>.+<', rl[i])[0][1:-1]
            elif 'LNAME' in rl[i]:
                last_name = re.findall(r'>.+<', rl[i])[0][1:-1]
            elif 'ADDRESS' in rl[i]:
                address = re.findall(r'>.+<', rl[i])[0][1:-1]
            elif 'ZIP' in rl[i]:
                zipcode = re.findall(r'>.+<', rl[i])[0][1:-1]
            elif 'PARTY' in rl[i]:
                party = re.findall(r'>.+<', rl[i])[0][1:-1]
        voters.append(str(clock) + ','
                    + str(clock) + ','
                    + first_name + ','
                    + middle_name + ','
                    + last_name + ','
                    + party + ','
                    + address + ','
                    + str(zipcode))

with open('voter_registration.txt', 'w') as f:
    for i in range(len(voters)):
        f.write(voters[i])
        f.write('\n')