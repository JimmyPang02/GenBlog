from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from account_manager.models import DataLinker
from article_manager.models import Article
from get_jwt.jwt_controller import validate_access_jwt_intern


@csrf_exempt
def get_user_list(request, page_begin, page_end):
    if request.method == 'GET':
        # 按页码，获取user数据库里的10个用户,只获取username和last_login字段，并按last_login降序排列，一一对应
        user_list = User.objects.all().order_by('-last_login').values('username', 'last_login')[page_begin:page_end]
        return JsonResponse({'result': '获取用户列表成功', 'user_list': list(user_list)})
    else:
        return JsonResponse({'result': '仅支持GET调用，获取用户列表失败'})


@csrf_exempt
def follow_user(request):
    access_token = request.POST.get('access_token')
    follow_user_str = request.POST.get('follow_user')
    if request.method == 'POST':
        # 校验access_token
        validate_result = validate_access_jwt_intern(access_token)
        if validate_result[0]:
            current_user_str = validate_result[1]

            current_user = User.objects.get(username=current_user_str)
            follow_user = User.objects.get(username=follow_user_str)

            current_user_id = current_user.id
            follow_user_id = follow_user.id

            # 为current_user新建DataLinker对象，如果已存在，则不新建
            DataLinker.objects.get_or_create(user_id=current_user_id)

            # 为follow_user新建DataLinker对象，如果已存在，则不新建
            DataLinker.objects.get_or_create(user_id=follow_user_id)

            # 获取current_user的DataLinker对象
            current_user_data_linker = DataLinker.objects.get(user_id=current_user_id)
            current_user_data_linker.followed_user_list.add(follow_user_id)
            current_user_data_linker.save()

            # 返回成功，并且注明谁关注了谁
            return JsonResponse(
                {'result': '关注用户成功', 'current_user': current_user_str, 'follow_user': follow_user_str})
    else:
        return JsonResponse({'result': '仅支持POST调用，关注用户失败'})


@csrf_exempt
def unfollow_user(request):
    access_token = request.POST.get('access_token')
    unfollow_user_str = request.POST.get('unfollow_user')
    if request.method == 'POST':
        # 校验access_token
        validate_result = validate_access_jwt_intern(access_token)
        if validate_result[0]:
            current_user_str = validate_result[1]

            current_user = User.objects.get(username=current_user_str)
            unfollow_user = User.objects.get(username=unfollow_user_str)

            current_user_id = current_user.id
            unfollow_user_id = unfollow_user.id

            # 为current_user新建DataLinker对象，如果已存在，则不新建
            DataLinker.objects.get_or_create(user_id=current_user_id)

            # 为unfollow_user新建DataLinker对象，如果已存在，则不新建
            DataLinker.objects.get_or_create(user_id=unfollow_user_id)

            # 获取current_user的DataLinker对象
            current_user_data_linker = DataLinker.objects.get(user_id=current_user_id)
            current_user_data_linker.followed_user_list.remove(unfollow_user_id)
            current_user_data_linker.save()

            # 返回成功，并且注明谁取消关注了谁
            return JsonResponse(
                {'result': '取消关注用户成功', 'current_user': current_user_str, 'unfollow_user': unfollow_user_str})
    else:
        return JsonResponse({'result': '仅支持POST调用，取消关注用户失败'})


def show_followers(request):
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
            followed_user_list = current_user_data_linker.followed_user_list.all()

            # 把followed_user_list转换成一个新建的列表，列表里的元素是followed_user_list里的每个元素的username
            followed_user_id_list_str = []
            for followed_user in followed_user_list:
                followed_user_id_list_str.append(followed_user.user_id)

            # 根据followed_user_id_list_str，获取username
            followed_user_name_list_str = []
            for followed_user_id in followed_user_id_list_str:
                followed_user_name_list_str.append(User.objects.get(id=followed_user_id).username)

            # 返回成功，并且注明谁关注了谁
            return JsonResponse({'result': '获取关注用户列表成功', 'current_user': current_user_str,
                                 'followed_user_id_list': followed_user_id_list_str,
                                 'followed_user_name_list': followed_user_name_list_str})



    else:
        return JsonResponse({'result': '仅支持POST调用，获取关注用户列表失败'})


def update_user_info(request):
    access_token = request.POST.get('access_token')
    if request.method == 'POST':
        # 校验access_token
        validate_result = validate_access_jwt_intern(access_token)
        if validate_result[0]:
            current_user_str = validate_result[1]

            current_user = User.objects.get(username=current_user_str)
            current_user_id = current_user.id

            # 为current_user新建DataLinker对象，如果已存在，则不新建
            current_user_data_linker = DataLinker.objects.get_or_create(user_id=current_user_id)[0]

            # 获取用户信息avatar_url和self_indroduction
            avatar_url = request.POST.get('avatar_url')
            self_indroduction = request.POST.get('self_indroduction')

            # 更新用户信息
            current_user_data_linker.avatar_url = avatar_url
            current_user_data_linker.self_indroduction = self_indroduction
            current_user_data_linker.save()

            # 返回成功，注明更新的信息
            return JsonResponse(
                {'result': '更新用户信息成功', 'current_user': current_user_str, 'avatar_url': avatar_url,
                 'self_indroduction': self_indroduction})

        else:
            return JsonResponse({'result': '更新用户信息失败'})
    else:
        return JsonResponse({'result': '仅支持POST调用，更新用户信息失败'})


def get_current_user_info(request):
    access_token = request.POST.get('access_token')
    if request.method == 'POST':
        # 校验access_token
        validate_result = validate_access_jwt_intern(access_token)
        if validate_result[0]:
            current_user_str = validate_result[1]

            current_user = User.objects.get(username=current_user_str)
            current_user_id = current_user.id

            # 为current_user新建DataLinker对象，如果已存在，则不新建
            current_user_data_linker = DataLinker.objects.get_or_create(user_id=current_user_id)[0]

            # 获取用户信息avatar_url和self_introduction
            avatar_url = current_user_data_linker.avatar_url
            self_introduction = current_user_data_linker.self_introduction

            # 获取用户的被关注数和关注数
            followed_user_list = current_user_data_linker.followed_user_list.all()
            followed_user_num = len(followed_user_list)  # 指定用户关注的用户数
            follower_user_list = DataLinker.objects.filter(followed_user_list=current_user_id)
            follower_user_num = len(follower_user_list)  # 指定用户的粉丝数

            # 获取用户发布的文章数
            article_list = Article.objects.filter(author_id=current_user_id)
            article_num = len(article_list)

            # 获取用户id
            user_id = current_user.id

            # 返回成功，并包含上述内容
            return JsonResponse({'result': '获取用户信息成功', '当前用户id': user_id, '当前用户名': current_user_str,
                                 '头像链接': avatar_url,
                                 '自我介绍': self_introduction, '关注数': followed_user_num,
                                 '粉丝数': follower_user_num, '文章数': article_num})

        else:
            return JsonResponse({'result': '获取用户信息失败', '原因': validate_result[1]})
    else:
        return JsonResponse({'result': '仅支持POST调用，获取用户信息失败'})
