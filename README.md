<h1>SpriteSheet</h1>

<h2>Cria Folhas de Sprites com o UPBGE/blender 2.79</h2>

<h3>Ajuda no processo de desenvolvimento de jogos 2d<h3>

<h4>O addon, cria SpriteSheets para jogos top-down ou isométricos(em todas as direções) , basta configurar a camera e decidir qual usar.</h4>

<h5>Antes de instalar o Addon:</h5>

<h6>Deve atualizar o pip do Blender/UPBGE e installar o pilow no blender</h6>

<p>Para isso você deverá estar conectado a internet,copie o código abaixo e cole no editor do blender e de run.</p>
<p>No sistema Linux, deve exisgir autorização do admin.</p>  



##Instala/Atualiza o pip no blender

import subprocess<br/>
import sys<br/>
import os<br/>
import bpy<br/>
 
python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')<br/>
target = os.path.join(sys.prefix, 'lib', 'site-packages')<br/>
 
subprocess.call([python_exe, '-m', 'ensurepip'])<br/>
subprocess.call([python_exe, '-m', 'pip', 'install', '--upgrade', 'pip'])<br/>

subprocess.call([python_exe, '-m', 'pip', 'install', '--upgrade', 'scipy', '-t', target])<br/>
 

##Instala o pillow 
import bpy<br/>
import subprocess<br/>
import ensurepip<br/>


ensurepip.bootstrap()<br/>
pybin = bpy.app.binary_path_python<br/>
subprocess.check_call([pybin, '-m', 'pip', 'install', 'Pillow'])<br/>
