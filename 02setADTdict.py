def initialize_hash_table():
    return [{'key': -1, 'name': 'NULL'} for _ in range(10)]

def insert(h):
    cnt = 0
    flag = 0
    while True:
        if cnt >= 10:
            print("\n\tHash Table is FULL")
            break
        k = int(input("\n\tEnter a Telephone No: "))
        n = input("\n\tEnter a Client Name: ")
        hi = k % 10  # hash function
        if h[hi]['key'] == -1:
            h[hi]['key'] = k
            h[hi]['name'] = n
        else:
            if h[hi]['key'] % 10 != hi:
                temp = h[hi]['key']
                ntemp = h[hi]['name']
                h[hi]['key'] = k
                h[hi]['name'] = n
                for i in range(hi + 1, 10):
                    if h[i]['key'] == -1:
                        h[i]['key'] = temp
                        h[i]['name'] = ntemp
                        flag = 1
                        break
                for i in range(hi):
                    if flag == 0 and h[i]['key'] == -1:
                        h[i]['key'] = temp
                        h[i]['name'] = ntemp
                        break
            else:
                for i in range(hi + 1, 10):
                    if h[i]['key'] == -1:
                        h[i]['key'] = k
                        h[i]['name'] = n
                        flag = 1
                        break
                for i in range(hi):
                    if flag == 0 and h[i]['key'] == -1:
                        h[i]['key'] = k
                        h[i]['name'] = n
                        break
        flag = 0
        cnt += 1
        ans = input("\n\t..... Do You Want to Insert More Key: y/n: ")
        if ans != 'y' and ans != 'Y':
            break

def display(h):
    print("\n\t\tKey\t\tName")
    for i in range(10):
        print("\n\th[{}]\t{}\t\t{}".format(
            i, h[i]['key'], h[i]['name']))

def find(h, k):
    for i in range(10):
        if h[i]['key'] == k:
            print("\n\t{} is Found at {} Location With Name {}".format(
                h[i]['key'], i, h[i]['name']))
            return i
    print("\n\tKey Not Found")
    return -1

def delete(h, k):
    index = find(h, k)
    if index != -1:
        h[index]['key'] = -1
        h[index]['name'] = "NULL"
        print("\n\tKey is Deleted")

if _name_ == '_main_':
    h = initialize_hash_table()
    while True:
        print("\n\t***** Telephone (ADT) *****")
        print("\n\t1. Insert\n\t2. Display\n\t3. Find\n\t4. Delete\n\t5. Exit")
        ch = int(input("\n\t..... Enter Your Choice: "))
        if ch == 1:
            insert(h)
        elif ch == 2:
            display(h)
        elif ch == 3:
            find(h, k)
        elif ch == 4:
            k = int(input("\n\tEnter a Key Which You Want to Delete: "))
            delete(h, k)
        elif ch == 5:
            break
        ans = input("\n\t..... Do You Want to Continue in Main Menu: y/n: ")
        if ans != 'y' and ans != 'Y':
            break
