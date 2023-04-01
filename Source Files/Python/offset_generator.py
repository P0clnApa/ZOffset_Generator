#Script Startup

import pymeshlab
import subprocess

print('wait while process is done...')

ms = pymeshlab.MeshSet()

#load reference mesh

ms.load_new_mesh('C:\\Users\\Public\\Documents\\Script_Workspace\\RefMesh.obj')

#configs load phase

f_ir = open('C:\\Users\\Public\\Documents\\Script_Workspace\\offset_note_resolution.txt' ,  'r' )
Im_ir = f_ir.read()
f_ir.close()
       
f_id = open('C:\\Users\\Public\\Documents\\Script_Workspace\\offset_note_distance.txt' ,  'r' )
Im_id = f_id.read()
f_id.close()

n_ir = float(Im_ir)
n_id = float(Im_id)

#calculate

ms.generate_resampled_uniform_mesh(cellsize=pymeshlab.AbsoluteValue(n_ir), offset=pymeshlab.AbsoluteValue(n_id))

    
#mesh Export phase

ms.save_current_mesh('C:\\Users\\Public\\Documents\\Script_Workspace\\Offset_Mesh.obj')

subprocess.call('C:\\Users\\Public\\Documents\\Script_Workspace\\EndSequence.bat')