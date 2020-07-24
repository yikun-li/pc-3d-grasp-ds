import glob
import os

import matplotlib.pyplot as plt
import numpy as np


def view_point_cloud_model_and_affordance(number_of_object_per_category=5):
    """
    View model and grasp affordance

    :return:
    """
    list_pc_paths = [f for f in glob.glob('./dataset/*.npy', recursive=True)]
    set_objects = set([os.path.basename(pc_path).split('_')[0] for pc_path in list_pc_paths])

    for obj in set_objects:
        try:
            # load point cloud models
            pc_models = np.load('./dataset/{}_point_cloud_models.npy'.format(obj))[
                        :number_of_object_per_category]
            # load point cloud grasp affordance
            pc_affordance = np.load('./dataset/{}_point_cloud_grasp_affordance.npy'.format(obj))[
                            :number_of_object_per_category]

            # visualization
            for i, m in enumerate(pc_models):
                fig = plt.figure()
                ax = fig.add_subplot(projection='3d')
                list_model_x, list_model_y, list_model_z = [], [], []
                list_affordance_x, list_affordance_y, list_affordance_z = [], [], []

                for x in range(32):
                    for y in range(32):
                        for z in range(32):
                            if pc_affordance[i, x, y, z] == 1:
                                list_affordance_x.append(x)
                                list_affordance_y.append(y)
                                list_affordance_z.append(z)
                            elif m[x, y, z] == 1:
                                list_model_x.append(x)
                                list_model_y.append(y)
                                list_model_z.append(z)

                ax.scatter(list_model_x, list_model_y, list_model_z, c='#0c457d')
                ax.scatter(list_affordance_x, list_affordance_y, list_affordance_z, c='#e8702a', alpha=0.35)
                ax.set_xlim(0, 32)
                ax.set_ylim(0, 32)
                ax.set_zlim(0, 32)
                plt.show()

        except FileNotFoundError:
            print('Some point cloud npy files are not found.')
            continue


if __name__ == '__main__':
    view_point_cloud_model_and_affordance(number_of_object_per_category=5)
