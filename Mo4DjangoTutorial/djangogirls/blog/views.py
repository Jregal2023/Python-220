from django.shortcuts import render

# Create your views here.
#views is used to handle requests and provide a respons
#we take the request info and handle it in someway
#then we fetch the info (if needed) from the database to then send ot a HTML page
#finally, we create a  response to send back to the client

#everything in our views file takes in a request as an argument
def post_list(request):
    #return a response..the response will return the request back to the user
    #tell you the template or html page to go to and any data that needs to be passed to that html page
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    
    return render(request,'blog/post_list.html', {'Posts' : posts})