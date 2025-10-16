from setuptools import setup, find_packages
from glob import glob
package_name = 'detection_system'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/config', glob('config/*.yaml')),  # optional
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shareef',
    maintainer_email='',
    description='Fusion node and launch files',
    license='',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fusion_node = detection_system.fusion_node:main',
        ],
    },
)
