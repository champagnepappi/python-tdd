class Calculator(object):
    def add(self,x,y):
        number_types = (int, long, float, complex)

        if isinstance(x,number_types) and isinstance(y, number_types):
            return x+y
            # print 'X is: {}'.format(x)
            # print 'Y is: {}'.format(y)
            # import pdb; pdb.set_trace()
            # print 'Result is: {}'.format(result)
            # return x - y
        else:
            raise ValueError
