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

if __name__ == '__main__':
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
#############################################################################
class Set:
    def init(self):
        self.hashSet = set()

    def add(self, newElement):
        self.hashSet.add(newElement)

    def remove(self, element):
        self.hashSet.discard(element)

    def contains(self, element):
        return element in self.hashSet

    def size(self):
        return len(self.hashSet)

    def iterator(self):
        return iter(self.hashSet)

    def intersection(self, otherSet):
        result = Set()
        for element in self.hashSet:
            if otherSet.contains(element):
                result.add(element)
        return result

    def union(self, otherSet):
        result = Set()
        result.hashSet = self.hashSet.union(otherSet.hashSet)
        return result

    def difference(self, otherSet):
        result = Set()
        for element in self.hashSet:
            if not otherSet.contains(element):
                result.add(element)
        return result

    def subset(self, otherSet):
        return self.hashSet.issubset(otherSet.hashSet)


# Test the Set implementation
set1 = Set()
set1.add(1)
set1.add(2)
set1.add(3)

set2 = Set()
set2.add(2)
set2.add(3)
set2.add(4)

# Test operations
print("Set 1 Size:", set1.size())
print("Set 2 Size:", set2.size())

print("Intersection:", end=" ")
intersection = set1.intersection(set2)
for element in intersection.iterator():
    print(element, end=" ")
print()

print("Union:", end=" ")
union_set = set1.union(set2)
for element in union_set.iterator():
    print(element, end=" ")
print()

print("Difference:", end=" ")
difference = set1.difference(set2)
for element in difference.iterator():
    print(element, end=" ")
print()


print("Subset:", set1.subset(set2))
