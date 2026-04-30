class Parent:
    a = 1

    @classmethod
    def show(cls):
        print(cls.a)

p = Parent()
p.a = 45
p.show()  # output :1


class Parent:
    a = 1

    def show(self):
        print(self.a)

p = Parent()
p.a = 45
p.show() # output : 45


