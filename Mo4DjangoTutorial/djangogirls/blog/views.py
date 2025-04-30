from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm , CommentForm
from django.shortcuts import redirect
#Basically this says hey you need to have a login and allows me to define functions that require a login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
#from django.urls import LazyView

# Create your views here.
#views is used to handle requests and provide a respons
#we take the request info and handle it in someway
#then we fetch the info (if needed) from the database to then send ot a HTML page
#finally, we create a  response to send back to the client

#everything in our views file takes in a request as an argument
def post_list(request):
    #return a response..the response will return the request back to the user
    #tell you the template or html page to go to and any data that needs to be passed to that html page
    #POST in HTTP means to add something to a database
    #GET us to grab
    #PUT - updated Existing
    #DELETE -Delete something from DB
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    #get object 404 only works when grabbing a single item
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        
        form = PostForm()
    return render (request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    #grab post to edit
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        #instace=post makes sure we are changing an existing post and not making a new one
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        #pre-fill out text boxes with all the info from our database entry for this particular post
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')

    return render(request, 'blog/post_draft_list.html', {'posts' : posts})
    
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.publish()
    return redirect('post_detail', pk=pk)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def post_remove(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method =='POST':
        post.delete()
    return redirect('post_list')

def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})    

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)