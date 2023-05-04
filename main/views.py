from django.shortcuts import render,redirect

# Create your views here.

from .models import IndexInfo,IndexSecondInfo,IncludeIndex,MenuInclude,MenuContent,Xohararner,XohararVernagir,Clients,Client_B,Book_Table
from .models import Team,ContactForm
from .forms import FormBookTable,FormContact
def index(request):

    index_list = IndexInfo.objects.all()
    index_second_list = IndexSecondInfo.objects.all()
    include_list = IncludeIndex.objects.all()[0]
    menu_include = MenuInclude.objects.all()[0]
    menu_list = MenuContent.objects.all()
    xoharar_list = Xohararner.objects.all()
    vernagir_list = XohararVernagir.objects.all()[0]
    client_list = Clients.objects.all()
    chgitem_list = Client_B.objects.all()[0]


    if request.method == 'POST':
        form = FormBookTable(request.POST)

        if form.is_valid():
            Book_Table.objects.create(**form.cleaned_data)
            form.save()
            return redirect('index')
    else:
        form = FormBookTable()
    return render(request,'main/index.html',context={

        'act':'index',
        'index_list': index_list,
        'index_second_list':index_second_list,
        'include_list': include_list,
        'menu_include':menu_include,
        'menu_list':menu_list,
        'xoharar_list': xoharar_list,
        'vernagir_list':vernagir_list,
        'client_list':client_list,
        'chgitem_list':chgitem_list,
        'form':form
        
    })

def about(request):
    include_list = IncludeIndex.objects.all()[0]
    xoharar_list = Xohararner.objects.all()
    vernagir_list = XohararVernagir.objects.all()[0]

    return render(request,'main/about.html',context={
        'act':'about',
        'include_list': include_list,
        'xoharar_list': xoharar_list,
        'vernagir_list':vernagir_list

    })

def contact(request):

    if request.method == 'POST':
        form = FormContact(request.POST)
        if form.is_valid():
            ContactForm.objects.create(**form.cleaned_data)
            form.save()
            return redirect('contact')
    else:
        form = FormContact()
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')


    return render(request,'main/contact.html',context={
         'act':'contact',
         'form':form
    })

def booking(request):

    return render(request,'main/booking.html',context ={
         'act':'booking'
    })

def menu(request):
    menu_include = MenuInclude.objects.all()[0]
    menu_list = MenuContent.objects.all()

    return render(request,'main/menu.html',context={
        'act':'menu',
        'menu_include':menu_include,
        'menu_list':menu_list

    })

def service(request):

    return render(request,'main/service.html',context={
         'act':'service'
    })

def team(request):

    team_list = Team.objects.all()


    return render(request,'main/team.html',context={
         'team_list': team_list
    })

def testimonial(request):
    client_list = Clients.objects.all()
    chgitem_list = Client_B.objects.all()[0]

    return render(request,'main/testimonial.html',context={
        'client_list':client_list,
        'chgitem_list':chgitem_list

    })


def book_a_table(request):

    return render(request,'main/book_a_table.html',context={
        'act':'book_a_table'
    })