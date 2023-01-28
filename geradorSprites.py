# -*- coding: utf-8 -*-
###########################################################
#       Addon Gerador de Sprite by Anderson Paulo         #
#                                                         #
#                                                         #
###########################################################

bl_info = {
    "name": "Gerador de Sprites",
    "author": "Anderson Paulo",
    "version": (0, 0, 2),
    "blender": (2, 79, 7),
    "location": "View3D > Tool Shelf > Tools",
    "description": "Cria Sprite com todos as direções",
    "category": "3D View",
}

import bpy
import os, sys
import math
import json
from PIL import Image
import re
#Essa função cria a Pasta principal e as subPastas ,já nomeadas,aonde serão guardados as imagens
def Pasta_Arquivo(self,context):
    try:  
        if bpy.context.scene.QueryProps.Pasta != "" and bpy.context.scene.QueryProps.Direcoes == "2":
            up = "Up"
            down = "Down"
            left ="Left"
            right ="Right"
            pasta = bpy.context.scene.QueryProps.Pasta 
            parent_dir= bpy.context.scene.QueryProps.CaminhoPaht 
            path = os.path.join(parent_dir,pasta)
            dirs = os.listdir(parent_dir)
            for file in dirs:
                if file != pasta:
                    
                    os.mkdir(path) 
                    parent_dir2 = bpy.context.scene.QueryProps.CaminhoPaht + bpy.context.scene.QueryProps.Pasta +"/"   
                    path_up = os.path.join(parent_dir2,up)
                    path_down = os.path.join(parent_dir2,down)
                    path_left = os.path.join(parent_dir2,left)
                    path_right = os.path.join(parent_dir2,right)
                    os.mkdir(path_up)
                    os.mkdir(path_down)
                    os.mkdir(path_left)
                    os.mkdir(path_right)
        if bpy.context.scene.QueryProps.Pasta != "" and bpy.context.scene.QueryProps.Direcoes == "1":
            
            up = "Up"
            Up_Left = "Up_Left"
            Up_Right = "Up_Right"
            Down_Left = "Down_Left"
            Down_Right = "Down_Right"
            
            down = "Down"
            left ="Left"
            right ="Right"
            pasta = bpy.context.scene.QueryProps.Pasta 
            parent_dir= bpy.context.scene.QueryProps.CaminhoPaht 
            path = os.path.join(parent_dir,pasta)
            dirs = os.listdir(parent_dir)
            for file in dirs:
                if file != pasta:
                    
                    os.mkdir(path) 
                    parent_dir2 = bpy.context.scene.QueryProps.CaminhoPaht + bpy.context.scene.QueryProps.Pasta +"/"   
                    
                    path_up = os.path.join(parent_dir2,up)
                    path_down = os.path.join(parent_dir2,down)
                    path_left = os.path.join(parent_dir2,left)
                    path_right = os.path.join(parent_dir2,right)
                    
                    path_up_left = os.path.join(parent_dir2,Up_Left)
                    path_down_left = os.path.join(parent_dir2,Down_Left)
                    path_down_right = os.path.join(parent_dir2,Down_Right)
                    path_up_right = os.path.join(parent_dir2,Up_Right)
                    
                    os.mkdir(path_up)
                    os.mkdir(path_down)
                    os.mkdir(path_left)
                    os.mkdir(path_right)
                    
                    os.mkdir(path_up_left)
                    os.mkdir(path_down_left)
                    os.mkdir(path_down_right)
                    os.mkdir(path_up_right)
                        

                
    except OSError as error:
        print(error)
#Função para posicionar a camera ,na posição isometrica ou 2D.
def CameraNada(self,context):
        
    scena =context.scene
    objetos=scena.objects

    for obj in objetos :
        
      
        if obj.name == "Camera":
            
                
            if bpy.context.scene.QueryProps.Camera_Nada == True:
                bpy.context.scene.QueryProps.normal_Cam = False
                bpy.context.scene.QueryProps.IsoMetric_Cam = False
                bpy.context.scene.objects.active= obj
                bpy.context.object.data.type = "ORTHO"
                bpy.context.object.data.sensor_width = 32
                bpy.context.object.data.sensor_fit = "AUTO"
                bpy.context.object.data.ortho_scale = 8.714
                obj.rotation_euler= (5101.83,0,0)
                obj.location=(0,-19.1952,12.7459)
                
def CameraISOmetric(self,context):
        
    scena =context.scene
    objetos=scena.objects

    for obj in objetos :
        
      
        if obj.name == "Camera":
            
                
            if bpy.context.scene.QueryProps.IsoMetric_Cam == True:
                bpy.context.scene.QueryProps.normal_Cam = False
                bpy.context.scene.QueryProps.Camera_Nada = False
                bpy.context.scene.objects.active= obj
                bpy.context.object.data.type = "ORTHO"
                bpy.context.object.data.sensor_width = 32
                bpy.context.object.data.sensor_fit = "AUTO"
                bpy.context.object.data.ortho_scale = 8.714
                obj.rotation_euler=(0.955323,0,0)
                obj.location=(0.0519361,-4.75023,7.46402)
                

              
def CameraNormal(self,context):
        
    scena =context.scene
    objetos=scena.objects

    for obj in objetos :
        
      
        if obj.name == "Camera":
            
            if bpy.context.scene.QueryProps.normal_Cam == True:
                bpy.context.scene.QueryProps.IsoMetric_Cam = False
                bpy.context.scene.QueryProps.Camera_Nada = False
                bpy.context.scene.objects.active= obj
                bpy.context.object.data.type = "ORTHO"
                bpy.context.object.data.sensor_width = 32
                bpy.context.object.data.ortho_scale = 8.714
                bpy.context.object.data.sensor_fit = "AUTO"
                obj.rotation_euler=(89.5682,0,0)
                obj.location=(0,-40,0)


            
class QueryProps(bpy.types.PropertyGroup):
    #Essa classe basicamente organiza as propriedades que serão chamandas no painel,Elas poderão serem chamadas em qualquer momento no script
    CaminhoPaht = bpy.props.StringProperty(default="C:\SpriterSheet/")
    Pasta = bpy.props.StringProperty(default="Frames",update=Pasta_Arquivo)
    Sprite_Name = bpy.props.StringProperty(default="0")
    Target_ = bpy.props.StringProperty(default="")
    Frames1_ =  bpy.props.IntProperty(
		name = "Frames",
		description = "",
		default = 1,
		min = 1,
		max = 1
  )
    Frames2_ =  bpy.props.IntProperty(
		name = "Frames",
		description = "",
		default = 1,
		min = 1,
		max = 300
  )
    size_X = bpy.props.EnumProperty(name="Dreções", description="",items=(('2048', "1024 ", ""),
           ('1024', "512 ", ""),
           ('512', "256 ", ""),
           ('256', "128", "")),    
       default='512')
       
    size_Y = bpy.props.EnumProperty(name="Dreções", description="",items=(('2048', "1024 ", ""),
           ('1024', "512 ", ""),
           ('512', "256 ", ""),
           ('256', "128", "")),       
              default='512') 
    IsoMetric_Cam = bpy.props.BoolProperty(name="Visão Isometrica",description="Posição da camera1",default = False, update = CameraISOmetric)
    normal_Cam = bpy.props.BoolProperty(name="Visão Frontal",description="Posição da camera2",default = False, update = CameraNormal )
    Camera_Nada = bpy.props.BoolProperty(name="Visão Nada",description="Posição da camera3",default = False, update = CameraNada )
    
    Direcoes = bpy.props.EnumProperty(name="Dreções", description="",items=(('1',"8 Direções Isometrico",""),
           ('2', "4 Direções Isometrico",""),
           ('3', "Zerar","")),
            default='3'  )

class Render_Sprites(bpy.types.Operator):
    bl_idname = "object.render_"
    bl_label = "Render Sprite"   
    


    def execute(self, context):
        #nome das pasas ,aonde serão guardadas as imagens
        up = "Up"
        down = "Down"
        left ="Left"
        right ="Right"
        
        Up_Left = "Up_Left"
        Up_Right = "Up_Right"
        Down_Left = "Down_Left"
        Down_Right = "Down_Right"
        #Recebo a pasta Principal aonde guardará os sprites
        pasta = bpy.context.scene.QueryProps.Pasta
        #Caminho abosoluto do diretorio
        parent_dir= bpy.context.scene.QueryProps.CaminhoPaht 
        #Camino aonde as imagens serão guardadas em suas respectivas pastas e já nomeadas,com o nome principal(4 direções principais)
        parent_dir_Up = parent_dir + pasta +"/"+up+"/"+bpy.context.scene.QueryProps.Sprite_Name
        parent_dir2_Down = parent_dir + pasta +"/"+down+"/"+bpy.context.scene.QueryProps.Sprite_Name
        parent_dir2_Left = parent_dir + pasta +"/"+left+"/"+bpy.context.scene.QueryProps.Sprite_Name
        parent_dir2_Right = parent_dir + pasta +"/"+right+"/"+bpy.context.scene.QueryProps.Sprite_Name
        #Camino aonde as imagens serão guardadas em suas respectivas pastas e já nomeadas,com o nome principal(4 direções alternativas)
        parent_dir2_Up_Left = parent_dir + pasta +"/"+Up_Left+"/"+bpy.context.scene.QueryProps.Sprite_Name
        parent_dir2_Up_Right = parent_dir + pasta +"/"+Up_Right+"/"+bpy.context.scene.QueryProps.Sprite_Name
        parent_dir2_Down_Left = parent_dir + pasta +"/"+Down_Left+"/"+bpy.context.scene.QueryProps.Sprite_Name
        parent_dir2_Down_right = parent_dir + pasta +"/"+Down_Right+"/"+bpy.context.scene.QueryProps.Sprite_Name
        # diretorio e nome principal,para sequencia das animacoes
        path = os.path.join(parent_dir,pasta)
        path2 = path+"/"+bpy.context.scene.QueryProps.Sprite_Name
        #Recebe o target do cubo para girar os graus
        targ = bpy.context.scene.QueryProps.Target_ 
        #Redimensiona as imagens em pixels
        bpy.context.scene.render.resolution_x = int(bpy.context.scene.QueryProps.size_X)
        bpy.context.scene.render.resolution_y = int(bpy.context.scene.QueryProps.size_Y)
        scena =context.scene
        objetos=scena.objects
        
        rotations = [0,45,90,135,180,225,270,315,316]
        rotations2 = [0,90,180,270,271]
        #Recebe o frame inicial e final
        bpy.context.scene.frame_start =bpy.context.scene.QueryProps.Frames1_
        bpy.context.scene.frame_end = bpy.context.scene.QueryProps.Frames2_
        for obj in objetos :
                    
                if obj.name == targ :  
                    bpy.context.scene.objects.active= obj #O cubo terá que estar selecionado para que a rotação automática funcione
                    bpy.ops.object.rotation_clear(clear_delta= False)
                    
                    
                    if bpy.context.scene.QueryProps.Direcoes == "1"  and bpy.context.scene.QueryProps.Sprite_Name !="":
                        
                        for ang in rotations:
                                                                                                             
                            if ang <=316:
                                                                                
                                
                                if ang == 0:
                                    for fr in range(bpy.context.scene.frame_start,(bpy.context.scene.frame_end+1)):
                                        num = fr
                                        bpy.context.scene.frame_set(num)
                                        bpy.context.scene.render.alpha_mode = 'TRANSPARENT'
                                        bpy.context.scene.render.image_settings.color_mode ='RGBA'
                                        bpy.context.scene.render.filepath = parent_dir2_Down+str(num)
                                        bpy.ops.render.render(use_viewport = True,write_still=True)
                                        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                                       
                                        
                                if ang == 45:
                                    bpy.ops.transform.rotate(value=0.785398, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0.385543)
                                    if True:
                                        for fr in range(bpy.context.scene.frame_start,(bpy.context.scene.frame_end+1)):
                                            num = fr
                                            bpy.context.scene.frame_set(num)
                                            bpy.context.scene.render.alpha_mode = 'TRANSPARENT'
                                            bpy.context.scene.render.image_settings.color_mode ='RGBA'
                                            bpy.context.scene.render.filepath = parent_dir2_Down_right+str(num)
                                            bpy.ops.render.render(use_viewport = True,write_still=True)
                                            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                                           
                                if ang == 90:
                                    bpy.ops.transform.rotate(value=0.785398, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0.385543)
                                    if True:
                                        for fr in range(bpy.context.scene.frame_start,(bpy.context.scene.frame_end+1)):
                                            num = fr
                                            bpy.context.scene.frame_set(num)
                                            bpy.context.scene.render.alpha_mode = 'TRANSPARENT'
                                            bpy.context.scene.render.image_settings.color_mode ='RGBA'
                                            bpy.context.scene.render.filepath = parent_dir2_Right+str(num)
                                            bpy.ops.render.render(use_viewport = True,write_still=True)
                                            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                                           
                                if ang == 135:
                                    bpy.ops.transform.rotate(value=0.785398, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0.385543)
                                    if True:
                                        for fr in range(bpy.context.scene.frame_start,(bpy.context.scene.frame_end+1)):
                                            num = fr
                                            bpy.context.scene.frame_set(num)
                                            bpy.context.scene.render.alpha_mode = 'TRANSPARENT'
                                            bpy.context.scene.render.image_settings.color_mode ='RGBA'
                                            bpy.context.scene.render.filepath = parent_dir2_Up_Right+str(num)
                                            bpy.ops.render.render(use_viewport = True,write_still=True)
                                            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)  
                                           
                                if ang == 180:
                                    bpy.ops.transform.rotate(value=0.785398, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0.385543)
                                    if True:
                                        for fr in range(bpy.context.scene.frame_start,(bpy.context.scene.frame_end+1)):
                                            num = fr
                                            bpy.context.scene.frame_set(num)
                                            bpy.context.scene.render.alpha_mode = 'TRANSPARENT'
                                            bpy.context.scene.render.image_settings.color_mode ='RGBA'
                                            bpy.context.scene.render.filepath = parent_dir_Up+str(num)
                                            bpy.ops.render.render(use_viewport = True,write_still=True)
                                            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                                    
                                if ang == 225:
                                    bpy.ops.transform.rotate(value=0.785398, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0.385543)
                                    if True:
                                        for fr in range(bpy.context.scene.frame_start,(bpy.context.scene.frame_end+1)):
                                            num = fr
                                            bpy.context.scene.frame_set(num)
                                            bpy.context.scene.render.alpha_mode = 'TRANSPARENT'
                                            bpy.context.scene.render.image_settings.color_mode ='RGBA'
                                            bpy.context.scene.render.filepath = parent_dir2_Up_Left+str(num)
                                            bpy.ops.render.render(use_viewport = True,write_still=True)
                                            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                                    
                                if ang == 270:
                                    bpy.ops.transform.rotate(value=0.785398, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0.385543)
                                    if True:
                                        for fr in range(bpy.context.scene.frame_start,(bpy.context.scene.frame_end+1)):
                                            num = fr
                                            bpy.context.scene.frame_set(num)
                                            bpy.context.scene.render.alpha_mode = 'TRANSPARENT'
                                            bpy.context.scene.render.image_settings.color_mode ='RGBA'
                                            bpy.context.scene.render.filepath = parent_dir2_Left+str(num)
                                            bpy.ops.render.render(use_viewport = True,write_still=True)
                                            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                                
                                if ang == 315:
                                    bpy.ops.transform.rotate(value=0.785398, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0.385543)
                                    if True:
                                        for fr in range(bpy.context.scene.frame_start,(bpy.context.scene.frame_end+1)):
                                            num = fr
                                            bpy.context.scene.frame_set(num)
                                            bpy.context.scene.render.alpha_mode = 'TRANSPARENT'
                                            bpy.context.scene.render.image_settings.color_mode ='RGBA'
                                            bpy.context.scene.render.filepath = parent_dir2_Down_Left+str(num)
                                            bpy.ops.render.render(use_viewport = True,write_still=True)
                                            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)      
                                    
                                
                    if bpy.context.scene.QueryProps.Direcoes == "2" and bpy.context.scene.QueryProps.Sprite_Name !="":
                        
                        for ang in rotations2:
                            
                            if ang <=271:
                                    
                                                                
                                if ang == 0:
                                    for fr in range(bpy.context.scene.frame_start,(bpy.context.scene.frame_end+1)):
                                        
                                        num = fr
                                        bpy.context.scene.frame_set(num)
                                        bpy.context.scene.render.alpha_mode = 'TRANSPARENT'
                                        bpy.context.scene.render.image_settings.color_mode ='RGBA'
                                        bpy.context.scene.render.filepath = parent_dir2_Down +str(num)
                                        bpy.ops.render.render(use_viewport = True,write_still=True)
                                        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                                            
                                if ang == 90:
                                        bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0.385543)
                                        if True:
                                            for fr in range(bpy.context.scene.frame_start,(bpy.context.scene.frame_end+1)):

                                                num = fr
                                                bpy.context.scene.frame_set(num)
                                                bpy.context.scene.render.alpha_mode = 'TRANSPARENT'
                                                bpy.context.scene.render.image_settings.color_mode ='RGBA'
                                                bpy.context.scene.render.filepath = parent_dir2_Right+str(num)
                                                bpy.ops.render.render(use_viewport = True,write_still=True)
                                                bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                                        
                                if ang == 180:
                                    bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0.385543)
                                    if True:
                                        for fr in range(bpy.context.scene.frame_start,(bpy.context.scene.frame_end+1)):

                                            num = fr
                                            bpy.context.scene.frame_set(num)
                                            bpy.context.scene.render.alpha_mode = 'TRANSPARENT'
                                            bpy.context.scene.render.image_settings.color_mode ='RGBA'
                                            bpy.context.scene.render.filepath = parent_dir_Up+str(num)
                                            bpy.ops.render.render(use_viewport = True,write_still=True)
                                            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                                        
                                if ang == 270:
                                    
                                    bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0.385543)
                                    if True:
                                        
                                        for fr in range(bpy.context.scene.frame_start,(bpy.context.scene.frame_end+1)):

                                            num = fr
                                            bpy.context.scene.frame_set(num)
                                            bpy.context.scene.render.alpha_mode = 'TRANSPARENT'
                                            bpy.context.scene.render.image_settings.color_mode ='RGBA'
                                            bpy.context.scene.render.filepath = parent_dir2_Left+str(num)
                                            bpy.ops.render.render(use_viewport = True,write_still=True)
                                            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                                        
                    if bpy.context.scene.QueryProps.Direcoes  == "3" :
    
                        pass

        self.Criar()

                        
    def Criar(self):
        
        self.Caminho = "C:\SpriterSheet\\Frames"
        Down = []
        Down2 = []
        Down_Left = []
        Down_Left2 = []
        Down_Right = []
        Down_Right2 = []
        Left = []
        Left2 = []
        Right = []
        Right2 = []             
        Up = []
        Up2 = []
        Up_Left = []
        Up_Left2 = []
        Up_Right = []
        Up_Right2 = []

        max_sprites_row = 12
        tile_width = 0
        tile_height = 0

        spritesheet_width = 0
        spritesheet_height = 0

        pasta_Down = os.listdir("C:\\SpriterSheet\\Frames\\Down")
        pasta_Down_Left = os.listdir("C:\\SpriterSheet\\Frames\\Down_Left")
        Pasta_Down_Right = os.listdir("C:\\SpriterSheet\\Frames\\Down_Right")  
        pasta_Left = os.listdir("C:\\SpriterSheet\\Frames\\Left")  
        Pasta_Right = os.listdir("C:\\SpriterSheet\\Frames\\Right")  
        Pasta_Up = os.listdir("C:\\SpriterSheet\\Frames\\Up")  
        Pasta_Up_Left = os.listdir("C:\\SpriterSheet\\Frames\\Up_Left")  
        Pasta_Up_Right = os.listdir("C:\\SpriterSheet\\Frames\\Up_Right")  

        pasta = os.listdir(self.Caminho)
        ############################################           
        for Image_png in pasta_Down:  

                           
            Image_png = Image_png.replace(".png","")
            Image_png = int(Image_png)
            Down2.append(Image_png)
            Down2.sort()
        ############################################
        for Image_png1 in pasta_Down_Left:  

                           
            Image_png1 = Image_png1.replace(".png","")
            Image_png1 = int(Image_png1)
            Down_Left2.append(Image_png1)
            Down_Left2.sort()        
        ############################################
        for Image_png2 in Pasta_Down_Right:  

                           
            Image_png2 = Image_png2.replace(".png","")
            Image_png2 = int(Image_png2)
            Down_Right2.append(Image_png2)
            Down_Right2.sort()           
        ##########################################    
        for Image_png3 in pasta_Left:  

                           
            Image_png3 = Image_png3.replace(".png","")
            Image_png3 = int(Image_png3)
            Left2.append(Image_png3)
            Left2.sort()           
        ##########################################  

        for Image_png4 in Pasta_Right:  

                           
            Image_png4 = Image_png4.replace(".png","")
            Image_png4 = int(Image_png4)
            Right2.append(Image_png4)
            Right2.sort()           
        ##########################################  

        for Image_png5 in Pasta_Up:  

                           
            Image_png5 = Image_png5.replace(".png","")
            Image_png5 = int(Image_png5)
            Up2.append(Image_png5)
            Up2.sort()           
        ##########################################  
        for Image_png6 in Pasta_Up_Left:  

                           
            Image_png6 = Image_png6.replace(".png","")
            Image_png6 = int(Image_png6)
            Up_Left2.append(Image_png6)
            Up_Left2.sort()           
        ##########################################
        for Image_png7 in Pasta_Up_Right:  

                           
            Image_png7 = Image_png7.replace(".png","")
            Image_png7 = int(Image_png7)
            Up_Right2.append(Image_png7)
            Up_Right2.sort()           
        ########################################## 
        for img1 in Down2 :
       
            img1 = str(img1)+".png"                   
            with Image.open(r"C:\SpriterSheet\Frames\Down"+"\\"+"0"+ img1) as im :
                Down.append(im.getdata())
        #########################################
        for img2 in Down_Left2 :
       
            img2 = str(img2)+".png"        
            with Image.open(r"C:\SpriterSheet\Frames\Down_Left"+"\\"+"0"+ img2) as im :
                Down_Left.append(im.getdata())
        #########################################
        for img3 in Down_Right2 :  

            img3 = str(img3)+".png"      
            with Image.open(r"C:\SpriterSheet\Frames\Down_Right"+"\\"+"0"+ img3) as im :
                Down_Right.append(im.getdata())
        #########################################
        for img4 in Left2 :  

            img4 = str(img4)+".png"         
            with Image.open(r"C:\SpriterSheet\Frames\Left"+"\\"+"0" + img4) as im :              
                Left.append(im.getdata())
        #########################################
        for img5 in Right2 :  

            img5 = str(img5)+".png"         
            with Image.open(r"C:\SpriterSheet\Frames\Right"+"\\"+"0"+ img5) as im :              
                Right.append(im.getdata())
        #########################################
        for img6 in Up2 :  

            img6 = str(img6)+".png" 
            with Image.open(r"C:\SpriterSheet\Frames\Up"+"\\"+"0"+ img6) as im :              
                Up.append(im.getdata())
        #########################################
        for img7 in Up_Left2 :  

            img7 = str(img7)+".png" 
            with Image.open(r"C:\SpriterSheet\Frames\Up_Left"+"\\"+"0"+ img7) as im :              
                Up_Left.append(im.getdata())
        #################################################        
        for img8 in Up_Right2 :  

            img8 = str(img8)+".png"
            with Image.open(r"C:\SpriterSheet\Frames\Up_Right"+"\\"+"0"+ img8) as im :              
                Up_Right.append(im.getdata())                    
               
      
              
        tile_widthD = Down[0].size[0]
        tile_heightD = Down[0].size[1]

        tile_widthD_F = Down_Left[0].size[0]
        tile_heightD_F = Down_Left[0].size[1]

        tile_widthD_R = Down_Right[0].size[0]
        tile_heightD_R = Down_Right[0].size[1]

        tile_widthL = Left[0].size[0]
        tile_heightL = Left[0].size[1]

        tile_widthR = Right[0].size[0]
        tile_heightR = Right[0].size[1]

        tile_widthU = Up[0].size[0]
        tile_heightU = Up[0].size[1]

        tile_widthUL = Up_Left[0].size[0]
        tile_heightUL = Up_Left[0].size[1]

        tile_widthUR = Up_Right[0].size[0]
        tile_heightUR = Up_Right[0].size[1]
        
        if len(Down) > max_sprites_row :
            
            spritesheet_width = tile_widthD * max_sprites_row
            required_rows = math.ceil(len(Down)/max_sprites_row)
            spritesheet_height = tile_heightD * required_rows
            
        else:
            
            spritesheet_width = tile_widthD*len(Down)
            spritesheet_height = tile_heightD
            
        spritesheetDown = Image.new("RGBA",(int(spritesheet_width), int(spritesheet_height)))
        
        for current_frame in Down :
            top = tile_heightD * math.floor((Down.index(current_frame))/max_sprites_row)
            left = tile_widthD * (Down.index(current_frame) % max_sprites_row)
            bottom = top + tile_heightD
            right = left + tile_widthD
            
            box = (left,top,right,bottom)
            box = [int(i) for i in box]
            cut_frame = current_frame.crop((0,0,tile_widthD,tile_heightD))
        
            spritesheetDown.paste(cut_frame, box)
        
        spritesheetDown.save(self.Caminho+"\\"+"SpriteSheetDown" + ".png", "PNG")
        ##################################################################################

        if len(Down_Left) > max_sprites_row :
            
            spritesheet_width1 = tile_widthD_F * max_sprites_row
            required_rows1 = math.ceil(len(Down_Left)/max_sprites_row)
            spritesheet_height1 = tile_heightD_F * required_rows1
            
        else:
            
            spritesheet_width1 = tile_widthD_F*len(Down_Left)
            spritesheet_height1 = tile_heightD_F
            
        spritesheetDownLeft = Image.new("RGBA",(int(spritesheet_width1), int(spritesheet_height1)))
        
        for current_frame1 in Down_Left :
            top1 = tile_heightD_F * math.floor((Down_Left.index(current_frame1))/max_sprites_row)
            left1 = tile_widthD_F * (Down_Left.index(current_frame1) % max_sprites_row)
            bottom1 = top1 + tile_heightD_F
            right1 = left1 + tile_widthD_F
            
            box1 = (left1,top1,right1,bottom1)
            box1 = [int(i) for i in box1]
            cut_frame1 = current_frame1.crop((0,0,tile_widthD_F,tile_heightD_F))
        
            spritesheetDownLeft.paste(cut_frame1, box1)      
                                              
        spritesheetDownLeft.save(self.Caminho+"\\"+"spritesheetDownLeft" + ".png", "PNG")
        ##################################################################################

        if len(Down_Right) > max_sprites_row :
            
            spritesheet_width2 = tile_widthD_R * max_sprites_row
            required_rows2 = math.ceil(len(Down_Right)/max_sprites_row)
            spritesheet_height2 = tile_heightD_R * required_rows2
            
        else:
            
            spritesheet_width2 = tile_widthD_R*len(Down_Right)
            spritesheet_height2 = tile_heightD_R
            
        spritesheetDownRight = Image.new("RGBA",(int(spritesheet_width2), int(spritesheet_height2)))
        
        for current_frame2 in Down_Right :
            top2 = tile_heightD_R * math.floor((Down_Right.index(current_frame2))/max_sprites_row)
            left2 = tile_widthD_R * (Down_Right.index(current_frame2) % max_sprites_row)
            bottom2 = top2 + tile_heightD_R
            right2 = left2 + tile_widthD_R
            
            box2 = (left2,top2,right2,bottom2)
            box2 = [int(i) for i in box2]
            cut_frame2 = current_frame2.crop((0,0,tile_widthD_R,tile_heightD_R))
        
            spritesheetDownRight.paste(cut_frame2, box2)

        spritesheetDownRight.save(self.Caminho+"\\"+"spritesheetDownRight" + ".png", "PNG")      
        ##################################################################################

        if len(Left) > max_sprites_row :
            
            spritesheet_width3 = tile_widthL * max_sprites_row
            required_rows3 = math.ceil(len(Left)/max_sprites_row)
            spritesheet_height3 = tile_heightL * required_rows3
            
        else:
            
            spritesheet_width3 = tile_widthL*len(Left)
            spritesheet_height3 = tile_heightL
            
        spritesheetLeft = Image.new("RGBA",(int(spritesheet_width3), int(spritesheet_height3)))
        
        for current_frame3 in Left :
            top3 = tile_heightL * math.floor((Left.index(current_frame3))/max_sprites_row)
            left3 = tile_widthL * (Left.index(current_frame3) % max_sprites_row)
            bottom3 = top3 + tile_heightL
            right3 = left3 + tile_widthL
            
            box3 = (left3,top3,right3,bottom3)
            box3 = [int(i) for i in box3]
            cut_frame3 = current_frame3.crop((0,0,tile_widthL,tile_heightL))
        
            spritesheetLeft.paste(cut_frame3, box3)      

        spritesheetLeft.save(self.Caminho+"\\"+"spritesheetLeft" + ".png", "PNG")
        ##################################################################################

        if len(Right) > max_sprites_row :
            
            spritesheet_width4 = tile_widthR * max_sprites_row
            required_rows4 = math.ceil(len(Right)/max_sprites_row)
            spritesheet_height4 = tile_heightR * required_rows4
            
        else:
            
            spritesheet_width4 = tile_widthR*len(Right)
            spritesheet_height4 = tile_heightR
            
        spritesheetRight = Image.new("RGBA",(int(spritesheet_width4), int(spritesheet_height4)))
        
        for current_frame4 in Right :
            top4 = tile_heightR * math.floor((Right.index(current_frame4))/max_sprites_row)
            left4 = tile_widthR * (Right.index(current_frame4) % max_sprites_row)
            bottom4 = top4 + tile_heightR
            right4 = left4 + tile_widthR
            
            box4 = (left4,top4,right4,bottom4)
            box4 = [int(i) for i in box4]
            cut_frame4 = current_frame4.crop((0,0,tile_widthR,tile_heightR))
        
            spritesheetRight.paste(cut_frame4, box4)

        spritesheetRight.save(self.Caminho+"\\"+"spritesheetRight" + ".png", "PNG")
        ##################################################################################

        if len(Up) > max_sprites_row :
            
            spritesheet_width5 = tile_widthU * max_sprites_row
            required_rows5 = math.ceil(len(Up)/max_sprites_row)
            spritesheet_height5 = tile_heightU * required_rows5
            
        else:
            
            spritesheet_width5 = tile_widthU*len(Up)
            spritesheet_height5 = tile_heightU
            
        spritesheetUp = Image.new("RGBA",(int(spritesheet_width5), int(spritesheet_height5)))
        
        for current_frame5 in Up :
            top5 = tile_heightU * math.floor((Up.index(current_frame5))/max_sprites_row)
            left5 = tile_widthU * (Up.index(current_frame5) % max_sprites_row)
            bottom5 = top5 + tile_heightU
            right5 = left5 + tile_widthU
            
            box5 = (left5,top5,right5,bottom5)
            box5 = [int(i) for i in box5]
            cut_frame5 = current_frame5.crop((0,0,tile_widthU,tile_heightU))
        
            spritesheetUp.paste(cut_frame5, box5) 

        spritesheetUp.save(self.Caminho+"\\"+"spritesheetUp" + ".png", "PNG")       
        ##################################################################################

        if len(Up_Left) > max_sprites_row :
            
            spritesheet_width6 = tile_widthUL * max_sprites_row
            required_rows6 = math.ceil(len(Up_Left)/max_sprites_row)
            spritesheet_height6 = tile_heightUL * required_rows6
            
        else:
            
            spritesheet_width6 = tile_widthUL*len(Up_Left)
            spritesheet_height6 = tile_heightUL
            
        spritesheetUp_Left = Image.new("RGBA",(int(spritesheet_width6), int(spritesheet_height6)))
        
        for current_frame6 in Up_Left :
            top6 = tile_heightUL * math.floor((Up_Left.index(current_frame6))/max_sprites_row)
            left6 = tile_widthUL * (Up_Left.index(current_frame6) % max_sprites_row)
            bottom6 = top6 + tile_heightUL
            right6 = left6 + tile_widthUL
            
            box6 = (left6,top6,right6,bottom6)
            box6 = [int(i) for i in box6]
            cut_frame6 = current_frame6.crop((0,0,tile_widthUL,tile_heightUL))
        
            spritesheetUp_Left.paste(cut_frame6, box6)     

        spritesheetUp_Left.save(self.Caminho+"\\"+"spritesheetUp_Left" + ".png", "PNG")
         ##################################################################################

        if len(Up_Right) > max_sprites_row :
            
            spritesheet_width7 = tile_widthUR * max_sprites_row
            required_rows7 = math.ceil(len(Up_Right)/max_sprites_row)
            spritesheet_height7 = tile_heightUR * required_rows7
            
        else:
            
            spritesheet_width7 = tile_widthUR*len(Up_Right)
            spritesheet_height7 = tile_heightUR
            
        spritesheetUp_Right = Image.new("RGBA",(int(spritesheet_width7), int(spritesheet_height7)))
        
        for current_frame7 in Up_Right :
            top7 = tile_heightUR * math.floor((Up_Right.index(current_frame7))/max_sprites_row)
            left7 = tile_widthUR * (Up_Right.index(current_frame7) % max_sprites_row)
            bottom7 = top7 + tile_heightUR
            right7 = left7 + tile_widthUR
            
            box7 = (left7,top7,right7,bottom7)
            box7 = [int(i) for i in box7]
            cut_frame7 = current_frame7.crop((0,0,tile_widthUR,tile_heightUR))
        
            spritesheetUp_Right.paste(cut_frame7, box7)
       ###########################################################################
        spritesheetUp_Right.save(self.Caminho+"\\"+"spritesheetUp_Right" + ".png", "PNG")

        self.MesclaFolhasdeSpriteSheet()

    def MesclaFolhasdeSpriteSheet(self):

        arquivo = []
        arquivo2 = []
        max_sprites_row = 1
        tile_width = 0
        tile_height = 0

        spritesheet_width = 0
        spritesheet_height = 0

        pasta = os.listdir("C:\\SpriterSheet\\Frames")
        ############################################           
        for imge in pasta:                            
            
            if ".png" in imge:
                arquivo2.append(imge)

        for img in arquivo2 :  

            img = str(img)
            with Image.open(r"C:\SpriterSheet\Frames/"+ img) as im :              
                arquivo.append(im.getdata())                    
             
              
        tile_width = arquivo[0].size[0]
        tile_height = arquivo[0].size[1]

        if len(arquivo) > max_sprites_row :
            
            spritesheet_width = tile_width * max_sprites_row
            required_rows = math.ceil(len(arquivo)/max_sprites_row)
            spritesheet_height = tile_height * required_rows
            
        else:
            
            spritesheet_width = tile_width*len(arquivo)
            spritesheet_height = tile_height
            
        spritesheet = Image.new("RGBA",(int(spritesheet_width), int(spritesheet_height)))
        
        for current_frame in arquivo :
            top = tile_height * math.floor((arquivo.index(current_frame))/max_sprites_row)
            left = tile_width * (arquivo.index(current_frame) % max_sprites_row)
            bottom = top + tile_height
            right = left + tile_width
            
            box = (left,top,right,bottom)
            box = [int(i) for i in box]
            cut_frame = current_frame.crop((0,0,tile_width,tile_height))
        
            spritesheet.paste(cut_frame, box)
        
        spritesheet.save("C:\SpriterSheet"+"\\"+"SpriteSheet" + ".png", "PNG")

        return {'FINISHED'}

class PanelThree(bpy.types.Panel):
    #cria e modela o painel o Painel essa classe é bem intuitiva
    bl_idname = "VIEW3D_PT_"
    bl_label = "Gerador Sprite"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    def draw(self, context):
        props = bpy.context.scene.QueryProps
        layout = self.layout
        obj = context.object
        col = layout.column(align=True)
        
        row = col.row()
        row.label(text="Config Imagem:", icon='WORLD_DATA')
        
        rowsub0 = col.row(align=True)
        rowsub0.label(text="Target :")
        rowsub0.prop(props, "Target_", text="")
        
        rowsub01 = col.row(align=True)
        rowsub01.label(text="Path:")
        rowsub01.prop(props, "CaminhoPaht", text="")
                        
        rowsub2 = col.row(align=True)
        rowsub2.label(text="Pasta :")
        rowsub2.prop(props, "Pasta", text="")
        
        rowsub1 = col.row(align=True)
        rowsub1.label(text="Deixe 00 :")
        rowsub1.prop(props, "Sprite_Name", text="")
        
        rowsub3 = col.row(align=True)
        rowsub3.label(text="Largura :")
        rowsub3.label(text="Altura :")
        
        
        rowsub4 = col.row(align=True)
        rowsub4.prop(props, "size_X", text="")
        rowsub4.prop(props, "size_Y", text="")

        rowsub5 = col.row(align=True)
        rowsub5.label(text="Camera Normal :")
        rowsub5.prop(props, "normal_Cam", text="")
        rowsub5.label(text="Camera Isometrica :")
       
        rowsub5.prop(props, "IsoMetric_Cam", text="")
        
        rowsub6 = col.row(align=True)
        rowsub6.label(text="Camera Nada :")
        
        rowsub6.prop(props,"Camera_Nada", text="")
        
        rowsub8 = col.row(align=True)
        rowsub8.label(text="Escolher Direções:", icon='FILE_REFRESH') 
        
        rowsub9 = col.row(align=True)
        rowsub9.label(text="Direções dos Sprites:")
        
       
        rowsub9 = col.row(align=True)
        rowsub9.prop(props, "Direcoes", text="")
        
        
        rowsub9 = col.row(align=True)
        rowsub9.label(text="Frames:", icon='OUTLINER_OB_ARMATURE') 
        
        rowsub9_1 = col.row(align=True)
        rowsub9_1.prop(props, "Frames1_", text="")
        rowsub9_1.prop(props, "Frames2_", text="")
        rowsub9_1 = col.row(align=True)
        
        rowsub10 = col.row(align=True)
        rowsub10.label(text="Executar Render:", icon='RENDER_STILL') 
        
        rowsub11 = col.row(align=True)
        rowsub11.operator(Render_Sprites.bl_idname,text="Executar Render:", icon='RESTRICT_RENDER_OFF') 
        
     

classes = (
    QueryProps,
    Render_Sprites,
    PanelThree
    
)

def register():

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    # Register QueryProps
    bpy.types.Scene.QueryProps = bpy.props.PointerProperty(type=QueryProps)
def unregister():

    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
    # $ delete QueryProps on unregister
    del(bpy.types.Scene.QueryProps)
if __name__ == "__main__":
    register()
  
    


