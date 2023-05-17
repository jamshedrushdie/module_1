import re

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


import sqlite3
conn = sqlite3.connect('tables.db')
cursor = conn.cursor()

cursor.execute("""DROP TABLE IF EXISTS Table_wordcount""")
cursor.execute("""DROP TABLE IF EXISTS Table_character_percent""")

cursor.execute("""CREATE TABLE Table_wordcount(Words VARCHAR(255), Count INTEGER(255))""")
cursor.execute("""CREATE TABLE Table_character_percent(Letter CHAR(1), Total INTEGER(255), capital INTEGER(255), Caps DECIMAL(5, 2))""")

cursor.executemany("""INSERT INTO Table_wordcount(Words, Count) VALUES (?, ?)""", [ (r[0], r[1]) for r in wc_table[1:]])
cursor.executemany("""INSERT INTO Table_character_percent(Letter, Total, capital, Caps) VALUES (?, ?, ?, ?)""", [(r[0], r[1], r[2], r[3]) for r in char_table[1:]])
conn.commit()

for r in cursor.execute("""SELECT * FROM Table_character_percent"""): print(r)
for r in cursor.execute("""SELECT * FROM Table_wordcount"""): print(r)

conn.close()

