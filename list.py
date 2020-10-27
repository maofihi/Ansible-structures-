#Lists ordered, mutable,and allow duplicate elements

'''mylst = ["ale", "cherry", "lemn", "banana"]
mylst[0] = 'Apple'
print(mylst)

mylst2 = list()
print(mylst2)
mylst3 = [5, True, "ale", "ale"]
print(mylst3)
tem = mylst3[0]
print(tem)
tem2 = mylst[-1]
print(tem2)
for x in mylst:
    print(x)

if "alee" in mylst:
    print("Y")
else:
    print("N")
print(len(mylst))
mylst.append("orange")
print(mylst)
mylst.insert(2, "blueberry")
print(mylst)
tem3 = mylst.pop()
print(tem3)
print(mylst)
mylst.remove("lemn")
print(mylst)
mylst.clear()
print(mylst)
mylst3.reverse()
print(mylst3)
#mylst3.sort()
print(mylst3)
mylst2.append(2)
mylst2.insert(1,8)
print(mylst2)
mylst4 = [2, 5, 6, 7, 8, 9]
newmylst2 = mylst2 + mylst4
print(newmylst2)
newmylst2.sort()
print(newmylst2)
a = newmylst2[2:5]
b = newmylst2[:5]
c = newmylst2[2:]
d = newmylst2[::1]
f = newmylst2[::2]
e = newmylst2[::-1]
e_copy = e[:]
newmylst3 = e.copy()
e_copy.append(0)
print(a)
print(b)
print(c)
print(d)
print(f)
print(e)
print(newmylst3)
print(e_copy)
print(e)
print(newmylst3)
g = [x*x for x in e]# called List Comprehension
ee1 = [x*3 for x in e] # called List Comprehension
print(g)
ee2 = e*2
print(ee1)'''

# users = [{'name': 'mele', 'age': 31}, {'name': 'max', 'age': 29}, {'name': 'manuel', 'age': 38}]
# user_name = [user['name'] for user in users if user['age'] > 30]
# print(user_name)
user_groups = [
    [
        {'name': 'mele', 'age': 31, 'sex': 'M'}, {'name': 'max', 'age': 29, 'sex':'M'}
    ],
    [
        {'name': 'sara', 'age': 28, 'sex': 'F'}, {'name': 'nani', 'age': 32, 'sex': 'F'}
    ]
]
user_nameallf = [user for group in user_groups for user in group if user['sex'] == 'F']
print(user_nameallf)
user_namef = [user['name'] for group in user_groups for user in group if user['sex'] == 'F']
print(user_namef)
user_name = [user for group in user_groups for user in group]

for tm in user_name:
    print(tm)

l = [1, 2, 3, 5, 6, 7, 8, 10, 11]
L = l[-5:]
L3 = l[:5]
L2 = l[0:-1:3]
L4 = l[0:-2]
L5 = l[0:-1:2]
print(L2)
print(L3)
print(L)
my_lst = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):

    for y in range(0,3):
        print(my_lst[x][y])

def getList(max):
    x = list(range(max))
    for i in x:
        x[i] = i*5
    return x

my_lst1 = getList(30)
print(my_lst1)
