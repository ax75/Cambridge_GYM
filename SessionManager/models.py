from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import datetime as dt

# Create your models here.

class Session(models.Model):

    ME_choice = (
        ("Morning", 'morning'),
        ("Evening", 'evening'),

    )

    session_time = models.CharField(max_length=15)
    members_count = models.IntegerField(default=12)
    ME = models.CharField(max_length=255, choices=ME_choice, blank=True)

    def __str__(self):
        return self.session_time

class BookSession(models.Model):
    slot = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT,blank=True, null=True, editable=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    slot_date = models.DateField(blank=True)
    is_duplicate = False

    def clean(self, is_duplicate=0):
        print("Inside Clean : ", self.is_duplicate)
        slot_counter = BookSession.objects.filter(slot=self.slot, slot_date=self.slot_date).count()
        if slot_counter >= self.slot.members_count:
            raise ValidationError("Slots are full for the session.")
        elif self.slot_date < dt.date.today():
            raise ValidationError("Select Future Date.")
        
        super(BookSession, self).clean()
            
        
    '''
    def __str__(self):
        return "hello"
    '''

    def save(self, is_duplicate=0):
        if is_duplicate == 0:
            self.full_clean()
            super(BookSession, self).save()
        

#@receiver(pre_save, sender=BookSession)
def set_user(sender, instance, raw, using, **kwargs):
        
        
        if BookSession.objects.filter(slot_date=instance.slot_date, user=instance.user, slot=instance.slot).exists():
            #raise ValidationError("Eror")
            print("Pre_Save : ", instance.is_duplicate)
            instance.is_duplicate = True
            print("Pre_Save1 : ", instance.is_duplicate)
        # update_fileds["is_duplicate"] = True
        input("Interrupt:::")
        
        
    

