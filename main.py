from ursina import *
import subprocess

app = Ursina()

window.boderless=False

txt=Text(text="SON-BAHAR",scale=3,color=color.gold,y=.3,x=-.3)

def calistir3():
    subprocess.Popen(["python","level3.py"])

def calistir2():
    subprocess.Popen(["python","level2.py"])

def calistir1():
    subprocess.Popen(["python","level1.py"])

level3=Button(scale=2,color=color.red,text="bölüm 3",parent=scene,x=3)
level2=Button(scale=2,color=color.red,text="bölüm 2",parent=scene,x=0)
level1=Button(scale=2,color=color.red,text="bölüm 1",parent=scene,x=-3)

level1.on_click=calistir1
level2.on_click=calistir2
level3.on_click=calistir3

app.run()