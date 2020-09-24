from django.shortcuts import render,redirect
from .models import Post,Info
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.conf import settings 
from django.core.mail import send_mail
# Home Page
def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)   
    return render(request,'blog/home.html',{'posts':posts})

# detail post
def detail_post(request,id):
    posts = Post.objects.get(id=id)   
    return render(request,'blog/detail_post.html',{'posts':posts})     

# Contact Page
def contact(request):
    info = Info.objects.first()
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
            
        send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
         )
    return render(request,'blog/contact.html',{'info':info})

# Dashboard Page
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        paginator = Paginator(posts,3)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)   
        return render(request,'blog/dashboard.html',{'posts':posts})
    else:
        return redirect('login')  

# Add New Post
@login_required(login_url='login')          
def add_post(request):
    form = PostForm()    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.created_by = request.user
            form1.save()
        else:
             form = PostForm()
    return render(request,'blog/add_post.html',{'form':form})

# Update Post
@login_required(login_url='login')          
def update_post(request,id):
        post = Post.objects.get(id=id)
        form = PostForm(instance=post)
        if request.method == 'POST':
                 form = PostForm(request.POST,instance=post)
                 if form.is_valid():
                     form.save()
                 else:       
                     post = Post.objects.get(id=id)
                     form = PostForm(instance=post)
        return render(request,'blog/update_post.html',{'form':form})             

# Delete Post
@login_required(login_url='login') 
def delete_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('Mini-Blog:home')

