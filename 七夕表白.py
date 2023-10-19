import tkinter as tk
import pygame
import random
import requests


#下载歌曲
url = 'https://webfs.tx.kugou.com/202309282119/8bdcedefb62a1c229446235fd3a037fc/v2/6a8038b2a92c807671df66b90a355b8e/KGTX/CLTX001/6a8038b2a92c807671df66b90a355b8e.mp3'
content = requests.get(url).content     #下载歌曲
f = open("music.mp3",'wb')              #新建文件
f.write(content)                        #写入文件
f.close()                               #关闭文件，防止内存消耗

#下载图片
url = 'https://pics1.baidu.com/feed/35a85edf8db1cb13798ab1c1bfbe034590584b72.png@f_auto?token=b0342225c2d0c16008fc4ff33ecf872b'
content0 = requests.get(url).content     #下载图片
x = open("img.jpg",'wb')                 #新建文件
x.write(content0)                        #写入文件
x.close()                                #关闭文件，防止内存消耗

# 创建窗口
for i in range(10):
    window = tk.Tk()
    window.title("七夕节快乐！")
    window.geometry("400x400")
    window.configure(bg="pink")


    # 设置文本
    texts = [
        "1、今天是七夕，我为你乞巧，希望你心灵手巧！天上牛郎织女来相会，地下多情人儿共祈爱情永恒不渝。我爱你！",
        "2、七夕的情，最真，因为有永恒的爱恋牵系；七夕的夜，最美，因为有美丽的传说点缀；七夕的祝福，最灵，因为有浪漫的星光见证：愿你爱情甜蜜，幸福如意！",
        "3、鹊桥美丽如故，思念堆积无数。心头对你思慕，七夕爱情倾诉。爱你如山坚固，真情一片永驻。携手追寻幸福，步入快乐旅途。七夕到了，爱你一万年。",
        "4、你不要偷偷摸摸躲躲藏藏慌慌张张了，快点投案自首！我会向月老求情的，你必须明白，爱上我不是罪过，快点向我示爱吧。",
        "5、你有一双迷人的黑瞳，有时忧心忡忡，有时单纯懵懂，总之令我怦然心动。素色的裙子在风中，尽情舞动。只想用最美的歌声来讲你赞颂。亲爱的，七夕快乐，让我们共同编织属于我们自己的美梦，让生活与众不同！",
        "6、天上雀桥结成之时，你我心丝相连，希望今后的每天我们也都朝朝暮暮。",
        "7、七夕之夜星麻麻，看着水里鱼双双。想到了你心一酸，唯有想着当初情？",
        "8、莫羡鹊桥仙，人间花更嫣；今沐七夕雨，爱你更心坚！",
        "9、天又给我一个约你的借口，相爱的人儿，与你共度，天天都是情人节。",
        "10、我对你的深情，愿你能“夕”罕。"
        #‘七夕表白情话语录大全’来源：https://baijiahao.baidu.com/s?id=1750845339073730489
    ]
    text = random.choice(texts)
    label = tk.Label(window, text=text, bg="pink", font=("Arial", 12), wraplength=300, justify="center")
    label.pack()

# 初始化pygame
pygame.init()

# 设置歌曲路径
song_path = "music.mp3"

# 创建窗口和音乐播放器
windows = []
player = pygame.mixer.music

# 播放歌曲
player.load(song_path)
player.play()

screen = pygame.display.set_mode((800, 600))
image = pygame.image.load("img.jpg")
screen.blit(image, (0, 0))
pygame.display.flip()

window.mainloop()