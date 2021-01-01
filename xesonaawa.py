# 完整代码。
import meowbit,time 

#显示乌龟蛋
meowbit.screen.loadBmp("egg")
#获取温度
t = meowbit.sensor.getTemp()
#显示温度
meowbit.screen.showText("现在的温度是："+str(t),20,2)
#准备孵化
meowbit.screen.showText("马上开始孵化",30,110)
time.sleep(2)
#根据温度的不同，孵化不同属性的小乌龟
if t <= 15:
    for i in range(8):
        meowbit.screen.loadBmp("eggLeft")
        time.sleep(0.1)
        meowbit.screen.loadBmp("eggRight")  
        time.sleep(0.1)
    meowbit.screen.loadBmp("ice")    
    meowbit.buzzer.melody(10) 

if t > 15 and t <= 20:
    for i in range(8):
        meowbit.screen.loadBmp("eggLeft")
        time.sleep(0.1)
        meowbit.screen.loadBmp("eggRight")  
        time.sleep(0.1)
    meowbit.screen.loadBmp("water")   
    meowbit.buzzer.melody(10)
        
if t > 20 and t <= 25:
    for i in range(8):
        meowbit.screen.loadBmp("eggLeft")
        time.sleep(0.1)
        meowbit.screen.loadBmp("eggRight")  
        time.sleep(0.1)
    meowbit.screen.loadBmp("metal")    
    meowbit.buzzer.melody(10)
        
if  t > 25:
    for i in range(8):
        meowbit.screen.loadBmp("eggLeft")
        time.sleep(0.1)
        meowbit.screen.loadBmp("eggRight")  
        time.sleep(0.1)
    meowbit.screen.loadBmp("fire")     
    meowbit.buzzer.melody(10)