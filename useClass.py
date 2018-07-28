#ecoding=gbk
import Class
from Class import *


myDog=Dog('gaka',age=2)
print("my dog is named "+myDog.name+",and its age is "+str(myDog.age))
myDog.sit()
myDog.rollOver()

car=Car('andi','a4',2017)
car.describeCar()
car.updateOdometer(100)
car.readOdometer()


elecar=ElectriCar('tesla','s',2017,100)
elecar.describeCar()
elecar.updateOdometer(98)
elecar.readOdometer()
elecar.updateBettery(88)
elecar.readBattery()
elecar.battery.describeBattery()


from collections import OrderedDict

finalValue=OrderedDict()
finalValue['PI']=3.14159
finalValue['C']=3*10**6
finalValue['V']=340
for k,v in finalValue.items():
	print(k+":"+str(v))
	



























