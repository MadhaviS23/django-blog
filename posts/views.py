from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q
from urllib.parse import quote_plus
from django.core.paginator import Paginator ,EmptyPage ,PageNotAnInteger
from .models import post , Category, Author



# Create your views here.

#category_detail

def category(request,id):
    category = get_object_or_404(Category,id=id)
    catdetail = post.objects.filter(categories__title = category.title)
    latest = post.objects.order_by('-timestamp')[0:4]
    popular = post.objects.order_by('comment_count')[0:4]
    cat_count = get_category_count()

    context = {
        'category' : category,
        'catdetail' : catdetail,
        'latest' : latest,
        'popular' : popular,
        'cat_count' : cat_count
    }
    return render (request, 'category_detail.html', context)



#categoroy_count
def get_category_count():
    queryset= post.objects.values('categories__id', 'categories__title').annotate(Count('categories'))
    return queryset

    

#blog-list
def blog(request):
    cat_count = get_category_count()
    print(cat_count)
    latest = post.objects.order_by('-timestamp')[0:4]

    post_list = post.objects.get_queryset().order_by('id')
    popular = post.objects.order_by('comment_count')[0:4]
    paginator = Paginator(post_list, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    
    context = {
        'queryset' : paginated_queryset,
        'latest' : latest,
        'popular' : popular,
        'page_request_var' : page_request_var,
        'cat_count': cat_count

    }

    return render (request, 'blog.html', context)



#post-detail
def single(request,id):
    single = get_object_or_404(post, id=id)
    latest = post.objects.order_by('-timestamp')[0:4]
    popular = post.objects.order_by('comment_count')[0:4]
    cat_count = get_category_count()
    share_string = quote_plus(single.overview)

    
    
    context = {
        'post':single,
        'latest' : latest,
        'popular' : popular,
        'cat_count': cat_count,
        'share_string': share_string,
    }
    return render (request, 'single.html', context)



#search->search_result.html
def search(request):
    queryset = post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)

        ).distinct()
    context = {
        'queryset': queryset

    }

    return render(request,'search_result.html', context)



#homepage
def index(request):

    featured = post.objects.filter(featured=True)
    latest = post.objects.order_by('-timestamp')[0:4]
    random1 = post.objects.all()[0:2]
    random2 = post.objects.all()[3:6]
    random3 = post.objects.all()[2:4]
    category1 = post.objects.all()[0:3]
    category2 = post.objects.all()[3:6]
    popular = post.objects.order_by('comment_count')[0:4]
    section1_1 = post.objects.filter(id=1)
    section1_2 = post.objects.filter(id=3)
    section1_3 = post.objects.filter(id=4)
    cat_count = get_category_count()
    

    
    context = {
        'object_list' : featured,
        'latest' : latest,
        'random1' : random1,
        'random2' : random2,
        'random3' : random3,
        'category1': category1,
        'category2' : category2,
        'popular' : popular,
        'section1_1' : section1_1,
        'section1_2' : section1_2,
        'section1_3' : section1_3,
        'cat_count' : cat_count
        
    }
    
    return render (request, 'index.html', context)



