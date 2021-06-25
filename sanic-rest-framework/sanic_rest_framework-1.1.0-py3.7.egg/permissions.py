"""
@Author：WangYuXiang
@E-mile：Hill@3io.cc
@CreateTime：2021/4/25 16:51
@DependencyLibrary：无
@MainFunction：无
@FileDoc： 
    permissions.py
    文件说明
@ChangeHistory:
    datetime action why
    example:
    2021/4/25 16:51 change 'Fix bug'
        
"""


class CheckPermission:
    async def has_permission(self, request, view):
        pass

    async def has_obj_permission(self, request, view, obj):
        pass
