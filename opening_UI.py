from guizero import *
import datetime
import employee_UI
import changeDate_UI
import view_UI

class opening_UI:

    def __init__(self) -> None:
        self.open_page = App(title="三会员工工资编辑计算器", width=1200, height= 1000)
        Text(self.open_page, text='', size=20)
        Text(self.open_page, text='今天是:  '+datetime.date.today().strftime("%Y 年 %m 月 %d 号"), size=40)
        Text(self.open_page, text='', size=50)
        self.choices = Box(self.open_page, width=500, height=900)
        Text(self.choices, text='请选择以下操作：', size=30)
        Text(self.choices, text='', size=12)

    def choice(self):
        self.today = PushButton(self.choices, text='输入今日工资', height=2, width=500, command=self.todayButtonPress)
        self.today.text_size = 35
        Text(self.choices, text='', size=12)
        self.otherDate = PushButton(self.choices, text='修改其他日期工资', height=2, width=500, command=self.otherDateButtonPress)
        self.otherDate.text_size = 35
        Text(self.choices, text='', size=12)
        self.look = PushButton(self.choices, text='查     看', height=2, width=500, command=self.lookButtonPress)
        self.look.text_size = 35
        self.open_page.display()

    def todayButtonPress(self):
            self.open_page.destroy()
            employee_UI.employee_UI().edit()
            print('open 1')
            # return 1
        
    def otherDateButtonPress(self):
            self.open_page.destroy()
            changeDate_UI.changeDate_UI().chooseDate()
            print('open 2')
            # return 2

    def lookButtonPress(self):
            self.open_page.destroy()
            view_UI.view_UI().view_file()
            print('open 3')
            # return 3

opening_UI().choice()