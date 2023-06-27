#今天的工资
import os
import sys
from guizero import *
import workHour
import readfile
from openpyxl import load_workbook


class otherEmployee_UI:
    def __init__(self, timelist, yuangong):
        self.m_workHour = 0.0
        self.a_workHour = 0.0
        self.e_workHour = 0.0
        self.day_workHour = 0.0
        self.meal = 0
        self.year = timelist[0]
        self.month = timelist[1]
        self.day = timelist[2]
        print(self.year,self.month,self.day)
        self.employ_done = 1
        self.reachlast = False
        self.filename = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),"{}工资单.xlsx".format(self.year))
        self.list_wb = load_workbook(self.filename)
        self.sheet = self.list_wb["{}月".format(self.month)]
        self.employ_list, self.employ_dic = readfile.readfile(self.year,self.month,self.day)
        self.currentEmployee = self.employ_list.getHead()
        self.yuangong = Window(yuangong,title="{}月{}日员工工资".format(str(self.month),str(self.day)), width=1200, height= 1000)
        # self.yuangong = changeDate_UI.changeDate_UI().employeeButtonPress()
        Text(self.yuangong, text='', size=10)
        Text(self.yuangong, text='已选择: {} 年 {} 月 {} 号'.format(self.year,self.month,self.day), size=35)
        Text(self.yuangong, text='', size=5)
        self.name = Text(self.yuangong, text=self.currentEmployee.getName(), size = 38, bg = 'white')
        Text(self.yuangong, text='', size=5)
        self.shijian = Box(self.yuangong, height='fill', layout='grid')

        Text(self.shijian, text='上午:', size=25, grid=[0,1])
        self.morning_all = CheckBox(self.shijian, text='全勤 （8:00 - 11:30）', grid=[1,1])
        self.morning_all.text_size=20
        self.morning_no = CheckBox(self.shijian, text='请假', grid=[1,2])
        self.morning_no.text_size=20
        self.morning = CheckBox(self.shijian, text='如有请假，请输入上下班时间：', grid=[2,1])
        self.morning.text_size=20
        self.msText = Text(self.shijian, text='上班时间:', size=18, grid=[2,2])
        self.ms = TextBox(self.shijian, width=10, grid=[3,2])
        self.ms.text_size = 18
        self.meText = Text(self.shijian, text='下班时间:', size=18, grid=[2,3])
        self.me = TextBox(self.shijian, width=10, grid=[3,3])
        self.me.text_size = 18
        Text(self.shijian, text='', size=10, grid=[0,4])

        Text(self.shijian, text='下午:', size=25, grid=[0,5])   
        self.afternoon_all = CheckBox(self.shijian, text='全勤（12:00 - 17:30）', grid=[1,5])
        self.afternoon_all.text_size=20
        self.afternoon_no = CheckBox(self.shijian, text='请假', grid=[1,6])
        self.afternoon_no.text_size=20
        self.afternoon = CheckBox(self.shijian, text='如有请假，请输入上下班时间：', grid=[2,5])
        self.afternoon.text_size=20
        self.afsText = Text(self.shijian, text='上班时间:', size=18, grid=[2,6])
        self.afs = TextBox(self.shijian, width=10, grid=[3,6])
        self.afs.text_size = 18
        self.aeText = Text(self.shijian, text='下班时间:', size=18, grid=[2,7])
        self.ae = TextBox(self.shijian, width=10, grid=[3,7])
        self.ae.text_size = 18
        Text(self.shijian, text='', size=10, grid=[0,8])

        self.noExtra = CheckBox(self.shijian, text='不加班', grid=[0,10])
        self.noExtra.text_size=23
        self.evening_all = CheckBox(self.shijian, text='全勤（18:00 - 21:00）', grid=[1,10])
        self.evening_all.text_size=20
        self.evening = CheckBox(self.shijian, text='如有请假，请输入上下班时间：', grid=[2,10])
        self.evening.text_size=20
        self.esText = Text(self.shijian, text='上班时间:', size=18, grid=[2,11])
        self.es = TextBox(self.shijian, width=10, grid=[3,11])
        self.es.text_size = 18
        self.eeText = Text(self.shijian, text='下班时间:', size=18, grid=[2,12])
        self.ee = TextBox(self.shijian, width=10, grid=[3,12])
        self.ee.text_size = 18

        self.conclude = Text(self.yuangong, text='上午上班 ', size=27)

    def edit(self): 
        self.morning_all.update_command(command=self.choose_all_m)
        self.morning.update_command(command=self.choose_all_m)
        self.morning_no.update_command(command=self.choose_all_m)
        self.afternoon_all.update_command(command=self.choose_all_a)
        self.afternoon.update_command(command=self.choose_all_a)
        self.afternoon_no.update_command(command=self.choose_all_a)
        self.noExtra.update_command(command=self.choose_extra)
        self.evening_all.update_command(command=self.choose_all_e)
        self.evening.update_command(command=self.choose_all_e) 
        # print(self.m_workHour, self.a_workHour, self.e_workHour, self.m_workHour + self.a_workHour + self.e_workHour)
        yes = PushButton(self.yuangong, text='确      认', height='fill', width='fill', command=self.yesButtonPress)
        yes.text_size = 35
        reset = PushButton(self.yuangong, text='重      置', height='fill', width='fill', align='right', command=self.resetButtonPress, args=[self.shijian])
        reset.text_size = 35
        # self.yuangong.set_full_screen()
        # self.change.display()
    
    def yesButtonPress(self):
        self.currentEmployee.setWorkTime(self.day_workHour)
        # print(self.currentEmployee.getWorkTime())
        self.currentEmployee.setMeal(self.meal)
        print(self.currentEmployee.getWorkTime(), self.currentEmployee.getMeal())
        today_col = ''
        for head in self.sheet[1]:
            if head.value == self.day:
                today_col = head.coordinate.strip('1')
                # print(type(head.coordinate),head.coordinate.strip('1'))
        cell = today_col + str(self.employ_done+1)
        self.sheet[cell].value = self.day_workHour
                # print(cell, self.sheet[cell].value)
        meal = 'AK' + str(self.employ_done+1)
        self.sheet[meal].value = self.currentEmployee.getMeal()
        # print(meal,self.sheet[meal].value)
        print(self.currentEmployee)
        if self.currentEmployee is not None:
            if self.currentEmployee.next_employee is not None:
                self.name.clear()
                self.currentEmployee = self.currentEmployee.next_employee
                self.name.append(self.currentEmployee.getName())
                self.resetButtonPress(self.shijian)
                self.employ_done +=1
            else:
                self.reachlast = True
        self.end()
        # self.list_wb.save(self.filename)

    def end(self):
        if self.reachlast == True:
            self.yuangong.warn("结算结束", "下班！！！")
            self.list_wb.save(self.filename)
            self.yuangong.destroy()

            
    def choose_all_m(self):
        if self.morning_all.value == 1:
            self.m_workHour = workHour.fullTime_m()
            self.morning.disable()
            self.msText.disable()
            self.ms.disable()
            self.meText.disable()
            self.me.disable()
            self.morning_no.disable()
        elif self.morning.value == 1:
            self.m_workHour = workHour.workHour(self.ms.value,self.me.value)        
            self.morning_all.disable()
            self.morning_no.disable()
        elif self.morning_no.value == 1:
            self.m_workHour = 0.00
            self.morning.disable()
            self.msText.disable()
            self.ms.disable()
            self.meText.disable()
            self.me.disable()
            self.morning_all.disable()
        self.day_workHour = self.day_workHour + self.m_workHour
        self.conclude.append(str(self.m_workHour) + ' 小时，下午上班 ') 

    def choose_all_a(self):
        if self.afternoon_all.value == 1:
            self.a_workHour = workHour.fullTime_a()
            self.afternoon.disable()
            self.afsText.disable()
            self.afs.disable()
            self.aeText.disable()
            self.ae.disable()
            self.afternoon_no.disable()
        elif self.afternoon.value == 1:
            self.a_workHour = workHour.workHour(self.afs.value,self.ae.value)       
            self.afternoon_all.disable()
            self.afternoon_no.disable()
        elif self.afternoon_no.value == 1:
            self.a_workHour = 0.00
            self.afternoon_all.disable()
            self.afternoon.disable()
            self.afsText.disable()
            self.afs.disable()
            self.aeText.disable()
            self.ae.disable()
        self.day_workHour = self.day_workHour + self.a_workHour
        if self.m_workHour+self.a_workHour >= 6.5:
            self.meal += 8
        self.conclude.append(str(self.a_workHour) + ' 小时，') 

    def choose_all_e(self):
        if self.evening_all.value == 1:
            self.e_workHour = workHour.fullTime_e()
            self.evening.disable()
            self.esText.disable()
            self.es.disable()
            self.eeText.disable()
            self.ee.disable()
            self.noExtra.disable()
        elif self.evening.value == 1:
            self.e_workHour = workHour.workHour(self.es.value,self.ee.value)
            self.evening_all.disable()
            self.noExtra.disable()
        self.day_workHour = self.day_workHour + self.e_workHour
        if self.e_workHour >= 2:
            self.meal += 6
        self.conclude.append('加班 ' + str(self.e_workHour) + ' 小时，共计 ' + str(self.day_workHour) + ' 小时')
        
    def choose_extra(self):
        if self.noExtra.value == 1:
            self.evening_all.disable()
            self.evening.disable()
            self.esText.disable()
            self.es.disable()
            self.eeText.disable()
            self.ee.disable()
            self.conclude.append('不加班，共计 ' + str(self.day_workHour) + ' 小时')

    def resetButtonPress(self,box):
        self.day_workHour = 0.0
        self.meal = 0
        for widget in box.children:
            if type(widget) == CheckBox:
                # print(1,widget)
                widget.value = 0
                widget.enable()
            elif type(widget) == Text:
                # print(2,widget)
                widget.enable()
            else:
                # print(3,widget)
                widget.clear()
                widget.enable()
        self.conclude.clear() 
        self.conclude.append('上午上班 ')
        print('done')

# otherEmployee_UI([2023,6,1]).edit()