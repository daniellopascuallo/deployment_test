from django.shortcuts import render, redirect

from .models import Show

#add messages framework: shows the error messages for one refresh
from django.contrib import messages


def index(request):
    # print(request.method)
    # print(request.GET)
    # print("*********")
    return redirect("/shows")

def shows(request):
    # print(request.method)
    # print(request.GET)
    # print("*********")
    context = {
        "allShows" : Show.objects.all()
    }
    return render(request, "shows.html", context)    

def add_new_show(request):
    # print(request.method)
    # print(request.GET)
    # print("*********")
    return render(request, "add_new_show.html")

###############################################
# method to validate:
def create_show(request):    
    # print(request.method)
    # print(request.POST)
    # print("**************")
    # connecting request.POST (form info) to the validator
    errorsObject = Show.objects.showValidator(request.POST)

    # printed errors in models.py (ShowManager) and we now we are getting the errors dictionary and its len

    # creating if statements to control those errors based on the len of that errors dictionary. If it is > 0 we have validation error messages 

    if len(errorsObject) > 0:
        # check if the errors dictionary has anything in it
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errorsObject.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/shows/new")

    # Store the new object in a variable (new_show) so it can be referenced on the redirection with its id
    new_show = Show.objects.create(title=request.POST["form_title"], network=request.POST["form_network"], release_date=request.POST["form_release_date"], description=request.POST["form_description"])
    return redirect(f"/shows/{new_show.id}")  # redirects to show's page: needed f"" string for the variable.
###################################################

def show_info(request, showID):
    # print(request.method)
    # print(request.GET)
    # print("*********")
    showInfo = Show.objects.get(id= showID)
    # print(showInfo)
    context = {
        "showInfo" : showInfo
    }
    return render(request, "show_info.html", context)

def delete_show(request, showID):
    # print(request.method)
    # print(request.GET)
    # print("**************")
    # print(showID)
    show_to_delete = Show.objects.get(id= showID)
    show_to_delete.delete()
    return redirect("/shows")

def edit_show(request, showID):
    # print(request.method)
    # print(request.GET)
    # print("**************")
    # print(showID)
    # we need to send info to the edit show template, specific show info:
    showInfo = Show.objects.get(id= showID)
    # print(showInfo)
    context = {
        "showInfo" : showInfo
    }
    return render(request, "edit_show.html", context)

######################################################
# method to validate
def update_show(request, showID):
    print(request.method)
    print(request.POST)
    print("**************")
    errorsObject = Show.objects.showValidator(request.POST)

    if len(errorsObject) > 0:
        for key, value in errorsObject.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f"/shows/{showID}/edit")

    # print(showID)
    edited_show = Show.objects.get(id= showID)
    # print(edited_show)
    edited_show.title = request.POST["form_title"]
    edited_show.network = request.POST["form_network"]
    edited_show.release_date = request.POST["form_release_date"]
    edited_show.description = request.POST["form_description"]
    edited_show.save()
    return redirect(f"/shows/{edited_show.id}")
##########################################################