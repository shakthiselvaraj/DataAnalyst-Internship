class even:

    def __init__(self,max):

        self.num = 2
        self.max = max

    def __iter__(self):

        return self

    def __next__(self):

        if self.num <= self.max:

            a = self.num
            self.num = self.num + 2
            return  a

        else:

            raise StopIteration

n = even(20)

for i in n:
    print(i)

