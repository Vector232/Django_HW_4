from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    news = Article.objects.order_by(ordering).all()
    for article in news:
        print(article.title)
        for scope in article.scopes.all():
            print(scope)

    context = {'object_list': news}

    return render(request, template, context)
