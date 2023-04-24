from django.shortcuts import render, get_object_or_404
import os
from django.http import FileResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from django.shortcuts import render
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs_list = Blog.objects.all()
    popular_blogs = Blog.objects.filter(is_popular=True)[:3]
    paginator = Paginator(blogs_list, 2)
    page_number = request.GET.get("page")
    try:
        blogs = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)
    return render(request, "blog/all_blogs.html", {"blogs": blogs, "popular_blogs": popular_blogs})


def show_pdf(request):
    filepath = os.path.join('static', 'Python-week1.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/detail.html", {"blog": blog, "request": request})
