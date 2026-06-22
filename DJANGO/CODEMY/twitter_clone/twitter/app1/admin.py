from django.contrib import admin
from django.contrib.auth.models import Group , User 
from .models import Profile  , Meep 
 

# unregister group 
admin.site.unregister(Group)

# admin.site.register(Profile)

# mix Profile info into usern info 

class ProfileInline(admin.StackedInline):
    model = Profile 


# extends User Model 

class UserAdmin(admin.ModelAdmin):
    model = User 
    # just display username fields on admin page 
    fields = ['username']
    inlines = [ProfileInline]

# unregister initial user 
admin.site.unregister(User)
admin.site.register(User , UserAdmin)


admin.site.register(Meep)