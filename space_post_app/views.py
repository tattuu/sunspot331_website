from django.shortcuts import render

def post_list(request):
    return render(request, 'space_post/post_list.html', {})