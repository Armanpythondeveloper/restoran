from django.db import models

# Create your models here.
class IndexInfo(models.Model):

    text1 = models.TextField('text info1')
    text2 = models.TextField('text info2')
    btn_name = models.CharField('btn name',max_length=30) 
    img = models.ImageField('image',upload_to='images') 

    def __str__(self) -> str:
        return self.text1
    
    


class IndexSecondInfo(models.Model):

    name = models.CharField('name',max_length=30)
    name_text = models.TextField('text name')

    def __str__(self) -> str:
        return self.name
    

class IncludeIndex(models.Model):

    img_1 = models.ImageField('image1',upload_to='images')
    img_2 = models.ImageField('image2',upload_to='images')
    img_3 = models.ImageField('image3',upload_to='images')
    img_4 = models.ImageField('image4',upload_to='images')

    name = models.CharField('name include',max_length=30)
    text_1 = models.TextField('text 1')
    text_2 = models.TextField('text 2')
    text_3 = models.TextField('text 3')
    text_4 = models.TextField('text 4')
    text_5 = models.TextField('text 5')
    text_6 = models.TextField('text 6')
    text_7 = models.TextField('text 7')
    text_8 = models.TextField('text 8')
    text_9 = models.TextField('text 9')
    text_10 = models.TextField('text 10')
    text_11 = models.TextField('text 11')


class MenuInclude(models.Model):

    men_1 = models.TextField('men 1')
    men_2 = models.TextField('men 2')
    men_3 = models.TextField('men 3')
    men_4 = models.TextField('men 4')
    men_5 = models.TextField('men 5')
    men_6 = models.TextField('men 6')
    men_7 = models.TextField('men 7')
    men_8 = models.TextField('men 8')

    def __str__(self) -> str:
        return self.men_1


class MenuContent(models.Model):

    prod_name = models.CharField('prod name',max_length=30)
    prod_price = models.PositiveIntegerField('product price')
    prod_img = models.ImageField('product image',upload_to='images')
    prod_info = models.TextField('product info')

    def __str__(self) -> str:
        return self.prod_name
    

class Xohararner(models.Model):

    xoh_1 = models.CharField('anuny',max_length=30)
    xoh_2 = models.CharField('ira masin',max_length=30)
    xoh_img = models.ImageField('nkary',upload_to='images')


    def __str__(self) -> str:
        return self.xoh_1
    

class XohararVernagir(models.Model):

    vern_1 = models.TextField('vernagir 1')
    vern_2 = models.TextField('vernagir 2')

    def __str__(self) -> str:
        return self.vern_1
    

class Clients(models.Model):

    client_name = models.CharField('name',max_length=30)
    client_img = models.ImageField('client image',upload_to='images')
    client_proff = models.CharField('professional',max_length=30)
    client_info = models.TextField('info about client')

    def __str__(self) -> str:
        return self.client_name
    

class Client_B(models.Model):

    upp_1 = models.CharField('nanana',max_length=30)
    upp_2 = models.CharField('dndndnd',max_length=30)

    def __str__(self) -> str:
        return self.upp_1
    


class Book_Table(models.Model):

    name = models.CharField('name',max_length=30)
    email = models.EmailField('user email')
    date = models.TextField('date')
    people_count = models.TextField('people count')
    message = models.TextField('message')

    def __str__(self) -> str:
        return self.name


class Team(models.Model):

    team_img = models.ImageField('image',upload_to='images')
    team_name = models.CharField('team name',max_length=30)
    team_info = models.CharField('information about chief',max_length=30)


    def __str__(self) -> str:
        return self.team_name
    

class ContactForm(models.Model):

    name = models.CharField('user name',max_length=30)
    email = models.EmailField('user email')
    subject = models.CharField('subject name',max_length=30)
    message = models.TextField('text')

    def __str__(self) -> str:
        return self.name
    


    
    