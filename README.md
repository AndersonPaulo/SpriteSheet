# SpriteSheet

Cria Folhas de Sprites com o UPBGE/blender 2.79


Para que funcione deve atualizar o pip do Blender/UPBGE e installar o pilow no blender,para isso você deverá estar conectado a internet,copie o código abaixo e cole no editor do blender e de run.
No sistema Linux, deve exisgir autorização do admin.
    



#Instala/Atualiza o pip no blender

import subprocess<br/>
import sys<br/>
import os<br/>
 
python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')<br/>
target = os.path.join(sys.prefix, 'lib', 'site-packages')<br/>
 
subprocess.call([python_exe, '-m', 'ensurepip'])<br/>
subprocess.call([python_exe, '-m', 'pip', 'install', '--upgrade', 'pip'])<br/>

#example package to install (SciPy):<br/>
subprocess.call([python_exe, '-m', 'pip', 'install', '--upgrade', 'scipy', '-t', target])<br/>
 
print('DONE')<br/>

#Instala o pillow 

import subprocess<br/>
import ensurepip<br/>
import bpy<br/>

ensurepip.bootstrap()<br/>
pybin = bpy.app.binary_path_python<br/>
subprocess.check_call([pybin, '-m', 'pip', 'install', 'Pillow'])<br/>
