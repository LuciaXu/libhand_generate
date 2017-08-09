import numpy as np
import matplotlib.pyplot as plt
import matplotlib
data=np.loadtxt("../Gestures/Depth/depth_2.txt",delimiter=",")
#print data
print len(data)
row=data[0]
col=data[1]
image=data[2:2+int(row)*int(col)]
image=np.reshape(image,(int(row),int(col)))
fig=plt.figure()
ax=fig.add_subplot(111)
ax.imshow(image)
hc_d=data[2+int(row)*int(col)]
print ("distance:")
print hc_d

bone=np.loadtxt("../Gestures/Joints/bone_2.txt",delimiter=",")
bone=bone[:len(bone)-1]
#print bone
print len(bone)
num_bone=len(bone)/6
bone=np.reshape(bone,(int(num_bone),int(6)))
ax.scatter(bone[:, 0], bone[:, 1],c='r')


camera=np.loadtxt("../Gestures/Camera/camera_2.txt",delimiter=",")
camera=camera[:len(camera)-1]
view_M=camera[:16]
proj_M=camera[16:]
view_M=np.reshape(view_M,(4,4))
proj_M=np.reshape(proj_M,(4,4))
#print view_M
#print proj_M
bone_trans=np.zeros((num_bone,3))
for i in range(num_bone):
    cur_bone=bone[i,:]
    #print cur_bone
    cur_bone_2d=cur_bone[:3]
    cur_bone_pos=cur_bone[3:]
    cur_bone_pos=np.append(cur_bone_pos,1)
    cur_bone_pos=cur_bone_pos.transpose()
    #print cur_bone_pos
    #print cur_bone_2d
    world=np.dot(view_M, cur_bone_pos)
    #print world
    bone_trans[i,2]=world[2]
    hcpos=np.dot(proj_M,world)
    hcpos[0]=hcpos[0]/hcpos[3]
    hcpos[1]=hcpos[1]/hcpos[3]
    #print hcpos
    bone_trans[i,0] = col/2 + col/2*hcpos[0]
    bone_trans[i,1] = row/2 -row/2*hcpos[1]
    #print cur_bone_trans

ax.scatter(bone_trans[:, 0], bone_trans[:, 1],c='y')
plt.show()
