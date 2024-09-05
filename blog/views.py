from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Post
def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Fetch all posts, ordered by creation date (newest first)
    return render(request, 'home.html', {'posts': posts})




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to a thank you page or success message
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})

def thank_you_view(request):
    return render(request, 'blog/thank_you.html')

