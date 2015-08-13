from django.shortcuts import render
from blog.models import Blog,Category,Message
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import MessageForm
from django.contrib.auth.decorators import login_required


class category_num():
	def get_list(self):
		classf =  Category.objects.all();
		classf_list =[]
		for i in range(len(classf)):
			classf_list.append([])
		for i in range(len(classf)):
			temp = Category.objects.get(name=classf[i])
			posts = temp.blog_set.all()
			classf_list[i].append(classf[i])
			classf_list[i].append(len(posts))
		return classf_list


def index(request):
	articles = Blog.objects.order_by('-update_time')
	paginator=Paginator(articles,5)
	page_num = request.GET.get('page')
	art = {}
	c = category_num()
	art['categorys'] = c.get_list() # category : number
	try:
		articles = paginator.page(page_num) #check  number page
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(pageinator.num_pages)
	art['articles'] = articles	
	return render(request,'blog/index.html',art)

def category_page(request,category_name):
	category = Category.objects.get(name = category_name) 
	articles = category.blog_set.all()
	paginator = Paginator(articles,5)
	page_num = request.GET.get('page')
	
	art={}
	c = category_num()
	art['categorys'] = c.get_list()
	try:
		articles = paginator.page(page_num)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(name = category_name)	
	art['articles'] = articles
	return render(request,'blog/category_page.html',art)

def article(request,article_num):
	try:
		num = article_num
	except ValueError:
		num = ''
	art={}
 	c = category_num()
	art['categorys'] = c.get_list()	
	article  = Blog.objects.get(id=num)
	art['article'] = article
	return render(request,'blog/article.html',art )

#@login_required
def message(request):
	mess= {}
	mess['mess'] = Message.objects.all()
	
	if request.method =='POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			newmessage = Message(author=request.user,
					body=form.cleaned_data['body'],
				)
			newmessage.save()
		return render(request,'blog/message.html',mess)	
	else:	
		form = MessageForm()
	mess['form']=form	
	return render(request,'blog/message.html',mess)

def list(request):
	pass

def add_blog(request):
	form = Blog.objects.all()
	return render(request,'blog/add_blog.html',{'forms':form})
