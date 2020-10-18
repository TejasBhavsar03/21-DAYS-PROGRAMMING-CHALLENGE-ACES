# Global Scope
x = 1


def fun():
    # Local Scope
    # global x
    # x = 1
    def fun2():
        print(x)

    fun2()


fun()

print(x)
# Non Local Key word
    global scope
    def fun1():
       # enclosing function/scope
       def fun2():
          # neseted function
          # local scope
          print(2)
       fun2()
       print(1)
    fun1()
    ************************************
    # Exercise non local

    #
    # def fun1():
    # 	def fun2():
    # 		print(1)
    # 	fun2()
    # 	print(2)
    # fun1()
# Global Space
#     # def washingmachine():
#     #  # Enclosing function
#     #
#     #  clothes = 'Dry and Clean'
#     #  def dryclean():
#     #     # Nested Function
#     #     nonlocal clothes
#     #     clothes = 'Dry and Clean'
#     #     print(clothes)
#     #  dryclean()
#     #  print(clothes)
#     #
#     # washingmachine()