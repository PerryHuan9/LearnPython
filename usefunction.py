#ecoding=gbk
from function import *
#可直接使用函数，但可能覆盖本文件中的同名函数
import function 
#使用import 文件名 导入函数，下面使用函数时需使用句点表示法


function.describe_pet("狗",'包子')
describe_pet(pet_type='cat',name='kaka')
hello('黄益凛')
describe_pet('rabbit')
print(add(3.14,8))
print(buildPersion("perry","huang",18))
names=['perry','ximon','zudi','jack']
showList(names)

unprintedModels=['iphone case','robot pendant','dodecahedron']
printedModels=['Huawei case']
printModels(unprintedModels[:],printedModels)
print(printedModels)
print(unprintedModels)

makePizza('香橙')
makePizza('苹果','石榴','香蕉',88520)
print()
pofile=buildPofile('perry',"huang",age=21,sex="男",身份="学生")
print(pofile)

