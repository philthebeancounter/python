from datetime import date
from datetime import timedelta
from datetime import datetime

#def employee_entitlement_irreg_hours(result,company_entitlement):





#inputs
data=open('data.txt','a')
name_input = raw_input("name> ")
company_entitlement = input ("Annual entitlement >")


bh1 = date(2017,1,2)
bh2 = date(2017,4,14)
bh3 = date(2017,4,17)
bh4 = date(2017,5,1)
bh5 = date(2017,5,29)
bh6 = date(2017,8,28)
bh7 = date(2017,12,25)
bh8 = date(2017,12,26)

bank_holidays = [bh1,bh2,bh3,bh4,bh5,bh6,bh7,bh8]

#calculates hours per week and no of days workedk





#print "Hours per week", Hours
#print "No of days worked", Days_worked
#print "daily hours",Daily_hours
#bank holidays falling in working pattern

#bh_to_take = []

##for i in bank_holidays:
#    day = i.weekday()
#    if day==0 and Contracted_hours['Monday'] > 0:
#        bh_to_take.append(i)
#    elif day==1 and Contracted_hours['Tuesday'] > 0:
#        bh_to_take.append(i)
#    elif day == 2 and Contracted_hours['Wednesday'] > 0:
#        bh_to_take.append(i)
#    elif day == 3 and Contracted_hours['Thursday'] > 0:
#        bh_to_take.append(i)
#    elif day == 4 and Contracted_hours['Friday'] > 0:
#        bh_to_take.append(i)
#    elif day == 5 and Contracted_hours['Saturday'] > 0:
#        bh_to_take.append(i)
#    elif day == 6 and Contracted_hours['Sunday'] > 0:
#        bh_to_take.append(i)
#print bh_to_take

#Hours = 0
class Employee(object):



    def hours(self,uninque_daily_hours_count):

        #Daily_hours = []
        #self.Hours = Hours
        self.uninque_daily_hours_count= uninque_daily_hours_count
        Days_worked = 0
        dw = 0
        for i,v in self.Contracted_hours.iteritems():
            self.Hours = self.Hours + v

            Days_worked = Days_worked + dw
            if v == 0:
                dw = 0
            else:
                dw = 1
            if v > 0:
                self.Daily_hours.append(v)

        #test whether the working week is reguar hours or irregular hours
        uninque_daily_hours = set(self.Daily_hours)
        self.uninque_daily_hours_count = len(uninque_daily_hours)
        print uninque_daily_hours_count
        if self.uninque_daily_hours_count == 1:
            print "regular hours"
        else:
            print "irreguar hours"
        return self.Hours,self.uninque_daily_hours_count



    def __init__(self,name,company_entitlement):
        Hours = 0
        self.name = name
        self.company_entitlement = company_entitlement
        self.Hours = Hours
        self.Daily_hours = []
        self.Contracted_hours = {'Monday':7,'Tuesday':8.5,'Wednesday':8.5,'Thursday':8.5,'Friday':8.5,'Saturday':0,'Sunday':0}
    #def add_hol(self,days):
        #self.hol_allowance = self.hol_allowance - days


    def employee_entitlement_irreg_hours(self):
        #Hours = employee.hours()
        #self.Hours = Hours
        #self.company_entitlement = company_entitlement
        return self.Hours * self.company_entitlement / 5.0 + self.uninque_daily_hours_count

#print employee.name
#data.write(employee.name)
#data.write(str(employee.hol_allowance))
#print employee.hol_allowance


f = open('import.txt',"r")
line = f.readline()
while line:
    print line
    line = f.readline()
f.close()

employee = Employee(name_input,company_entitlement)
print employee.name
print employee.Contracted_hours
print  "hours", employee.hours(0)
print "class calculation", employee.employee_entitlement_irreg_hours()
