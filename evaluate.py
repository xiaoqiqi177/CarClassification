#!/usr/bin/python
import sys
ww = {}

ww['whole'] = int(sys.argv[1])
ww['front'] = int(sys.argv[2])
ww['back'] = int(sys.argv[3])
ww['tire'] = int(sys.argv[4])
ww['logo'] = int(sys.argv[5])
cars = []
search = {}

class part_class:
    __kind = ''
    __a6l_p = .0
    __accord_p = .0
    def __init__(self, which_part, k, p, cut_p):
        self.__kind = which_part
        if k == 'a6l':
            self.__a6l_p = p * cut_p
            self.__accord_p = (1-p)*cut_p
        else:
            self.__accord_p = p * cut_p
            self.__a6l_p = (1-p) * cut_p
    def getkind(self):
        return self.__kind
    def get_a6l_accu(self):
        return self.__a6l_p
    def get_accord_accu(self):
        return self.__accord_p

class car_class:
    def __init__(self, n):
        self.__name = n
        endd = -1
        while n[endd].isdigit():
            endd -= 1
        self.__actual = n[:endd+1]
        self.__parts = []
        self.__predict_result = ''
        self.__predict_probability = .0
        self.__ifright = False
    def add_part(self, tmp):
        self.__parts.append(tmp)
    def cal(self):
        a6l_ans = .0
        accord_ans = .0
        #for pa in self.__parts:
	#	a6l_ans = a6l_ans + ww[pa.getkind()]*pa.get_a6l_accu()
	#	accord_ans = accord_ans + ww[pa.getkind()]*pa.get_accord_accu()
        for pa in self.__parts:
            if pa.get_a6l_accu() > 0.8 or pa.get_accord_accu() > 0.8:
                a6l_ans = a6l_ans + ww[pa.getkind()]*pa.get_a6l_accu()
                accord_ans = accord_ans + ww[pa.getkind()]*pa.get_accord_accu()
        if a6l_ans < accord_ans:
            self.__predict_result = 'accord'
        else:
            self.__predict_result = 'a6l'
        if self.__predict_result == self.__actual:
            self.__ifright = True
    def printt(self):
        print '------------------'
        print self.__predict_result
        #print self.__actual
        #print len(self.__parts)
        #print self.__ifright
    def testfy(self):
        return self.__ifright
    def getactual(self):
        return self.__actual

record = open('result_test/result_record/record.txt', 'r')
f = open('all.txt','r')

while True:
    part = f.readline()
    result = f.readline()
    correct = f.readline()#pass CORRECT
    test = f.readline()#passs empty line
    relation = record.readline()
    if test != '\n':
        break
    part_type = relation.split()[2]
    car_name = relation.split()[1]
    part_pred_type = result.split()[0].split(':')[1].lower()
    part_pred_accu = result.split()[2].split(':')[1]
    part_cut_accu = result.split()[3].split(':')[1]

    if car_name in search:
        ln = search[car_name]
    else:
        cars.append(car_class(car_name))
        search[car_name] = len(cars)-1
        ln = len(cars)-1
    tmp = part_class(part_type, part_pred_type, float(part_pred_accu), float(part_cut_accu))    
    cars[ln].add_part(tmp)

f.close()
record.close()

right_No = 0
A6L_No = 0
ACCORD_No = 0
right_A6L_No = 0
right_ACCORD_No = 0
total_No = 0

for ob in cars:
    total_No += 1
    ob.cal()
    ob.printt()
'''
    if ob.getactual() == 'a6l':
        A6L_No += 1
        if ob.testfy() == True:
            right_No += 1
            right_A6L_No += 1
    else:
        ACCORD_No += 1
        if ob.testfy() == True:
            right_No += 1
            right_ACCORD_No += 1
'''
'''
print 'A6L_Right_No/A6L_No: ', right_A6L_No, '/',A6L_No
print 'A6L_Accuracy: ', right_A6L_No*1.0/A6L_No
print 'ACCORD_Right_No/ACCORD_No: ', right_ACCORD_No, '/', ACCORD_No
print 'ACCORD_Accuracy: ', right_ACCORD_No*1.0/ACCORD_No
print 'Right_No/total_No: ', right_No, '/', total_No
print 'Accuracy: ', right_No*1.0/total_No
'''
