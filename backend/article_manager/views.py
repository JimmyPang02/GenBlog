from django.contrib.auth.models import User
from django.http import JsonResponse

from account_manager.models import DataLinker
from article_manager.models import Article
from get_jwt.jwt_controller import validate_access_jwt_intern


def create_article(request):
    access_token = request.POST.get('access_token')
    article_title = request.POST.get('article_title')
    article_content = request.POST.get('article_content')
    if request.method == 'POST':
        # 校验access_token
        validate_result = validate_access_jwt_intern(access_token)
        if validate_result[0]:
            current_user_str = validate_result[1]

            current_user = User.objects.get(username=current_user_str)

            current_user_id = current_user.id

            # 建立Article对象
            article = Article(author_id=current_user_id, title=article_title, content=article_content,
                              author_name=current_user_str)
            article.save()

            article_id = article.article_id

            # 建立DataLinker对象
            table = DataLinker.objects.get_or_create(user_id=current_user_id)
            table[0].article_list.add(article_id)

            # 返回JsonResponse，包含文章的标题，作者和编号
            return JsonResponse({'result': 'success', '文章标题:': article_title, '文章作者:': current_user_str,
                                 '文章编号:': article_id})
        else:
            return JsonResponse({'result': 'fail', 'reason': validate_result[1]})
    else:
        return JsonResponse({'result': 'fail', 'reason': '请求方式错误'})


def show_articles(request):
    access_token = request.POST.get('access_token')
    if request.method == 'POST':
        # 校验access_token
        validate_result = validate_access_jwt_intern(access_token)
        if validate_result[0]:
            current_user_str = validate_result[1]

            current_user = User.objects.get(username=current_user_str)
            current_user_id = current_user.id

            # 为current_user新建DataLinker对象，如果已存在，则不新建
            DataLinker.objects.get_or_create(user_id=current_user_id)

            # 获取current_user的DataLinker对象
            current_user_data_linker = DataLinker.objects.get(user_id=current_user_id)

            # 把article_list转换成一个新建的列表，列表里的元素包含模型Article里的title、content、author、create_time、update_time
            article_list = current_user_data_linker.article_list.all()
            article_list_str = []
            for article in article_list:
                article_list_str.append(
                    {'title': article.title, 'content': article.content, 'author': article.author_name,
                     'create_time': article.create_time, 'update_time': article.update_time})

            # 返回成功，并且说明文章数目
            return JsonResponse(
                {'result': '获取文章列表成功', 'current_user': current_user_str, 'article_count': len(article_list_str),
                 'article_list': article_list_str})

    else:
        return JsonResponse({'result': '仅支持POST调用，获取文章列表失败'})


def show_articles_by_id(request):
    access_token = request.POST.get('access_token')
    article_id = request.POST.get('article_id')
    if request.method == 'POST':
        # 校验access_token
        validate_result = validate_access_jwt_intern(access_token)
        if validate_result[0]:
            current_user_str = validate_result[1]
            # 获取article_id对应的文章,如果不存在，则返回失败
            try:
                article = Article.objects.get(article_id=article_id)
            except:
                return JsonResponse({'result': '获取文章失败，文章不存在'})

            # 进一步获取文章的作者、标题、内容、创建时间、更新时间
            article_author = article.author_name
            article_title = article.title
            article_content = article.content
            article_create_time = article.create_time
            article_update_time = article.update_time

            # 整合文章信息为列表
            article_info = {'article_author': article_author, 'article_title': article_title,
                            'article_content': article_content, 'article_create_time': article_create_time,
                            'article_update_time': article_update_time}

            # 返回成功，并包含上述列表
            return JsonResponse({'result': '获取文章成功', '文章信息': article_info})
        else:
            return JsonResponse({'result': 'fail', 'reason': validate_result[1]})
    else:
        return JsonResponse({'result': '仅支持POST调用，获取文章失败'})
