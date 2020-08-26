from django.db import models


class ShowManager(models.Manager):
    def showValidator(self, postData):
        errors = {}
        if len(postData["form_title"]) < 2:
            errors["titleRequired"] = "Title must be 2 characters min"
        if len(postData["form_network"]) < 3:
            errors["networkRequired"] = "Network must be 3 characters min"
        if len(postData["form_description"]) < 10:
            errors["descriptionRequired"] = "Description must be 10 characters min"
        
        print("printing errors dict to check the len of errors object")
        print(errors)
        return errors
        

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = ShowManager()

    def __repr__(self):
        return f"<Tv Show object {self.title} ({self.id})>"
