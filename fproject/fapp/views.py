from django.shortcuts import render, redirect
from .models import Gallery

def index(request):
    if request.method == 'POST' and 'image' in request.FILES:  # Ensure the 'image' key is in request.FILES
        myimage = request.FILES['image']  # Access the uploaded image from request.FILES
        obj = Gallery(feedimage=myimage)  # Create an instance of Gallery and save the image
        obj.save()  # Save the object to the database
        return redirect('index')  # Redirect back to the index page after saving

    # Retrieve all gallery images to display
    gallery_images = Gallery.objects.all()
    return render(request, "index.html", {"gallery_images": gallery_images})  # Pass the images as context to the template
