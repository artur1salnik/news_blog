from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q


def new(request):
    search_query = request.GET.get('search', '')
    if search_query:
        articles_list = Article.objects.filter(Q(article_title__icontains=search_query) | Q(article_text__icontains=search_query))
    else:
        articles_list = Article.objects.order_by('-pub_date')

    paginator = Paginator(articles_list, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }
    return render(request, 'news/newsPage.html', context=context)


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")
    comments_list = a.comment_set.order_by('-id')
    sum_com = Comment.objects.filter(article_id=a).count()
    return render(request, 'news/detail.html', {'article': a, 'comments_list': comments_list, 'sum_com':sum_com})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('news:detail', args=(a.id,)))

