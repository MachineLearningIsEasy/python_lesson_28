from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Tag
from .forms import ArticleForm
from datetime import datetime
from django.core.files.images import ImageFile
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views (представление) here.

def main_page(request):
#    art_all = Article.objects.all()
#    art_all = Article.objects.filter(is_active = True)
    art_all = Article.active_objects.all()
#    art_all = Article.active_objects.select_related('article_tag').all()
#    art_all = Article.active_objects.prefetch_related('article_tag').all()

    art_one = art_all[0]

    tags = art_one.get_all_tags
    for tag in tags:
        print(tags)


    paginator = Paginator(art_all, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    some_info = 'some text information'
    return render(request, 'articles/category.html', {'articles':articles,'article_': art_one, 'info':some_info})


@login_required
def article_description(request, id):
    #art_one = Article.objects.first()
    #return HttpResponse(f'Text: {art_one.article_text}')
    art_one = get_object_or_404(Article,id = id)
    return render(request, 'articles/single.html', {'article':art_one})

@user_passes_test(lambda user: user.is_superuser)
def article_add(request):
    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'articles/article_add.html', {'form':form})
    else:
        #form = ArticleForm(request.POST)
        form = ArticleForm(request.POST, files = request.FILES)
        if form.is_valid():
            # обработка данных

            '''
            # Первый способ создания формы
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            tags = form.cleaned_data['tags']
            print(f'{name}, {text}, {tags}')
            article_object = Article(article_name = name, article_text = text, article_date = datetime.now(),article_img = ImageFile(open("media/articles/happy_lion.jpg", "rb")))
            article_object.save()
            '''
            # Второй способ создания формы
            form.save()

            return HttpResponseRedirect(reverse('articles:index'))
        else:
            return render(request, 'articles/article_add.html', {'form':form})


class TagListView(ListView):
    model = Tag
    template_name = 'articles/tag_list.html'
    context_object_name = 'tags'
    paginate_by = 2

    def get_queryset(self):
    # можно наложить условия на объекты
        #return Tag.objects.filter(is_active = True)
        return Tag.active_objects.all()



class TagDetailView(LoginRequiredMixin, DetailView):
    model = Tag
    template_name = 'articles/tag_one.html'


class PermissionMixin:

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('articles:index'))


class TagUpdateView(PermissionMixin, UserPassesTestMixin, UpdateView):
    template_name = 'articles/tag_update.html'
    model = Tag
    success_url = reverse_lazy('articles:tag_list')

class TagDeleteView(PermissionMixin, UserPassesTestMixin, DeleteView):
    template_name = 'articles/tag_delete.html'
    model = Tag
    success_url = reverse_lazy('articles:tag_list')


class TagCreateView(CreateView):
#class TagCreateView(PermissionMixin, UserPassesTestMixin, CreateView):
    fields = '__all__'
    template_name = 'articles/tag_create.html'
    model = Tag
    success_url = reverse_lazy('articles:tag_list')
