# Context Manager
# 1 - version
# file = open('test.txt', 'r')

# 2-version
# try:
#     file = open('test.txt', 'r')
#     print(file.read())
# except FileNotFoundError as e:
#     print(e)
# finally:
#     if file and not file.closed:
#         file.close()
#
# # 3-version
# with open('test.txt', 'r') as f:
#     # print(f.read())
#

# example contextmanager created
# class ContextManger:
#     def __init__(self):
#         print("Init method called")
#
#     def __enter__(self):
#         print('Entering method')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Exiting method')
#
#
# with ContextManger() as f:
#     print('with method')
#

# example for advanced contextmanager with file
class OpenContextManager:
    def __init__(self, file, mode='r'):
        self.file = file
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file and not self.file.closed:
            self.file.close()


# with OpenContextManager('test.txt', 'r') as file:
# print(file.read())

with OpenContextManager('test.txt', 'w') as file:
    file.write('writing 1 \n')
    file.write('writing 2')
