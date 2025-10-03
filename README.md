# IRS_2025_67
IRS Lab

After new docker update from compose pull
```bash
Go to explorer. Git clone repo in terminal. Go to search bar and open IRS_group_67 folder

```


To let me BUILD SPECIFIC package
```bash
colcon build --packages-select [PACKAGE_NAME]
```

To let me BUILD ALL packages
```bash
colcon build
```

To let me run ros2 
```bash
source /opt/ros/humble/local_setup.bash
```

To let me run my packages
```bash
source install/setup.bash
```

To open rqt_image_view
```bash
ros2 run rqt_image_view rqt_image_view
```
To open rqt tf tree
```bash
ros2 run rqt_tf_tree rqt_tf_tree 
```


To run executable through terminal use:
```bash
python3 ./FILE
```

To run rqt_graph use:
```bash
ros2 run rqt_graph rqt_graph --force-discover
```

To run navigation
```bash
ros2 launch hand_solo_virtual_nav nav_launch.py
```

