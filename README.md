# WRO Future Engineers 2025 – Autonomous Robot

This repository contains the full work of our team for the WRO Future Engineers 2025 competition.  
We designed, built, and programmed an autonomous robot capable of navigating the field, detecting colored blocks, and returning to the start point.

## Repository Structure
- **/docs/** – Project documentation (PDF, flowchart, images).
- **/code/arduino/** – Arduino sketches for servo steering, navigation, HuskyLens integration.
- **/code/raspberrypi/** – ROS2 nodes and scripts for Slamtec A1 LiDAR (future upgrade).
- **/cad/** – 3D-printed chassis, servo mount, and wheel designs.
- **/tests/** – Logs and results of experiments (ultrasonics, gyro, HuskyLens).

## Features
- 3D-printed modular chassis.
- HC-SR04 ultrasonic sensors for centering and distance measurement.
- MPU6050 gyroscope for straight-line driving and accurate turns.
- Servo motor steering + DC motor propulsion.
- HuskyLens for block color and area detection.
- Planned upgrade: Slamtec A1 LiDAR with Raspberry Pi for SLAM and precision mapping.

## How to Run
1. Upload Arduino sketches from `/code/arduino/` to the board.
2. Connect sensors according to `docs/WiringDiagram.png`.
3. For LiDAR mode: run `ros2 launch code/raspberrypi/slam_mapping.launch`.

## Team Members
- Khalid Bashar – Mechanical design (CAD & 3D printing).
- Ahmed Osama – Electronics & Arduino programming.
- Amr Elzehairy – Testing, HuskyLens integration.

## 📖 Documentation
Full project report: [docs/WRO2025_Report.pdf](docs/WRO2025_Report.pdf)
