#今天的工资
import os
import sys
from guizero import *
import workHour
import readfile
import openpyxl

class employee_UI:
    def __init__(self):
        self.m_workHour = 0.0
        self.a_workHour = 0.0
        self.e_workHour = 0.0
        self.day_workHour = 0.0
        self.meal = 0
        self.year = readfile.getDate()[0]
        self.month = readfile.getDate()[1]
        self.day = readfile.getDate()[2]
        self.employ_done = 1
        self.reachlast = False
        self.filename = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),"{}工资单.xlsx".format(self.year))
        self.list_wb = openpyxl.load_workbook(self.filename)
        self.sheet = self.list_wb["{}月".format(self.month)]
        self.employ_list, self.employ_dic = readfile.readfile(self.year,self.month,self.day)
        # print(self.employ_list)
        self.currentEmployee = self.employ_list.getHead()
        self.yuangong = App(title="今日员工工资", width=1200, height= 1000)
        Text(self.yuangong, text='', size=10)
        Text(self.yuangong, text='今天是: {} 年 {} 月 {} 号'.format(self.year,self.month,self.day), size=35)
        Text(self.yuangong, text='', size=5)
        self.name = Text(self.yuangong, text=self.currentEmployee.getName(), size=38, bg = 'white')
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

    def deleteButtonPress(self):      
        this_row = ''
        for each_name in self.sheet["B"]:
            if each_name.value == self.currentEmployee.getName():
                this_row = int(each_name.coordinate[1])
                self.sheet.delete_rows(idx=this_row)     
        self.list_wb.save(self.filename)
        if self.currentEmployee.next_employee is not None:
            self.name.clear()
            self.currentEmployee = self.currentEmployee.next_employee  
            self.name.append(self.currentEmployee.getName())
        else:
            self.reachlast = True
            self.end()
        self.employ_dic.pop(self.currentEmployee.getName())
        print('已删除')

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
        button_box = Box(self.yuangong, height='fill', width='fill')
        delete = PushButton(button_box, text='删除该员工', height='fill', width='fill', align='left', command=self.deleteButtonPress)
        delete.text_size = 30
        reset = PushButton(button_box, text='重      置', height='fill', width='fill', align='right', command=self.resetButtonPress, args=[self.shijian])
        reset.text_size = 35  
        # self.yuangong.set_full_screen()
        self.yuangong.display()
    
    def yesButtonPress(self):
        self.currentEmployee.setWorkTime(self.day_workHour)
        self.currentEmployee.setMeal(self.meal)
        print(self.currentEmployee.getWorkTime(), self.currentEmployee.getMeal())
        today_col = ''
        for head in self.sheet[1]:
            if head.value == self.day:
                today_col = head.coordinate.strip('1')
                # print(type(head.coordinate),head.coordinate[0])
        cell = today_col + str(self.employ_done+1)
        self.sheet[cell].value = self.day_workHour
        meal = 'AK' + str(self.employ_done+1)
        self.sheet[meal].value = self.currentEmployee.getMeal()
        # print(cell, self.sheet[cell].value)
        print(self.currentEmployee)
        if self.currentEmployee is not None:
            if self.currentEmployee.next_employee is not None:
                self.name.clear()
                self.currentEmployee = self.currentEmployee.next_employee
                self.name.append(self.currentEmployee.getName())
                self.resetButtonPress(self.shijian)
                self.employ_done += 1
            else:
                self.reachlast = True
        self.end()
        # self.list_wb.save(self.filename)

    def end(self):
        if self.reachlast == True:
             add = self.yuangong.yesno("结算结束", "是否添加员工？")
             if add == True:
                 self.reachlast = False
                 add_name = self.yuangong.question('添加员工','请输入添加人员：姓名，时薪')
                 if add_name is not None:
                     self.employ_done += 1
                     add_n = add_name.split('，')[0]
                     add_s = float(add_name.split('，')[1])
                     self.employ_list.addEmployee(add_n,add_s,0.0,0,0,0)
                     self.name.clear()
                     self.currentEmployee = self.currentEmployee.next_employee
                     self.name.append(self.currentEmployee.getName())
                     max_row = self.sheet.max_row + 1
                     print(max_row)
                     id = max_row - 1
                     row_data = [id, add_n, add_s]
                     for i in range(1,32):
                         row_data.append(0.0)
                     row_data.append('=SUM(D{}:AH{})'.format(str(max_row),str(max_row)))
                     row_data.append('=C{}*AI{}'.format(str(max_row),str(max_row)))
                     row_data.append(0.00)
                     row_data.append('=AJ{}+AK{}'.format(str(max_row),str(max_row)))
                     self.sheet.append(row_data) 
             else:
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
        elif self.morning.value == 1:
            self.m_workHour = workHour.workHour(self.ms.value,self.me.value)        
            self.morning_all.disable()
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
        elif self.afternoon.value == 1:
            self.a_workHour = workHour.workHour(self.afs.value,self.ae.value)       
            self.afternoon_all.disable()
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
        self.conclude.append(str(self.a_workHour) + ' 小时') 

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
        self.conclude.append('加班 ' + str(self.e_workHour) + ' 小时，共计 ' + str(self.day_workHour) + ' 小时，')
        
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
        print('reset')

# employee_UI().edit()