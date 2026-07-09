from django.shortcuts import render , get_object_or_404
from blog_app.models import BlogModel 

def content_type(request):
    return render(request, 'index.html')

def category_page(request):
    cat_id = request.GET.get('cat', '')
    context = {'cat_id': cat_id}
    return render(request, 'Category.html', context)

def blog_page(request):

  blog_data=BlogModel.objects.all()

  context={
    'blog_data':blog_data
  }

  return render(request,'blog.html',context=context)

def article_page(request):
    # ফ্রন্টএন্ড বা ইউআরএল থেকে আসা সেক্টরের আইডিগুলো রিসিভ করা
    cat_id = request.GET.get('cat', '')
    disorder_id = request.GET.get('disorder', '')
    content_type_id = request.GET.get('type', '')
    
    # ডাটাবেজ থেকে ফিল্টার করে নির্দিষ্ট সেক্টরের আর্টিকেলটি খুঁজে বের করা
    article = BlogModel.objects.filter(
        category=cat_id,
        disorder_slug=disorder_id,
        content_type=content_type_id
    ).first()
    
    # যদি ডাটাবেজে ওই সেক্টরে কোনো ডাটা আপলোড করা না থাকে, তবে একটি ডিফল্ট মেসেজ দেখাবে
    if not article:
        class DefaultArticle:
            title = "কন্টেন্ট পাওয়া যায়নি"
            content = "<h2>কন্টেন্ট এখনও আপলোড করা হয়নি</h2><p>এডমিন প্যানেল থেকে এই সেক্টরের জন্য কন্টেন্ট যুক্ত করুন।</p>"
            author = "DCPS Admin"
        article = DefaultArticle()
    
    context = {
        'cat_id': cat_id,
        'disorder_id': disorder_id,
        'content_type': content_type_id,
        'article': article, # সঠিক আর্টিকেল অবজেক্টটি পাঠানো হলো
    }
    return render(request, 'article.html', context)

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')

def all_articles_page(request):
    return render(request, 'allarticles.html')