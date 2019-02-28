import math

class MyClass:
    def method_trtre(self):
        long_name = ""
        x = 0
        for x in range(33):
            long_name += "Agane"
            x += 1
        print(long_name)

    def method_input(self):
        x = ""
        while x != "Stop":
            x = input("Enter String?")
            if x != "Stop":
                print("Keep Going")
        print("Bye!")

    def method_sum(self):
        x = 0
        k = 1
        n = 1000
        inf = (math.pi ** 2) / 6
        while k <= n:
            x = 1 / k ** 2 + x
            if k == 10 or k == 100 or k == 1000:
                print("n =", k)
                print(x)
                print(inf - x)
                print("------------------------------------")
            k += 1


class_ref = MyClass()
#class_ref.method_trtre()
#print("############################################")
#class_ref.method_input()
#print("############################################")
#class_ref.method_sum()
