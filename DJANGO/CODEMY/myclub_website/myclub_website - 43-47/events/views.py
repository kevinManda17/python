from django.shortcuts import render , redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime 
from django.http import HttpResponseRedirect, HttpResponse

from .models import Event , Venue , MyClubUser
# import user forms 
from django.contrib.auth.models import User

from .forms import VenueForm  ,EventFormAdmin , EventForm

import csv

from django.http import FileResponse
import io 
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#import pagination stuff
from django.core.paginator import Paginator


#query database with RawSQL
from django.db.models.expressions import RawSQL

#import messages after somethings 
from django.contrib import messages 


def show_event(request, event_id):
    event =Event.objects.get(pk = event_id )
    data ={
        "event":event
    }
    return render(request, "events/show_event.html", data )

def venue_events(request, venue_id):
    # grab the venue 
    venue =Venue.objects.get(id = venue_id)
    events= venue.event_set.all()
    data= {
            "venue":venue,
            "events":events,
    }
    if events :
        return render(request, "events/venue_event.html", data )
    else :
        messages.success(request , ("That Venue Has No Events At This Time !!"))
        return redirect("admin-approval")

def admin_approval (request):
    #Get Venue list 
    venue_list= Venue.objects.all()
    # Get counts 
    event_count = Event.objects.all().count()
    venue_count =Venue.objects.all().count()
    user_count =User.objects.all().count()
    event_list = Event.objects.all().order_by("-event_date")
    data ={
        "event_list":event_list,
        "event_count":event_count,
        "venue_count":venue_count,
        "user_count":user_count,
        "venue_list":venue_list,
    }
    if request.user.is_superuser:
        if request.method == "POST":
            messages.success(request, ("Event List Approved Has Been Updated !"))
            return redirect('list-events')
        else :
            return render(request, 'events/admin_approval.html', data )
    else :
        messages.success(request , ("You Are Not Authorized To View This Page !"))
    return redirect('admin-approval')


def my_events(request):
    if request.user.is_authenticated :
        user_id = request.user.id
        events = Event.objects.filter(attendees = user_id)
    else :
        messages.success(request , ("You Aren't Authorized To View This Page"))
        return redirect("home") 

    data = {
            "events":events,
    }
    return render(request , "events/my_events.html" , data )




def to_Query_database_with_rawsql(request):
  
    raw_events_list = Event.objects.raw("""
                select distinct name from Event 
    """)
    data ={
         

    }
    return render(request , "events/events_list1.html", data )



def venue_pdf(request):
    #create bytestream buffer 
    buf = io.BytesIO()
    #create canvas 
    c = canvas.Canvas(buf , pagesize = letter , bottomup=0)
    #create a text object
    text_obj =c.beginText()
    text_obj.setTextOrigin( inch , inch )
    text_obj.setFont("Helvetica", 14)

    #add some of text   
    venues =Venue.objects.all()
    lines =[

    ]

    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email_address)
        lines.append("__________________________________")

    for line in lines :
        text_obj.textLine(line)

    #finish Up 
    c.drawText(text_obj)
    c.showPage()
    c.save()
    buf.seek(0)

    # return  something
    return FileResponse(buf , as_attachment=True , filename ="venue.pdf")


def venue_csv(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attanchements; filename=venues.csv'
    #create a csv writter
    writer= csv.writer(response)
    #designate The Model 
    venues = Venue.objects.all()
    #add column heading to the csv file 
    writer.writerow([
        'venue name',
        'Address',
        'Zip Code',
        'Phone',
        'Web Address',
        'Email Address',
    ])

    #create blanck lines 
    lines =[]
    #loop Thu an output 
    for venue in venues:
        writer.writerow([  
                        # venue,
                        venue.name , 
                        venue.address, 
                        venue.zip_code,  
                        venue.phone,
                        venue.web ,
                        venue.email_address
    ])


    # response.writelines(lines)
    return response


def venue_text(request):
    response = HttpResponse(content_type="text/plain")
    response['Content-Disposition'] = 'attanchements; filename=venues.txt'
    #designate The Model 
    venues = Venue.objects.all()
    #create blanck lines 
    lines =[

    ]
    #loop Thu an output 
    for venue in venues:
        lines.append(f"""
                        {venue}  \n
                        {venue.name}  \n
                        {venue.address}  \n
                        {venue.zip_code}  \n
                        {venue.phone}  \n
                        {venue.web}  \n
                        {venue.email_address}  \n\n\n
    """)

    # lines= [
    #     "This is line 1\n"
    #     "This is line 2\n"
    #     "This is line 3\n"
    # ]
    response.writelines(lines)
    return response



#generate Text File Venue List 
def venue_text(request):
    response = HttpResponse(content_type="text/plain")
    response['Content-Disposition'] = 'attanchements; filename=venues.txt'
    #designate The Model 
    venues = Venue.objects.all()
    #create blanck lines 
    lines =[]
    #loop Thu an output 
    for venue in venues:
        lines.append(f"{venue}\n")

    # lines= [
    #     "This is line 1\n"
    #     "This is line 2\n"
    #     "This is line 3\n"
    # ]
    response.writelines(lines)
    return response


def delete_venue(request , venue_id):
    venue = Venue.objects.get( pk = venue_id )
    # event = User.objects.get(pk = Event.manager)
    # if request.user.is_superuser and request.user.id == Event.manager:
    if request.user == Event.manager:
        venue.delete()
        messages.success(request, ("Venue Was Deleted SuccessFully !!!"))
    else :
        messages.success(request, ("You Aren't Authorized To Delete This Venue  !!!"))
    return redirect('list-venues')


def delete_event (request , event_id ):

    event= Event.objects.get( pk = event_id )
    
    if request.user == event.manager :
        event.delete()
        messages.success(request , ("Event Deleted !!!"))
        return redirect("list-events")
    
    elif  request.user == event.manager:

        if event.manager ==  None :
            messages.success(request , "Not Manager For This Event !")
            return redirect("list-events")
    else :
        messages.success(request , ("You Aren't Authorized To Delete This Event !"))


def update_event(request , event_id):
    event= Event.objects.get( pk = event_id)
    form = EventForm(request.POST or None , instance= event)
    if form.is_valid():
        form.save()
        return redirect("list-events")

    data = {
            "event":event,
            "form":form,
    }
    
    return render(request , "events/update_event.html" , data )    

def add_event (request):
    submitted = False 
    if request.method == "POST":
       if request.user.is_superuser :
            form = EventFormAdmin(request.POST)
       else :
            form = EventForm(request.POST)
       if form.is_valid():
           form.save()
           return  HttpResponseRedirect("/add_event?submitted=True")
       
    else : 
        if request.user.is_superuser:
            form = EventFormAdmin
        else :
            form = EventForm
        if "submitted" in request.GET :
            submitted= True 
    form = EventForm
    data = {"form":form,
            "submitted":submitted ,

            }
    return render(request , "events/add_event.html", data )

def update_venue(request , venue_id):
    venue= Venue.objects.get( pk = venue_id )
    form = VenueForm(request.POST or None , request.FILES  or None , instance= venue  )
    if form.is_valid():
        form.save()
        return redirect("list-venues")

    data = {
            "venue":venue,
            "form":form,
    }
    return render(request , "events/update_venue.html" , data )    


def search_venues(request):

    if request.method == "POST":
        searched =request.POST['searched']
        venues = Venue.objects.filter(
            name__contains= searched,
            # web__contains=searched,      
    )
        data  = {
                "searched":searched,
                 "venues":venues ,
    
    } 
    return render(request , "events/search_venues.html", data)


def search_events(request):
    searched =""
    events =Event
    if request.method == "POST":
        searched =request.POST['searched']
        events = Event.objects.filter(
            name__contains= searched ,
            # description__contains = searched,
              
     )
    data  = {
                "searched":searched,
                 "events":events,
    
    } 
    return render(request , "events/search_events.html", data)

def user_after_submitted(request, venue_id):
    venue = Venue.objects.get( pk = venue_id )
    venue_owner = User.objects.get( pk = venue.owner)
    data = {
        "venue_owner":venue_owner,
    }
    return render(request , "events/show_venue.html", data  )

def show_venue(request , venue_id):
    venue = Venue.objects.get( pk = venue_id )
    venue_owner = User.objects.get( pk = venue.owner)

    data = {'venue':venue,
            "venue_owner":venue_owner,
            }
    return render(request , "events/show_venue.html", data)


def list_venues(request):
    # venue_list =Venue.objects.all().order_by("?")
    venue_list =Venue.objects.all()

    #set up pagination
    p = Paginator(Venue.objects.all(), 15)
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums= "a" * venues.paginator.num_pages

    data = {
            "venue_list":venue_list,
            'venues':venues,
            "nums":nums,
            }
    return render(request , "events/venue.html", data )



def add_venue(request):

    submitted = False 

    if request.method == "POST":
       
       form = VenueForm(request.POST , request.FILES )

       if form.is_valid():
           
           venue= form.save(commit=False)
           venue.owner = request.user.id #Logged in user 
           venue.save()
        #    form.save()
           return  HttpResponseRedirect("/add_venue?submitted=True")
       
    else : 

        form = VenueForm

        if "submitted" in request.GET :
            submitted= True 

    form = VenueForm
    data = {
            "form":form,
            "submitted":submitted ,

            }
    return render(request , "events/add_venue.html", data )




def all_events(request):
     events_list =Event.objects.all().order_by("-event_date")
     data = {
            "events_list":events_list,
         }
     
     return render(request , "events/event_list.html", data )



def home(request):
    data = {   
            "":""
            }
    return render(request, "events/home.html", data )



def calendar_home(request , year=datetime.now().year  , month=datetime.now().strftime("%B") ):
    name = "Kevin"
    month = month.title() 
     # convert month from name to numbers
    
    month_number= list(calendar.month_name).index(month)
    month_number = int ( month_number)

    # create calendar 
    cal = HTMLCalendar().formatmonth(
        year ,
        month_number
        )
    #get current year 
    now  = datetime.now()
    current_year = now.year
    #get time 
    time = now.strftime('%I:%M %p')

    #query the event model for dates 

    event_list =Event.objects.filter(
        event_date__year = year ,
        event_date__month= month_number , 
    )
    data = {
            "name": name,
            "year":year,
            "month":month,
            "month_number":month_number,
            "cal":cal,
            "current_year":current_year,
            "time": time ,
            "event_list":event_list,
        }
   

    return render(request, "events/home.html" , data)


# @KEVIN MANDA 

def show_my_name(request):
    data = {"data_name":"Kevin Manda"}

    return render(request , "events/home.html" , data )


