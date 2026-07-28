from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render


from .models import Blog

# Create your views here.

def blog(request):
    quick_search = request.GET.get("q", "").strip()

    
    blogs = Blog.objects.all().order_by("-date")

    if quick_search:
        blogs = blogs.filter(title__icontains=quick_search)

    



    return render(request, "blogs/blogs.html", {"blogs": blogs})
