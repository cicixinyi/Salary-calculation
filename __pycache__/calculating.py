import opening_UI
import employee_UI
import changeDate_UI
import otherEmployee_UI
import view_UI

start = opening_UI.opening_UI()
choice = start.choice()
print(choice)
if choice == 1:
    employee_UI.employee_UI().edit()
elif choice == 2:
    date = changeDate_UI.changeDate_UI().chooseDate()
    if date == 'today':
        employee_UI.employee_UI().edit()
    else:
        otherEmployee_UI.otherEmployee_UI(date).edit()
elif choice == 3:
    view_UI.view_UI().view_file()
    


