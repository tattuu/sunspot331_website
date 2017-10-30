from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Article, Comment, PopularPost, Category
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


def category(request, pk):
    pk_category = get_object_or_404(Category, pk=pk)
    popular_post_list = PopularPost.objects.all()
    categorys = Category.objects.all()
    posts = Article.objects.filter(category__name__contains=pk_category).filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'space_post/post_category.html',
                  {'posts': posts, 'popular_post_list': popular_post_list, 'categorys': categorys, 'pk_category': pk_category})


def post_list(request):
    posts = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    popular_post_list = PopularPost.objects.all()
    categorys = Category.objects.all()
    return render(request, 'space_post/post_list.html',
                  {'posts': posts, 'popular_post_list': popular_post_list, 'categorys': categorys})


def post_detail(request, pk):
    post = get_object_or_404(Article, pk=pk)
    popular_post_list = PopularPost.objects.all()
    categorys = Category.objects.all()
    return render(request, 'space_post/post_detail.html',
                  {'post': post, 'popular_post_list': popular_post_list, 'categorys': categorys})


def add_comment_to_post(request, pk):
    popular_post_list = PopularPost.objects.all()
    categorys = Category.objects.all()
    post = get_object_or_404(Article, pk=pk)
    form = CommentForm()  # Add commentを押した時はadd_comment_to_postがまだ開かれておらず、methodがPOSTと定まっていないので、下のif文は偽となる。その時用の初期値
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm()
        return render(request, 'space_post/add_comment_to_post.html',
                      {'form': form, 'popular_post_list': popular_post_list, 'categorys': categorys})
    return render(request, 'space_post/add_comment_to_post.html',
                  {'form': form, 'popular_post_list': popular_post_list, 'categorys': categorys})


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
