#!/usr/bin/env python

import rospkg
import os
import re
import subprocess

rospack = rospkg.RosPack()

if __name__ == '__main__':
    objects_dir = os.path.join(rospack.get_path('tmc_wrs_gazebo_worlds'), 'models')
    clouds_dir = os.path.join(rospack.get_path('image2kinect'), 'data')
    for object_dir in os.listdir(objects_dir):
        mesh_path = os.path.join(objects_dir, object_dir, 'meshes', 'nontextured.stl')
        name = re.sub(r'ycb_[0-9]*[_-]', '', object_dir)
        save_mesh_path = os.path.join(clouds_dir, name + '.obj')
        save_pcd_path = os.path.join(clouds_dir, name + '.pcd')
        if os.path.isfile(mesh_path):
            subprocess.run(['pcl_converter', mesh_path, save_mesh_path])
            subprocess.run(['pcl_mesh_sampling', save_mesh_path, save_pcd_path, '-write_normals', '-no_vis_result'])
