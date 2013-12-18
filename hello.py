#!usr/bin/python
class cal(object):

    def he(self, ls):
        a = ls[0]
        b = ls[1]
        c = ls[2]
        d = ls[3]
        if b == 0 or d == 0:
            print "NaN"
            return 0
        else:
            num = [a * d + b * c, b * d]
            self.yuefen(num)
            if(num[0] == 0):
                print "0"
                return 0
            elif num[1] == 1:
                print num[0]
                return 0
            print num[0]
            print num[1]

    def yuefen(self, lt):
        if lt[0] > lt[1]:
            h = lt[0]
        else:
            h = lt[1]
        i = 2
        while i <= h:
            if lt[0] % i == 0 and lt[1] % i == 0:
                lt[0] = lt[0] / i
                lt[1] = lt[1] / i
                self.yuefen(lt)
            i = i + 1
        return 0

print "enter four number: "
r = input()
begin = cal()
begin.he(r)


