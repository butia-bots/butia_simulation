#!/usr/bin/env python

import rospkg
import os
import re
import subprocess
import pyassimp

rospack = rospkg.RosPack()

if __name__ == '__main__':
    #objects_dir = os.path.join(rospack.get_path('tmc_wrs_gazebo_worlds'), 'models')
    objects_dir = "/home/butia-bots/butia_ws/ycb-tools/models/ycb"
    clouds_dir = os.path.join(rospack.get_path('image2kinect'), 'data')
    for object_dir in os.listdir(objects_dir):
        mesh_path = os.path.join(objects_dir, object_dir, 'poisson', 'nontextured.stl')
        ply_path = os.path.join(objects_dir, object_dir, 'clouds', 'merged_cloud.ply')
        name = object_dir[4:]
        save_mesh_path = os.path.join(clouds_dir, name, 'nontextured.stl')
        save_pcd_path = os.path.join(clouds_dir, name, 'merged_cloud.pcd')
        if os.path.isfile(mesh_path):
            os.mkdir(os.path.join(clouds_dir, name))
            #subprocess.run(['pcl_mesh_sampling', save_mesh_path, save_pcd_path, '-write_normals', '-write_colors', '-no_vis_result', '-leaf_size', '0.01'])
            subprocess.run(['cp', mesh_path, save_mesh_path])
            subprocess.run(['pcl_ply2pcd', ply_path, save_pcd_path])
            #subprocess.run(['pcl_normal_estimation', save_pcd_path, save_pcd_path, '-k', '5'])
            #pyassimp.export(scene, save_pcd_path, file_type='pcd')
