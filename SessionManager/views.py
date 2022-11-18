from re import M
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from SessionManager.models import *
import datetime as dt

# Create your views here.

@login_required
def home(request):
    return render(request, "BaseApp/home.html")

@login_required
def book_session_view(request):
    return render()


def create_date_obj(date):
    date = date.split('-')
    return dt.date(int(date[0]), int(date[1]), int(date[2]))
    


def select_date(request):
    today = dt.date.today().strftime("%Y-%m-%d")
    limit = dt.date.today() + dt.timedelta(days=2)
    limit = limit.strftime("%Y-%m-%d")
    return render(request, "BaseApp/select_date.html", context={"today":today, "limit":limit})

def select_slot(request):
    if request.POST["slot_date"]:
        morning_full = []
        morning_avail = []
        evening_full = []
        evening_avail = []
        m = Session.objects.filter(ME="Morning")
        for slot in m:
            if BookSession.objects.filter(slot=slot, slot_date=create_date_obj(request.POST["slot_date"])).count() >= slot.members_count:
                print("true")
                morning_full.append(slot)
            else:
                morning_avail.append(slot)

        e = Session.objects.filter(ME="Evening")

        for slot in e:
            if BookSession.objects.filter(slot=slot, slot_date=create_date_obj(request.POST["slot_date"])).count() >= slot.members_count:
                evening_full.append(slot)
            else:
                evening_avail.append(slot)

        print(morning_full, morning_full)

        return render(request, "BaseApp/select_slot.html", context={"slot_date":request.POST["slot_date"], "morning_full":morning_full, "morning_avail":morning_avail, 'evening_full':evening_full, "evening_avail":evening_avail})

    return redirect("home")

def confirm_slot_view(request, date):
    if request.POST.get('slot'):
        sess = Session.objects.get(id = request.POST["slot"])
        is_duplicate = False
        if BookSession.objects.filter(user=request.user, slot_date=create_date_obj(date)).exists():
            is_duplicate = True
        return render(request, "BaseApp/confirm_slot.html", context={"slot_date":date, "slot":sess.session_time, "me":sess.ME, "is_duplicate":is_duplicate})
    return redirect('home')

def book_slot(request, date):

    if request.POST["slot"] is not None:
        slot = Session.objects.get(session_time = request.POST['slot'], ME=request.POST["me"])
        
        if BookSession.objects.filter(user=request.user, slot_date=create_date_obj(date)).exists():
            return redirect('confirm_slot_view', date)

        sess = BookSession(slot=slot, user=request.user, slot_date=create_date_obj(date))
        sess.save()

        return render(request, "BaseApp/success.html")
    return redirect('home')


def view_booked_slots(request):
    sess = BookSession.objects.filter(user=request.user).order_by("-id")
    return render(request, "BaseApp/list_booked_slots.html", context={"sess" : sess})
