from guizero import *
import employee_UI
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
            employee = PushButton(self.date_page, text='选择员工', width='fill', height='fill', command=self.employeeButtonPress)
            employee.text_size = 35
            today = PushButton(self.date_page, text='返回今天日期', width='fill', height='fill', command=self.todayButtonPress)
            today.text_size = 35
            self.date_page.display() 

    def todayButtonPress(self):
            self.date_page.destroy()
            employee_UI.employee_UI().edit()
            print('today')
            return 'today'
    
    def employeeButtonPress(self):
          timeList = [int(self.year.value),int(self.month.value),int(self.day.value)]
          otherEmployee_UI.otherEmployee_UI(timeList,self.date_page).edit()

# changeDate_UI().chooseDate()