# can inheret list as the subclass of SuperList therefor adopting all it's attributes and methods.
# before I passed list as a parameter in the class SuperList I was getting errors for list methods like len on line 8
class SuperList(list):
    def __len__(self):
        return 10000
    
super_list1 = SuperList()
print(len(super_list1))
print(super_list1.append(5))
print(super_list1.append(6))
print(super_list1[0])
print(super_list1[1])

print(issubclass(SuperList, list))