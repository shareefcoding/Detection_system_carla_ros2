import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/shareef/CARLA_PROJECT/Detection_system_carla_ros2/install/detection_system'
