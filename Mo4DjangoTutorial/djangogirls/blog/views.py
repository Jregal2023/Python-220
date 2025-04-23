from django.shortcuts import render , get_object_or_404
from django.utils import timezone
from .models import Post
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
    
    return render(request,'blog/post_list.html', {'Posts' : posts})

def post_detail(request, pk):
    #get object 404 only works when grabbing a single item
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})
'''
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_Detail', pk = post.pk)
    else:
        
        form = PostForm()
        return render (request, 'blog/post_edit.html', {'form': form})
        '''