# copter_control_ifs 多旋翼无人机控制接口

copter control interface with dji or mavlink devicce like px4/ardupilot
适应大疆（未开发）和mavlink设备

# Introduction 介绍

基于C++的多旋翼无人机控制程序。可用于SLAM、路径跟踪或者其他算法的开发和验证。
A C++ based copter control interface to simplify the repeated work in copter control . One should be easily use this to devolop slam,trajectory planning ,or other state-of-art things.Currently Only mavlink interface has been developed.


# FlightTaskManager 飞行任务管理器

采用虚函数进行开发，方便拓展
Flight tasks manager is develop to virtual funtion ,so it is easy to extend other motion group by using the api.More work will be done.

# RouteTracker 路径跟踪器

纯跟踪算法
RouteTracker is based on pure pursuit.

# Visualization 视觉可视化

简化了可视化操作，方便可视化路径规划结果以及传感器信息。
Visualization in rviz has been wrapped into some simple steps by template class.So it will be more convenient to show your hard work.
More visualiztion wrapper of rviz  is under working . Also ,the purpose of this is to simplify work not to heavy study content.

