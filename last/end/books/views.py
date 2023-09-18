from books.models import Book
from django.core import serializers
from django.core.paginator import Paginator

from django.http import JsonResponse

import json


def all_view(request):
    books = Book.objects.all().order_by('id')
    paginator = Paginator(books, 4)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # 将QuerySet序列化为JSON格式
    serialized_data = serializers.serialize('json', page_obj)

    # 转换为Python数据结构
    data = json.loads(serialized_data)

    # 构建包含分页信息的字典
    pagination_info = {
        "total_pages": paginator.num_pages,
        "current_page": page_obj.number,
        "has_next": page_obj.has_next(),
        "has_previous": page_obj.has_previous(),
    }

    return JsonResponse({"data": data, "pagination_info": pagination_info}, safe=False)


def query_view(request):

    # 书籍查询，
    # 参数：
    # name
    # 书籍的某个信息
    # way
    # 书籍信息参数
    name = request.POST.get('name')
    way = request.POST.get('way')
    # print(name, way)

    if way == 'bookname':
        books = Book.objects.filter(bookname=name)
    elif way == 'isbn':
        books = Book.objects.filter(isbn=name)
    elif way == 'publisher':
        books = Book.objects.filter(publisher=name)
    elif way == 'author':
        books = Book.objects.filter(author=name)
    else:
        books = None

    # 使用Django序列化将查询结果转化为JSON格式，然后使用json.loads去掉转义符号
    book_data = serializers.serialize('json', books)
    book_data = json.loads(book_data)

    # 使用JsonResponse返回数据
    return JsonResponse({'books': book_data}, safe=False)
