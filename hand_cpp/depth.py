import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import Image


startnum=10
endnum=15
filenum=startnum
while (filenum<=endnum):
    fig = plt.figure()

    data=np.loadtxt("/media/data_cifs/lu/Synthetic/Depth/depth_" + str(filenum)+".txt",delimiter=",")
    row=data[0]
    col=data[1]
    image=data[2:2+int(row)*int(col)]
    image=np.reshape(image,(int(row),int(col)))

    ax=fig.add_subplot(121)
    ax.imshow(image)
    originrow=data[2+int(row)*int(col)]
    origincol=data[3+int(row)*int(col)]
    topleftx=data[4+int(row)*int(col)]
    toplefty = data[5 + int(row) * int(col)]

    bone=np.loadtxt("/media/data_cifs/lu/Synthetic/Joints/bone_" + str(filenum) + ".txt",delimiter=",")
    bone=bone[:len(bone)-1]
    num_bone=len(bone)/6
    bone=np.reshape(bone,(int(num_bone),int(6)))
    #ax.scatter(bone[:, 0]-topleftx, bone[:, 1]-toplefty,c='r')


    camera=np.loadtxt("/media/data_cifs/lu/Synthetic/Camera/camera_" + str(filenum) + ".txt",delimiter=",")
    camera=camera[:len(camera)-1]
    view_M=camera[:16]
    proj_M=camera[16:]
    view_M=np.reshape(view_M,(4,4))
    proj_M=np.reshape(proj_M,(4,4))
    bone_trans=np.zeros((num_bone,3))
    for i in range(num_bone):
        cur_bone=bone[i,:]
        cur_bone_2d=cur_bone[:3]
        cur_bone_pos=cur_bone[3:]
        cur_bone_pos=np.append(cur_bone_pos,1)
        cur_bone_pos=cur_bone_pos.transpose()
        world=np.dot(view_M, cur_bone_pos)
        bone_trans[i,2]=world[2]
        hcpos=np.dot(proj_M,world)
        hcpos[0]=hcpos[0]/hcpos[3]
        hcpos[1]=hcpos[1]/hcpos[3]
        bone_trans[i,0] = origincol/2 + origincol/2*hcpos[0]
        bone_trans[i,1] = originrow/2 -originrow/2*hcpos[1]

    ax.scatter(bone_trans[:, 0]-topleftx, bone_trans[:, 1]-toplefty,c='y')
    ax.scatter(bone_trans[26, 0] - topleftx, bone_trans[26, 1] - toplefty, c='r')

    seg=Image.open("/media/data_cifs/lu/Synthetic/Segment/seg_" + str(filenum) + ".jpg")

    bx=fig.add_subplot(122)
    bx.imshow(seg)
    plt.show()
    filenum=filenum+1


