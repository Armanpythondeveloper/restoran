from django import forms


from .models import Book_Table,ContactForm

class FormBookTable(forms.ModelForm):

    class Meta:

        model = Book_Table
        fields = ['name','email','date','people_count','message']



class FormContact(forms.ModelForm):

    class Meta:

        model = ContactForm
        fields = ['name','email','subject','message']