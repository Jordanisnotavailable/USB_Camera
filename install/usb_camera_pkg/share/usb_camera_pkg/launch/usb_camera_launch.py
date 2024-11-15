import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        # Declare launch arguments
        DeclareLaunchArgument('camera_id', default_value='0', description='Camera ID (USB port)'),
        DeclareLaunchArgument('frame_id', default_value='camera', description='Frame ID for the camera'),

        # Launch the usb_cam node
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_camera_node',
            output='screen',
            parameters=[{
                'camera_id': LaunchConfiguration('camera_id'),
                'frame_id': LaunchConfiguration('frame_id'),
                'image_width': 640,
                'image_height': 480,
                'pixel_format': 'YUYV',
                'io_method': 'mmap',
                'camera_info_url': '',
            }]
        ),
    ])

