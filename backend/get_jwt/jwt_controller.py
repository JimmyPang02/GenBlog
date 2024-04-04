import jwt

from GenBlogAPI.settings import SECRET_KEY


def validate_access_jwt_intern(access_token):
    if not access_token:
        return [False, 'access_token为空']
    try:
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=['HS256'])
        username = payload.get('username')
        type = payload.get('type')
    except jwt.ExpiredSignatureError:
        return [False, 'access_token已过期']
    except jwt.InvalidTokenError:
        return [False, 'access_token无效']
    if type != 'access':
        return [False, 'token不是access类型']
    # 返回列表
    return [True, username]
