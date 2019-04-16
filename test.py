class Parent:
    _attr = 1  # == Инкапсуляция ==#

    def get_attr(self):
        print("Parent Attr: " + str(self._attr))


class Another_class:
    attr = 3

    def get_attr(self):  # == Полиморфизм ==#
        print("Another: " + str(self.attr))


class Child(Parent):  # == Наследование ==#
    attr = 2
    New_obj = Another_class()

    def get_attr(self):  # == Полиморфизм ==#
        print("Child Attr: " + str(self.attr))

    def new_obj(self):
        return self.New_obj


p = Parent()
p.get_attr()

c = Child()
c.get_attr()

n = c.new_obj()
n.get_attr()

lm = lambda arr_len: [0 if i % 2 == 0 else 1 for i in range(arr_len)]
print(lm(5))
