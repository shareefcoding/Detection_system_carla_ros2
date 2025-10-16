from setuptools import setup, find_packages
from glob import glob
import os

package_name = 'cylinder3d'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    # Install non-Python assets (launch, config, rviz) into share/<pkg>/*
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/config', glob('config/*.yaml')),      # optional
        ('share/' + package_name + '/rviz',   glob('rviz/*.rviz')),        # optional
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shareef',
    maintainer_email='',
    description='ROS2 wrapper node for Cylinder3D inference',
    license='',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # maps `ros2 run cylinder3d cylinder3d_node` to your Python main()
            'cylinder3d_node = cylinder3d.cyl3d_node:main',
        ],
    },
)
