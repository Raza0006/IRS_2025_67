# IRS_2025_67
IRS Lab

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

To run executable through terminal use:
```bash
python3 ./FILE
```

To run rqt_graph use:
```bash
ros2 run rqt_graph rqt_graph --force-discover
```