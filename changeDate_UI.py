from guizero import *
import employee_UI
from openpyxl import *
import otherEmployee_UI

class changeDate_UI:

    def __init__(self) -> None:
        self.date_page = App(title="选择日期", width=1200, height= 1000)
        Text(self.date_page, text='', size=50)
        self.datebox = Box(self.date_page, width='fill', height='fill')
        Text(self.datebox, text='      请输入日期：', size=35, align='left')
        self.year = TextBox(self.datebox, width=4, align='left')
        self.year.text_size = 30
        Text(self.datebox, text=' 年 ', size=30, align='left')
        self.month = TextBox(self.datebox, width=2, align='left')
        self.month.text_size = 30
        Text(self.datebox, text=' 月 ', size=30, align='left')
        self.day = TextBox(self.datebox, width=2, align='left')
        self.day.text_size = 30
        Text(self.datebox, text=' 日    ', size=30, align='left')
               
    def chooseDate(self):
            employee = PushButton(self.date_page, text='选择员工', command=self.employeeButtonPress)
            employee.text_size = 35
            today = PushButton(self.date_page, text='返回今天日期', command=self.todayButtonPress)
            today.text_size = 35
            self.date_page.display() 

    def todayButtonPress(self):
            self.date_page.destroy()
            employee_UI.employee_UI().edit()
            print('today')
            return 'today'
    
    def getAPP(self):
        return self.date_page
    
    def employeeButtonPress(self):
          timeList = [int(self.year.value),int(self.month.value),int(self.day.value)]
          self.date_page.destroy()
          otherEmployee_UI.otherEmployee_UI(timeList).edit()

# changeDate_UI().chooseDate()
"""  def employeeButtonPress(self):
        m_workHour = 0.0
        a_workHour = 0.0
        e_workHour = 0.0
        day_workHour = 0.0
        employ_done = 1
        reachlast = False
        year = int(self.year.value)
        month = int(self.month.value)
        day = int(self.day.value)
        filename = "/Users/xinyixu/Desktop/工资/{}工资单.xlsx".format(str(year))
        list_wb = load_workbook(filename)
        sheet = self.list_wb["{}月".format(str(month))]
        employ_list, employ_dic = readfile.readfile(year,month,day)
        currentEmployee = employ_list.getHead()
        yuangong = Window(self.date_page, title="{}月{}日员工工资".format(str(month),str(day)), width=1200, height= 1000)
        Text(yuangong, text='', size=10)
        Text(yuangong, text='已选择: {} 年 {} 月 {} 号'.format(year,month,day), size=35)
        Text(yuangong, text='', size=5)
        name = Text(yuangong, text=currentEmployee.getName(), size = 38, bg = 'white')
        Text(yuangong, text='', size=5)
        shijian = Box(yuangong, height='fill', layout='grid')

        Text(shijian, text='上午:', size=25, grid=[0,1])
        morning_all = CheckBox(shijian, text='全勤 （8:00 - 11:30）', grid=[1,1])
        morning_all.text_size=20
        morning_no = CheckBox(shijian, text='请假', grid=[1,2])
        morning_no.text_size=20
        morning = CheckBox(shijian, text='如有请假，请输入上下班时间：', grid=[2,1])
        morning.text_size=20
        msText = Text(shijian, text='上班时间:', size=18, grid=[2,2])
        ms = TextBox(shijian, width=10, grid=[3,2])
        ms.text_size = 18
        meText = Text(shijian, text='下班时间:', size=18, grid=[2,3])
        me = TextBox(shijian, width=10, grid=[3,3])
        me.text_size = 18
        Text(shijian, text='', size=10, grid=[0,4])

        Text(shijian, text='下午:', size=25, grid=[0,5])   
        afternoon_all = CheckBox(shijian, text='全勤（12:00 - 17:30）', grid=[1,5])
        afternoon_all.text_size=20
        afternoon_no = CheckBox(shijian, text='请假', grid=[1,6])
        afternoon_no.text_size=20
        afternoon = CheckBox(shijian, text='如有请假，请输入上下班时间：', grid=[2,5])
        afternoon.text_size=20
        afsText = Text(shijian, text='上班时间:', size=18, grid=[2,6])
        afs = TextBox(shijian, width=10, grid=[3,6])
        afs.text_size = 18
        aeText = Text(shijian, text='下班时间:', size=18, grid=[2,7])
        ae = TextBox(shijian, width=10, grid=[3,7])
        ae.text_size = 18
        Text(shijian, text='', size=10, grid=[0,8])

        noExtra = CheckBox(shijian, text='今天不加班', grid=[0,9])
        noExtra.text_size=23
        extra = CheckBox(shijian, text='加班：', grid=[0,10])
        extra.text_size=23
        evening_all = CheckBox(shijian, text='全勤（18:00 - 21:00）', grid=[1,10])
        evening_all.text_size=20
        evening = CheckBox(shijian, text='如有请假，请输入上下班时间：', grid=[2,10])
        evening.text_size=20
        esText = Text(shijian, text='上班时间:', size=18, grid=[2,11])
        es = TextBox(shijian, width=10, grid=[3,11])
        es.text_size = 18
        eeText = Text(shijian, text='下班时间:', size=18, grid=[2,12])
        ee = TextBox(shijian, width=10, grid=[3,12])
        ee.text_size = 18

        conclude = Text(yuangong, text='上午上班 ', size=27)
        button_box = Box(yuangong, height='fill', width='fill')
        reset = PushButton(button_box, text='重      置', height='fill', width='fill', command=self.resetButtonPress, args=[self.employeeButtonPress.shijian])
        reset.text_size = 35
        yes = PushButton(button_box, text='确      认', height='fill', width='fill', command=self.yesButtonPress)
        yes.text_size = 35
        self.edit()
        yuangong.display()
        
    def edit(self):       
        self.employeeButtonPress.morning_all.update_command(command=self.choose_all_m)
        self.employeeButtonPress.morning.update_command(command=self.choose_all_m)
        self.employeeButtonPress.morning_no.update_command(command=self.choose_all_m)
        self.employeeButtonPress.afternoon_all.update_command(command=self.choose_all_a)
        self.employeeButtonPress.afternoon.update_command(command=self.choose_all_a)
        self.employeeButtonPress.afternoon_no.update_command(command=self.choose_all_a)
        self.employeeButtonPress.noExtra.update_command(command=self.choose_extra)
        self.employeeButtonPress.extra.update_command(command=self.choose_extra)
        self.employeeButtonPress.evening_all.update_command(command=self.choose_all_e)
        self.employeeButtonPress.evening.update_command(command=self.choose_all_e)  
        # print(m_workHour, a_workHour, e_workHour, m_workHour + a_workHour + e_workHour)
        self.employeeButtonPress.reset.update_command(command=self.resetButtonPress, args=[self.employeeButtonPress.shijian])
        self.employeeButtonPress.yes.update_command(command=self.yesButtonPress)
        # yuangong.set_full_screen()
        # self.employeeButtonPress.yuangong.display()
    
    def yesButtonPress(self):
        self.employeeButtonPress.currentEmployee.setWorkTime(self.employeeButtonPress.day_workHour)
        # print(currentEmployee.getWorkTime())
        # print(currentEmployee.getMeal())
        today_col = ''
        for head in self.employeeButtonPress.sheet[1]:
            if head.value == self.employeeButtonPress.day:
                today_col = head.coordinate.strip('1')
                # print(type(head.coordinate),head.coordinate.strip('1'))
        cell = today_col + str(self.employeeButtonPress.employ_done+1)
        self.employeeButtonPress.sheet[cell].value = self.employeeButtonPress.day_workHour
                # print(cell, sheet[cell].value)
        meal = 'AK' + str(self.employeeButtonPress.employ_done+1)
        self.employeeButtonPress.sheet[meal].value = self.employeeButtonPress.currentEmployee.getMeal()
        # print(meal,sheet[meal].value)
        print(self.employeeButtonPress.currentEmployee)
        if self.employeeButtonPress.currentEmployee is not None:
            if self.employeeButtonPress.currentEmployee.next_employee is not None:
                self.employeeButtonPress.name.clear()
                self.employeeButtonPress.currentEmployee = self.employeeButtonPress.currentEmployee.next_employee
                self.employeeButtonPress.name.append(self.employeeButtonPress.currentEmployee.getName())
                self.resetButtonPress(self.employeeButtonPress.shijian)
                self.employeeButtonPress.employ_done +=1
            else:
                self.employeeButtonPress.reachlast = True
        self.end()
        # list_wb.save(filename)

    def end(self):
        if self.employeeButtonPress.reachlast == True:
            self.employeeButtonPress.yuangong.warn("结算结束", "下班！！！")
            self.employeeButtonPress.list_wb.save(self.employeeButtonPress.filename)
            self.employeeButtonPress.yuangong.destroy()
           
    def choose_all_m(self):
        if self.employeeButtonPress.morning_all.value == 1:
            self.employeeButtonPress.m_workHour = workHour.fullTime_m()
            self.employeeButtonPress.morning.disable()
            self.employeeButtonPress.msText.disable()
            self.employeeButtonPress.ms.disable()
            self.employeeButtonPress.meText.disable()
            self.employeeButtonPress.me.disable()
            self.employeeButtonPress.morning_no.disable()
        elif self.employeeButtonPress.morning.value == 1:
            self.employeeButtonPress.m_workHour = workHour.workHour(self.employeeButtonPress.ms.value,self.employeeButtonPress.me.value)        
            self.employeeButtonPress.morning_all.disable()
            self.employeeButtonPress.morning_no.disable()
        elif self.employeeButtonPress.morning_no.value == 1:
            self.employeeButtonPress.m_workHour = 0.00
            self.employeeButtonPress.morning.disable()
            self.employeeButtonPress.msText.disable()
            self.employeeButtonPress.ms.disable()
            self.employeeButtonPress.meText.disable()
            self.employeeButtonPress.me.disable()
            self.employeeButtonPress.morning_all.disable()
        self.employeeButtonPress.day_workHour = self.employeeButtonPress.day_workHour + self.employeeButtonPress.m_workHour
        self.employeeButtonPress.conclude.append(str(self.employeeButtonPress.m_workHour) + ' 小时，下午上班 ') 

    def choose_all_a(self):
        if self.employeeButtonPress.afternoon_all.value == 1:
            self.employeeButtonPress.a_workHour = workHour.fullTime_a()
            self.employeeButtonPress.afternoon.disable()
            self.employeeButtonPress.afsText.disable()
            self.employeeButtonPress.afs.disable()
            self.employeeButtonPress.aeText.disable()
            self.employeeButtonPress.ae.disable()
            self.employeeButtonPress.afternoon_no.disable()
        elif self.employeeButtonPress.afternoon.value == 1:
            self.employeeButtonPress.a_workHour = workHour.workHour(self.employeeButtonPress.afs.value,self.employeeButtonPress.ae.value)       
            self.employeeButtonPress.afternoon_all.disable()
            self.employeeButtonPress.afternoon_no.disable()
        elif self.employeeButtonPress.afternoon_no.value == 1:
            self.employeeButtonPress.a_workHour = 0.00
            self.employeeButtonPress.afternoon_all.disable()
            self.employeeButtonPress.afternoon.disable()
            self.employeeButtonPress.afsText.disable()
            self.employeeButtonPress.afs.disable()
            self.employeeButtonPress.aeText.disable()
            self.employeeButtonPress.ae.disable()
        self.employeeButtonPress.day_workHour = self.employeeButtonPress.day_workHour + self.employeeButtonPress.a_workHour
        if self.employeeButtonPress.m_workHour+self.employeeButtonPress.a_workHour >= 6.5:
            self.employeeButtonPress.currentEmployee.setMeal(8)
        self.employeeButtonPress.conclude.append(str(self.employeeButtonPress.a_workHour) + ' 小时') 

    def choose_all_e(self):
        if self.employeeButtonPress.evening_all.value == 1:
            self.employeeButtonPress.e_workHour = workHour.fullTime_e()
            self.employeeButtonPress.evening.disable()
            self.employeeButtonPress.esText.disable()
            self.employeeButtonPress.es.disable()
            self.employeeButtonPress.eeText.disable()
            self.employeeButtonPress.ee.disable()
        elif self.employeeButtonPress.evening.value == 1:
            e_workHour = self.employeeButtonPress.workHour.workHour(self.employeeButtonPress.es.value,self.employeeButtonPress.ee.value)
            self.employeeButtonPress.evening_all.disable()
        self.employeeButtonPress.day_workHour = self.employeeButtonPress.day_workHour + self.employeeButtonPress.e_workHour
        if e_workHour >= 2:
            self.employeeButtonPress.currentEmployee.setMeal(6)
        self.employeeButtonPress.conclude.append(str(self.employeeButtonPress.e_workHour) + ' 小时，共计 ' + str(self.employeeButtonPress.day_workHour) + ' 小时')
        
    def choose_extra(self):
        if self.employeeButtonPress.noExtra.value == 1:
            self.employeeButtonPress.extra.disable()
            self.employeeButtonPress.evening_all.disable()
            self.employeeButtonPress.evening.disable()
            self.employeeButtonPress.esText.disable()
            self.employeeButtonPress.es.disable()
            self.employeeButtonPress.eeText.disable()
            self.employeeButtonPress.ee.disable()
            self.employeeButtonPress.conclude.append('，共计 ' + str(self.employeeButtonPress.day_workHour) + ' 小时')
        elif self.employeeButtonPress.extra.value == 1:
            self.employeeButtonPress.noExtra.disable()
            self.employeeButtonPress.conclude.append('，加班 ')

    def resetButtonPress(self,box):
        self.employeeButtonPress.day_workHour = 0.0
        for widget in self.employeeButtonPress.box.children:
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
        self.employeeButtonPress.conclude.clear() 
        self.employeeButtonPress.conclude.append('上午上班 ') """