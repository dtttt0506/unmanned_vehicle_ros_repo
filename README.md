# 无人车目标检测与自主导航ROS仿真代码仓库

## 1. 项目简介

本项目旨在提供一个基于ROS (Robot Operating System) 的无人车仿真环境，实现无人车的目标检测和自主导航功能。通过Gazebo进行物理仿真，Rviz进行可视化，并使用Python编写ROS节点，实现各个模块的功能。

## 2. 仓库结构

```
unmanned_vehicle_ros_repo/
├── src/
│   ├── object_detection/             # 目标检测ROS包
│   │   ├── src/
│   │   │   └── object_detector.py    # 目标检测节点
│   │   ├── CMakeLists.txt
│   │   └── package.xml
│   ├── navigation/                 # 自主导航ROS包
│   │   ├── src/
│   │   │   └── path_planner.py       # 路径规划节点
│   │   ├── CMakeLists.txt
│   │   └── package.xml
│   └── robot_description/          # 机器人模型描述ROS包
│       ├── urdf/
│       │   └── unmanned_vehicle.xacro  # 无人车URDF/XACRO模型
│       ├── meshes/                 # 机器人模型网格文件 (可选)
│       ├── rviz/
│       │   └── unmanned_vehicle.rviz # Rviz配置文件
│       ├── CMakeLists.txt
│       └── package.xml
├── launch/
│   ├── object_detection.launch     # 目标检测启动文件
│   ├── navigation.launch           # 导航启动文件
│   └── display_unmanned_vehicle.launch # 机器人模型显示启动文件
└── README.md
```

## 3. 模块说明

### 3.1 `object_detection` 包

该ROS包负责无人车的目标检测功能。`object_detector.py` 节点订阅摄像头图像话题，模拟目标检测过程，并发布检测结果。

### 3.2 `navigation` 包

该ROS包负责无人车的自主导航功能。`path_planner.py` 节点订阅目标点话题，模拟生成一条简单的路径，并发布全局路径。

### 3.3 `robot_description` 包

该ROS包包含无人车的URDF/XACRO模型描述文件，用于在Gazebo中加载机器人模型并在Rviz中进行可视化。`unmanned_vehicle.xacro` 定义了无人车的基本结构、轮子和摄像头等。

## 4. 启动说明

1.  **设置ROS环境：** 确保您的Ubuntu 18.04系统已安装ROS Melodic，并正确配置了ROS环境变量。

2.  **创建ROS工作空间：**
    ```bash
    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws/src
    ```

3.  **克隆本项目到工作空间：**
    ```bash
    git clone <本项目仓库地址> # 假设本项目已上传至GitHub等仓库
    ```
    (注：由于本项目是本地生成，此处仅为示例，实际操作时请替换为实际的仓库地址)

4.  **编译工作空间：**
    ```bash
    cd ~/catkin_ws
    catkin_make
    source devel/setup.bash
    ```

5.  **运行仿真：**

    *   **启动机器人模型显示 (Rviz):**
        ```bash
        roslaunch unmanned_vehicle_ros_repo display_unmanned_vehicle.launch
        ```

    *   **启动目标检测节点:**
        ```bash
        roslaunch unmanned_vehicle_ros_repo object_detection.launch
        ```

    *   **启动导航节点:**
        ```bash
        roslaunch unmanned_vehicle_ros_repo navigation.launch
        ```

    *   **在Gazebo中启动无人车仿真 (需要您自行创建Gazebo世界文件和启动文件):**
        ```bash
        # 示例：roslaunch gazebo_ros empty_world.launch
        # 示例：roslaunch your_robot_gazebo spawn_unmanned_vehicle.launch
        ```

## 5. 代码示例

具体代码请参考 `src` 目录下的各个ROS包中的Python脚本和XACRO文件。



