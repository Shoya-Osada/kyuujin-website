from rest_framework import permissions

#Django REST Framework が提供するパーミッションシステムを使用して、API を安全する。

#機能
#認証されたユーザーのみに API へのアクセスを許可する
#許可されたユーザーのみに書き込み権限を与える


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)

        return request.method in permissions.SAFE_METHODS or is_admin