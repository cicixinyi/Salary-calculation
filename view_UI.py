from guizero import *
import readfile

class view_UI:
    def __init__(self) -> None:
        self.year = readfile.getDate()[0]
        self.filename = "/Users/xinyixu/Desktop/工资/{}工资单.xlsx".format(self.year)
        self.view_page = App(title="三会员工工资一览", width=1200, height= 1000)
        Text(self.view_page, text='', size=20)
        Text(self.view_page, text='     请根据以下提示操作：', size=35)
        Text(self.view_page, text='', size=30)

    def view_file(self):
        Text(self.view_page, text='在 桌面 上找到并打开 工资 文件夹', size=38)
        Picture(self.view_page, image='/Users/xinyixu/Desktop/工资/wjj.png')
        Text(self.view_page, text='选择 年份 并打开 对应文件', size=38)
        Picture(self.view_page, image='/Users/xinyixu/Desktop/工资/wj.png')
        Text(self.view_page, text='在 左下角 选择并点击 月份 ', size=38)
        Picture(self.view_page, image='/Users/xinyixu/Desktop/工资/w.png')
        self.view_page.select_file(filename=self.filename)
        self.view_page.display()

# view_UI().view_file()
        