import struct
import numpy as np
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header

def pack_rgb_uint8_to_float(rgb_uint8):
    rgb_uint32 = (rgb_uint8[:,0].astype(np.uint32) << 16) | \
                 (rgb_uint8[:,1].astype(np.uint32) << 8)  | \
                  rgb_uint8[:,2].astype(np.uint32)
    return np.array([struct.unpack('f', struct.pack('I', c))[0] for c in rgb_uint32], dtype=np.float32)

def points_rgb_to_cloud(header: Header, xyz: np.ndarray, rgb: np.ndarray) -> PointCloud2:
    assert xyz.shape[0] == rgb.shape[0]
    N = xyz.shape[0]
    rgb_f = pack_rgb_uint8_to_float(rgb)

    pts = np.zeros(N, dtype=[('x', np.float32), ('y', np.float32), ('z', np.float32), ('rgb', np.float32)])
    pts['x'] = xyz[:,0]; pts['y'] = xyz[:,1]; pts['z'] = xyz[:,2]; pts['rgb'] = rgb_f

    fields = [
        PointField(name='x',   offset=0,  datatype=PointField.FLOAT32, count=1),
        PointField(name='y',   offset=4,  datatype=PointField.FLOAT32, count=1),
        PointField(name='z',   offset=8,  datatype=PointField.FLOAT32, count=1),
        PointField(name='rgb', offset=12, datatype=PointField.FLOAT32, count=1),
    ]
    return PointCloud2(
        header=header,
        height=1, width=N,
        is_dense=True, is_bigendian=False,
        fields=fields,
        point_step=16, row_step=16*N,
        data=pts.tobytes()
    )
