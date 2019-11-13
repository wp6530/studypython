# import time
# def foo():
#     time.sleep(2)
#     print("this is foo")
#
# def bar(func):
#     start_time = time.time()
#     func()
#     end_time = time.time()
#     print("this is func time %s"%(end_time - start_time))
#     return func
#
#
# print("start")
# foo = bar(foo)
# foo()