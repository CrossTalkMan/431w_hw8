import re

with open('candidates_all.xml', 'r') as f:
    rl = f.readlines()

for i in range(len(rl)):
    rl[i] = rl[i].strip() #  remove '\t', '\s', etc.

candidates = []

for i in range(len(rl)):
    if '<MAYOR>' in rl[i]: #  deal with voters run in mayor
        while rl[i] != "</MAYOR>":
            i += 1
            if "<CITY>" in rl[i]:
                city = rl[i].split("=\'")[1][:-2]
                i += 1
            elif "</CITY>" in rl[i]:
                i += 1
            else:
                if rl[i] == '<CANDIDATE>':
                    while rl[i] != "</CANDIDATE>":
                        i += 1
                        if "<PARTY>" in rl[i]:
                            party = re.findall(r'>.+<', rl[i])[0][1:-1]
                            print(party)
                        elif "<FNAME>" in rl[i]:
                            first_name = re.findall(r'>.+<', rl[i])[0][1:-1]
                            print(first_name)
                        elif "<MNAME>" in rl[i]:
                            middle_name = re.findall(r'>.+<', rl[i])[0][1:-1]
                            print(middle_name)
                        elif "<LNAME>" in rl[i]:
                            last_name = re.findall(r'>.+<', rl[i])[0][1:-1]
                            print(last_name)
                        elif "<ADDRESS>" in rl[i]:
                            address = re.findall(r'>.+<', rl[i])[0][1:-1]
                            print(address)
                        elif "<ZIP>" in rl[i]:
                            zipcode = re.findall(r'>\d+<', rl[i])[0][1:-1]
                            print(zipcode)
                    candidates.append(first_name + ','
                                    +middle_name + ','
                                    +last_name + ','
                                    +party + ','
                                    +address + ','
                                    +city + ','
                                    +"MAYOR")


