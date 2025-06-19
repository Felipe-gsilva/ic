import open3d as o3d
import numpy as np
from argparse import ArgumentParser


def main():
    cloud = o3d.io.read_point_cloud("data/output/original_pc.ply")
    rotation_matrix = cloud.get_rotation_matrix_from_xyz((0, 0, np.pi))
    cloud.rotate(rotation_matrix, center=(0, 0, 0))

    o3d.io.write_point_cloud("data/output/aligned_pc.ply", cloud)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument()
    main()
