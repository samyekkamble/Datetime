from django.shortcuts import render
import  datetime

time_obj = datetime.datetime.now()
time_now = time_obj.strftime("%X")
hours_now = time_obj.hour
todays_date = time_obj.date()


def view1(request):
    name = input("Enter Your Name :\n")
    template_name = 'Timeview/view1.html'
    context = {"Date": todays_date, "Hours": hours_now, "Time": time_now, "Name": name}
    return render(request, template_name, context)
