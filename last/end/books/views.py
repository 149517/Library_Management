from books.models import Book
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

from django.http import JsonResponse, HttpResponse

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

def getList_view(requst):
    if requst.method == 'GET':
        books = Book.objects.all()
        book_list = []

        for book in books:
            book_info = {
                'value': book.bookname,
                'link': book.isbn
            }
            book_list.append(book_info)

        return HttpResponse(json.dumps(book_list, ensure_ascii=False), content_type='application/json')

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


def add_view(request):
    if request.method == 'POST':
        try:
            # 从请求体中解析出前端发送的book对象
            data = json.loads(request.body)
            book_data = data.get('book', {})  # 假设前端将数据放在名为'book'的字段中
            print(book_data)

            # 在这里执行保存或处理book数据的逻辑
            # 例如，使用Django模型创建新的书籍记录
            # 请根据您的模型和业务逻辑来实现
            # 以下示例假设您有一个名为Book的Django模型

            book_instance = Book(
                bookname=book_data.get('bookname'),
                pic=book_data.get('pic'),
                author=book_data.get('author'),
                isbn=book_data.get('isbn'),
                lang=book_data.get('lang'),
                publisher=book_data.get('publisher'),
                type=book_data.get('type'),
                price=book_data.get('price'),
                intro=book_data.get('intro'),
                Listing_time=book_data.get('Listing_time'),
            )
            book_instance.save()

            return JsonResponse({'message': '提交成功'})
        except Exception as e:
            return JsonResponse({'message': '提交失败', 'error': str(e)})

    return JsonResponse({'message': '仅支持POST请求'})


def fix_view(request):
    if request.method == 'POST':
        try:
            # 从请求体中解析出前端发送的book对象
            data = json.loads(request.body)
            isbn = data.get('isbn', '')
            book_data = data.get('book', {})  # 假设前端将数据放在名为'book'的字段中

            # 获取要修改的书籍记录
            book_isbn = book_data.get('isbn', None)  # 假设前端传递了书籍的唯一标识符
            if book_isbn is not None:
                try:
                    # 使用ISBN值来查询要修改的书籍记录
                    book_instance = Book.objects.get(isbn=book_isbn)

                    # 根据前端发送的book对象更新数据库记录的字段
                    book_instance.bookname = book_data.get('bookname', book_instance.bookname)
                    book_instance.pic = book_data.get('pic', book_instance.pic)
                    book_instance.author = book_data.get('author', book_instance.author)
                    book_instance.isbn = book_data.get('isbn', book_instance.isbn)
                    book_instance.lang = book_data.get('lang', book_instance.lang)
                    book_instance.publisher = book_data.get('publisher', book_instance.publisher)
                    book_instance.type = book_data.get('type', book_instance.type)
                    book_instance.price = book_data.get('price', book_instance.price)
                    book_instance.intro = book_data.get('intro', book_instance.intro)
                    book_instance.Listing_time = book_data.get('Listing_time', book_instance.Listing_time)
                    # 保存更新后的数据
                    book_instance.save()

                    return JsonResponse({'message': '修改成功'})
                except Book.DoesNotExist:
                    return JsonResponse({'message': '未找到书籍记录'})
            else:
                return JsonResponse({'message': '未提供书籍ID'})
        except Exception as e:
            return JsonResponse({'message': '修改失败', 'error': str(e)})

    return JsonResponse({'message': '仅支持POST请求'})
