class MyIterator(object):
    def __init__(self, step):
        self.step = step

    def next(self):
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        return self


def test_simple_iterator():
    simple_iter = MyIterator(4)
    for i in range(0,4):
        print simple_iter.next()

test_simple_iterator()
