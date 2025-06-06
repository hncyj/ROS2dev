import os
import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    fishbot_navigation2_dir = get_package_share_directory("fishbot_navigation2")
    nav2_bringup_dir = get_package_share_directory("nav2_bringup")
    rviz_config_dir = os.path.join(
        nav2_bringup_dir, 'rviz', 'nav2_default_view.rviz'
    )
    
    use_sim_time = launch.substitutions.LaunchConfiguration(
        'use_sim_time', default=True
    )
    
    map_yaml_path = launch.substitutions.LaunchConfiguration(
        'map', default=os.path.join(fishbot_navigation2_dir, 'maps', 'room.yaml') 
    )
    
    nav2_param_path = launch.substitutions.LaunchConfiguration(
        'params_file', default=os.path.join(fishbot_navigation2_dir, 'config', 'nav2_params.yaml')
    )
    
    return launch.LaunchDescription(
        [
            launch.actions.DeclareLaunchArgument('use_sim_time', default_value=use_sim_time, description='Use simulation (Gazebo) clock if true.'),
            launch.actions.DeclareLaunchArgument('map', default_value=map_yaml_path, description='Full path to map file be load.'),
            launch.actions.DeclareLaunchArgument('params_file', default_value=nav2_param_path, description='Full path to params file be load.'),
            launch.actions.IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    [nav2_bringup_dir, '/launch', '/bringup_launch.py']
                ),
                launch_arguments={
                    'map': map_yaml_path,
                    'use_sim_time': use_sim_time,
                    'params_file': nav2_param_path
                }.items(),
            ),
            launch_ros.actions.Node(
                package='rviz2',
                executable='rviz2',
                name='rviz2',
                arguments=['-d', rviz_config_dir],
                parameters=[{'use_sim_time': use_sim_time}],
                output='screen'
            ),
        ]
    )
    
    