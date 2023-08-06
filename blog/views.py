from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .models import Blog
from .forms import BlogForm

# Create your views here.

def bloglist(request):
    blogs = Blog.objects.all()
    return render(request,'blog/list.html',{'blogs':blogs})

def blog_detail(request, id):
    blog = get_object_or_404(Blog,id=id)
    return render(request,'blog/detail.html',{'blog':blog})

def create_blog(request):
    form = BlogForm(request.POST or None)
    if request.POST :
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            print('form is valid')
            form = BlogForm(request.POST,request.FILES)
            post = form.save(commit=False)
            post.attachement = request.FILES["attachement"]
            post.save()
            return HttpResponseRedirect("/admin/blog")
        
        print('form is invalid')
    return render(request,'blog/createpost.html',{'form':form})

def update_blog(request,id):
    blog = get_object_or_404(Blog,id=id)
    form = BlogForm(data=request.POST or None,instance=blog)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/admin/blog")
    return render(request,'blog/editpost.html',{'form':form})