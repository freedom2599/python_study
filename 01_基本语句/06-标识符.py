"""
演示python中标识符的相关操作
"""
# 规则1.命名标识符只允许出现英文、中文、数字、下划线
# 注意！不推荐使用中文！！；数字不可以开头
# 举例
a = "英文"
例 = "中文（不推荐）"
_ = "下划线"
# 组合
a_1 = '字母下划线数字组合'
# 错误示例： 6 = "禁止数字"
# 规则2.大小写敏感
Admin = "用户1"
admin = "用户2"
print(Admin)
print(admin)
# 规则3.不可使用关键字
# False Ture None and as assert break class continue def del elif else
# except finally for form global if import in is lambda nonlocal not or
# pass raise return try while with yield
# 变量命名规范
