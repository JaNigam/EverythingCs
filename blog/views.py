from django.shortcuts import render, HttpResponse
from blog.models import post

# Create your views here.


def blogHome(request):
    #we are pulling all the object of post by this command line
    allpost = post.objects.all()
    #here we are declaring a dictionary as context.
    #we'll pass this in the render funtion
    #so that we can extract objects from it using the template coding
    context = {'allposts':allpost}
    return render(request, 'blog/blogHome.html', context)


def blogPost(request, slug):
    Post = post.objects.filter(slug = slug).first()
    context = {'post': Post}
    return render(request,'blog/blogPost.html', context)
    # return HttpResponse(f'this is: {blog_name}')
    # here the blog_name is a variable
