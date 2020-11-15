import re

from django.shortcuts import render

from .models import Good, GoodComment

chinese = '[\u4E00-\u9FA5]+'
number = '(\\d+(\\.\\d+)?)'


def index(request):
    queryset = Good.objects.all()
    goods = queryset.filter().all()
    return render(request, 'index.html', locals())


def index_search(request, content):
    queryset = Good.objects.all()
    conditions = {'name__contains': content}
    goods = queryset.filter(**conditions).all()
    return render(request, 'index.html', locals())


def page_comment(request, content):
    print(request)
    desc_search = request.GET.get('desc')
    start_date = request.GET.get('startDate')
    end_date = request.GET.get('endDate')
    queryset = Good.objects.all()
    conditions = {'id': content}
    goods = queryset.filter(**conditions).all()
    good_item = goods[0]
    top_words = re.findall(chinese, good_item.top_word)
    top_words2 = re.findall(number, good_item.top_word)
    top0 = top_words[0]
    top1 = top_words[1]
    top2 = top_words[2]
    top3 = top_words[3]
    top4 = top_words[4]
    weight = []
    for a in top_words2:
        weight.append(float(a[0]))
    queryset = GoodComment.objects.all()
    conditions = {'good_id': content}
    if desc_search:
        conditions['comment__contains'] = desc_search
    if start_date:
        start_date_new = start_date + ' 00:00:00'
        conditions['create_time__gt'] = start_date_new
    if end_date:
        end_date_new = end_date + ' 23:59:59'
        conditions['create_time__lt'] = end_date_new
    comments = queryset.filter(**conditions).all()
    good_comment = 0
    bad_comment = 0
    if len(comments) > 0:
        for comment_item in comments:
            if comment_item.positive == 0:
                good_comment = good_comment + 1
            else:
                bad_comment = bad_comment + 1
    return render(request, 'comment.html', locals())

