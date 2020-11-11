import sqlite3

conn = sqlite3.connect("TextDB.sqlite")
cur = conn.cursor()

cur.execute("""DROP TABLE IF EXISTS Text""")
cur.execute("""CREATE TABLE Text (letter TEXT, percentage TEXT)""")

try:
    fname = input("Please enter file name: ")
    fhandle = open(fname, "r")
except:
    print("File doesn't exist!", end="")
    quit()

# fname = "mbox.txt"
# fhandle = open(fname, "r")

lst = list()
for i in fhandle:
    for j in i.lower():
        if j.isalpha():
            lst.append(j)

dic = dict()
for i in lst:
    dic[i] = dic.get(i, 0) + 1

count = sum(dic.values())
# count = 0
# for i in dic.values():
#     count += i
#     print(i)
for k, v in dic.items():
    dic[k] = v / count * 100

tmp_lst = list()
for k,v in dic.items():
    newtup = (v, k)
    tmp_lst.append(newtup)
tmp_lst.sort(reverse=True)

print("letter", "percentage")
for k, v in tmp_lst:
    print(v, str(round(k, 3)) + "%")
    cur.execute("INSERT INTO Text(letter, percentage) VALUES(?, ?)", (v, str(round(k, 3)) + "%"))


conn.commit()

cur.close()
conn.close()