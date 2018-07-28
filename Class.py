#ecoding=gbk

class Dog():
	"""小狗类"""
	def __init__(self,name,age):
		"""类初始化方法"""
		self.name=name.title()
		self.age=age
		
	def sit(self):
		print(self.name+" is now sitting.")
		
	def rollOver(self):
		print(self.name+" is now rolling over.")
		
		
class Car():
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer=0
	
	def describeCar(self):
		carStr=self.make+' '+self.model+' '+str(self.year)
		print(carStr.title())
	
	def readOdometer(self):
		print("The odometer of this car is "+str(self.odometer)+".")
		
	def updateOdometer(self,mileage):
		self.odometer+=mileage
		
		
class Battery():
	def __init__(self,size=100):
		self.size=size
	def describeBattery(self):
		print("this battery has "+str(self.size)+"% power.")
		
		
class ElectriCar(Car):
	def __init__(self,make,model,year,batterySize):
		super().__init__(make,model,year)
		self.battery=Battery(batterySize);
		
	def updateBettery(self,battery):
		if self.battery.size>battery:
			self.battery.size=battery
		else:
			print("power can't increase without recharge")
	
	def readBattery(self):
		print("The battery now is "+str(self.battery.size)+".")

		
		

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































