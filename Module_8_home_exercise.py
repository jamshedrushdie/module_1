import re
import json

data = json.load(open('C:\\Users\\Jamshed_Rushdie\\Documents\\Output.json'))

txt = ""

for d in data:
	txt += d['text']
	txt += '\n'

print(txt)
with open("C:\\Users\\Jamshed_Rushdie\\Documents\\Output.txt", 'w') as i: i.write(txt)
    


inp = open('C:\\Users\\Jamshed_Rushdie\\Documents\\Output.txt', 'r', encoding="utf8", errors='ignore').read()
# print(inp)

lines = inp.split('\n')
# print(lines)

stripped = ""
for l in lines:
	if len(l) > 1 and l[-1] != '-':
		stripped += l + '\n'

# print(stripped)

chars = "abcdefghijklmnopqrstuvwxyz"
total_counts = {c.lower(): 0 for c in chars}
cap_counts = {c.upper(): 0 for c in chars}

for c in stripped:
	if c.isalpha():
		total_counts[c.lower()] += 1
		if c in cap_counts:
			cap_counts[c] += 1

char_table = [['Letter', 'Total', 'capital', '% of Caps']]
for c in chars:
	t = total_counts[c.lower()]
	C = cap_counts[c.upper()]
	if t > 0:
		p = 100*C/t
		char_table.append([c, t, C, p])

# for l in char_table: print("\t".join([str(x) for x in l]))

alpha = re.sub(r'[^A-za-z]', ' ', stripped)
alpha = " ".join(re.split(r"\s+", alpha, flags=re.UNICODE))
# print(alpha)

wc = {}
for w in alpha.split():
	w = w.lower()
	if w not in wc: wc[w] = 0
	wc[w] += 1

wc_table = [['Words', 'Count']]
for w in wc:
	wc_table.append([w, wc[w]])

# print()
# for l in wc_table: print("\t".join([str(x) for x in l]))    
    
import csv

with open('C:\\Users\\Jamshed_Rushdie\\Documents\\Table_wordcount.csv', 'w', newline='') as csvfile:
    w = csv.writer(csvfile)
    w.writerows(wc_table)

with open('C:\\Users\\Jamshed_Rushdie\\Documents\\Table_character_percent.csv', 'w', newline='') as csvfile:
    w = csv.writer(csvfile)
    w.writerows(char_table)
    