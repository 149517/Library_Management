from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
import json

from books.models import Book
from user.models import UserInfo

from record.models import Record


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def borrow_view(request):
    """
    添加数据，
    数据类型type: buy购书记录，borrow借阅记录
    用户:从token中添加用户id
    书籍：根据ISBN查询数据，添加数据的id
    :param request:
    :return:
    """
    if request.method == "POST":
        # 从请求数据中获取book的ISBN、type和令牌中的user_id
        isbn = request.data.get('isbn')
        type = request.data.get('type')
        user_id = request.user.id  # 从令牌中解析出user_id
        print(isbn,type,user_id)

        # 在Book模型中查找具有匹配ISBN的书籍记录
        try:
            book = Book.objects.get(isbn=isbn)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        # 创建一个新的记录并保存到数据库中
        record = Record(user_id=user_id, type=type, book=book)
        record.save()

        return Response({'message': 'Record created successfully'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_record_view(request):
    """
    获取用户额的记录
    :param request:type: 操作类型，buy, borrow
    token 获取用户
    """
    if request.method == 'POST':
        # 从请求数据中获取type值
        record_type = request.data.get('type')

        # 获取当前用户的id
        user_id = request.user.id

        # 根据用户id和type值查询多个Record对象
        records = Record.objects.filter(user=user_id, type=record_type)

        # 检查是否有记录
        if not records.exists():
            return JsonResponse({'error': 'Records not found'}, status=404)

        # 构建响应数据，将多个记录放入数组中
        response_data = {
            'user_id': user_id,
            'type': record_type,
            'records': []
        }

        for record in records:
            book = record.book
            time = record.addTime
            record_data = {
                'time': time,
                'book': {
                    'title': book.bookname,
                    'author': book.author,
                    'isbn': book.isbn,
                    'publisher': book.publisher,
                    'price': book.price
                }
            }
            response_data['records'].append(record_data)

        return JsonResponse(response_data, status=200)
