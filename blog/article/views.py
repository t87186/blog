from django.shortcuts import render

from article.models import Article, Comment
from article.forms import ArticleForm

# Create your views here.

def article(request):
    '''
    Render the article page
    '''
    articles = Article.objects.all()
    itemList = []
    for article in articles:
        items = [article]
        items.extend(list(Comment.objects.filter(article=article)))
        itemList.append(items)
    context = {'itemList':itemList}
    return render(request, 'article/article.html', context)

def articleCreate(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the article page
    '''

    template = 'article/articleCreate.html'
    if request.method == 'GET':
        print(ArticleForm())
        return render(request, template, {'articleForm':ArticleForm()})