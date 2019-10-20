import re

with open('votes.xml', 'r') as f:
    rl = f.readlines()

for i in range(len(rl)):
    rl[i] = rl[i].strip()

rl = rl[4:]

votes = []

for i in range(len(rl)):
    if '<VOTER>' in rl[i]:
        while '</VOTER>' not in rl[i]:
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
            elif '<VOTES>' in rl[i]:
                votes.append('----')
                votes.append(first_name + ' '
                            + middle_name + ' '
                            + last_name + ' '
                            + "VOTES FOR:")
                while '</VOTES>' not in rl[i]:
                    i += 1
                    if '<PRESIDENT>' in rl[i]:
                        all_info = re.findall(r'>.+<', rl[i])[0][1:-1].split('~')                    
                        votes.append('PRESIDENT:'
                                    + all_info[0] + ' '
                                    + all_info[1] + ' '
                                    + all_info[2])
                    elif '<GOVERNOR>' in rl[i]:
                        all_info = re.findall(r'>.+<', rl[i])[0][1:-1].split('~')
                        votes.append('GOVERNOR:'
                                    + all_info[0] + ' '
                                    + all_info[1] + ' '
                                    + all_info[2])
                    elif '<SENATOR>' in rl[i]:
                        all_info = re.findall(r'>.+<', rl[i])[0][1:-1].split('~')
                        votes.append('SENATE:'
                                    + all_info[0] + ' '
                                    + all_info[1] + ' '
                                    + all_info[2])
                    elif '<MAYOR>' in rl[i]:
                        all_info = re.findall(r'>.+<', rl[i])[0][1:-1].split('~')
                        votes.append('MAYOR:'
                                    + all_info[0] + ' '
                                    + all_info[1] + ' '
                                    + all_info[2])
                    elif '<STATE REP>' in rl[i]:
                        all_info = re.findall(r'>.+<', rl[i])[0][1:-1].split('~')
                        votes.append('STATE HOUSE:'
                                    + all_info[0] + ' '
                                    + all_info[1] + ' '
                                    + all_info[2])

with open("vote_result.txt", 'w') as f:
    for i in range(len(votes)):
        f.write(votes[i])
        f.write('\n')
