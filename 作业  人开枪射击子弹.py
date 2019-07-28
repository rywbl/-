#作业 人开枪射击子弹
import time

class Person(object):
	#bulletbox = 5
	#属性
	def __init__(self, name, bulletbox):
		self.name = name
		self.bulletbox = bulletbox 
	#方法
	def shoot(self):
		while self.bulletbox > 0:
			print("检查弹夹！")
			bb = self.bulletbox
			#time.sleep(1)
			print("还有%d发子弹！"%(bb))
			#time.sleep(1)
			print("开枪！")
			#time.sleep(1)
			print("打中了！")
			#time.sleep(1)
			print("还剩%d发子弹！"%(bb-1))
			self.bulletbox = bb -1
	def fill(self,num):
		bb = self.bulletbox
		print("还有%d发子弹，充填%d发子弹！"%(bb,num))
		#time.sleep(num/2)
		self.bulletbox = bb + num		
		bb = self.bulletbox
		print("充填完毕，剩余%d发子弹"%(bb))

	
#对象初始化		
per1 = Person("Jane",5)

#调用对象
print(per1.name,per1.bulletbox)
per1.shoot()
per1.fill(10)
per1.shoot()

per2 = Person("Sony",10)

print(per2.name,per2.bulletbox)
per2.shoot()
per2.fill(10)
per2.shoot()

