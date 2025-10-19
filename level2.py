from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import sys

app=Ursina()

window.borderless=False
window.fullscreen=True

dev_mode=False
cozum=5
filt_kontrol1=False
pil_kontrol1=False
araba_kontrol1=False


fabrika=Button(model="Factory.obj",color=color.white,texture="Factory_albedo.jpg",parent=scene)
Araba=Button(model="desoto.obj",color=color.white,texture="desoto_d.png",y=0,x=-15,z=20,parent=scene,scale=.05)
pil=Button(model="battery_alpha.obj",color=color.white,texture="battery_texture.png",x=-20,y=1,parent=scene)
ground=Button(model="cube",color=color.white,scale=(100,1,100),parent=scene,texture="grass",texture_scale=(100,100))

player = FirstPersonController(position=(0,0,30))

def filt_kontrol():
    global filt_kontrol1
    global cozum
    if cozum==1:
        filtre()
    else:
        txt=Text(text="önce elinize filtreyi alın",scale=3,color=color.red)
        invoke(txt.disable,delay=1)
        print("önce elinize filtreyi alin")


def araba_kontrol():
    global araba_kontrol1
    global cozum
    if cozum==3:
        araba()
    else:
        txt=Text(text="önce arabayı alın",scale=3,color=color.red)
        invoke(txt.disable,delay=1)
        print("önce arabayı alin")



def pil_kontrol():
    global pil_kontrol1
    global cozum
    if cozum==2:
        lion()
    else:
        txt=Text(text="önce elinize batarya alın",scale=3,color=color.red)
        invoke(txt.disable,delay=1)
        print("önce elinize batarya alin")


def filtre():
    global filt_kontrol1
    if filt_kontrol1==False:
        filt_kontrol1=True
        print("filtre takildi")
        agac=Button(model="tree.obj",texture="tree_text.png",color=color.white,x=30,z=30,parent=scene)
        txt=Text(text="filtre takıldı",scale=3,color=color.red)
        invoke(txt.disable,delay=1)
    else:
        print("filtre zaten takili")
        txt=Text(text="filtre zaten takılı",scale=3,color=color.red)
        invoke(txt.disable,delay=1)



def lion():
    global pil_kontrol1
    if pil_kontrol1==False:
        pil_kontrol1=True
        print("batarya takildi")
        txt=Text(text="batarya takıldı",scale=3,color=color.red)
        pil.model="battery_alp.obj"
        pil.texture="batterry.jpg"
        agac=Button(model="tree.obj",texture="tree_text.png",color=color.white,x=-20,z=25,parent=scene)
        invoke(txt.disable,delay=1)
    else:
        print("batarya zaten takili")
        txt=Text(text="batarya zaten takılı",scale=3,color=color.red)
        invoke(txt.disable,delay=1)


def araba():
    global araba_kontrol1
    if araba_kontrol1==False:
        araba_kontrol1=True
        Araba.model="e-car.obj"
        Araba.scale=.05
        txt=Text(text="araba değişti",scale=3,color=color.red)
        agac=Button(model="tree.obj",texture="tree_text.png",color=color.white,x=10,z=-30,parent=scene)
        agac=Button(model="tree.obj",texture="tree_text.png",color=color.white,x=10,z=20,parent=scene)
        invoke(txt.disable,delay=2)
        print("araba değişti")
    


def update():
    global cozum
    global dev_mode
    fabrika.on_click=filt_kontrol
    pil.on_click=pil_kontrol
    Araba.on_click=araba_kontrol
    if held_keys["1"]:
        cozum=1
    if held_keys["2"]:
        cozum=2
    if held_keys["3"]:
        cozum=3
    if held_keys["escape"] and dev_mode==False:
        mouse.locked=False
        mouse.visible=True
        dev_mode=True
    elif held_keys["escape"] and dev_mode==True:
        mouse.locked=True
        mouse.visible=False
        dev_mode=False


if filt_kontrol1==True and pil_kontrol1==True and araba_kontrol1==True:
    print("kapanıyor")
    exit()

else:
    pass


Sky(texture="sky_sunset")


app.run()