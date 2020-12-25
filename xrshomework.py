#补充第18行代码，检测是否按下左键
#补充第20行代码，加1分
#补充第22行代码，播放正确提示音
#补充第25行代码，检测是否按下右键
#补充第27行代码，播放错误提示音
#补充第32行代码，刷新屏幕

import meowbit,time

score = 0

#第一题
meowbit.screen.showText("dinosaur",50,35)
meowbit.screen.showText("恐龙   大象",35,80)

for i in range(200):
    #补充代码，检测是否按下左键
    if meowbit.sensor.btnValue("left")==1:
        #补充代码，加1分
        score = score + 1
        #补充代码，播放正确提示音
        meowbit.buzzer.melody(1)
        break
    #补充代码，检测是否按下右键
    if meowbit.sensor.btnValue("rigut")==1:
        #补充代码，播放错误提示音
        meowbit.buzzer.melody(2)
        break
    time.sleep(0.01)

#补充代码，刷新屏幕
meowbit.screen.fill((0,0,0))

#第二题
meowbit.screen.showText("eggplant",40,35)
meowbit.screen.showText("鸡蛋   茄子",35,80)
for i in range(200):
    if meowbit.sensor.btnValue("left")==1:
        meowbit.buzzer.melody(2)
        break
    if meowbit.sensor.btnValue("right")==1:
        score = score + 1
        meowbit.buzzer.melody(1)
        break
    time.sleep(0.01)



#想要添加更多的单词，每次将下面的代码进行复制粘贴。
#如果你添加的单词正确选项在左边，请将条件判断中的left改成right，right改为left。
#************************************
#刷新屏幕
meowbit.screen.fill((0,0,0))

#第三题
meowbit.screen.showText("tomato",40,35)
meowbit.screen.showText("土豆   西红柿",35,80)

for i in range(200):
    if meowbit.sensor.btnValue("left")==1:
        meowbit.buzzer.melody(2)
        break
    if meowbit.sensor.btnValue("right")==1:
        score = score + 1
        meowbit.buzzer.melody(1)
        break
    time.sleep(0.01)
#************************************

#刷新屏幕        
meowbit.screen.fill((0,0,0))
#显示答对单词数
meowbit.screen.showText("恭喜你，答对"+str(score)+"个单词！",15,60)
meowbit.buzzer.melody(7)