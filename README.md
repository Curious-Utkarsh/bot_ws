> **Maintained version:** this is the original workshop workspace (July 2025). The updated project, with Docker support and a demo video, lives at **[MechaMind-Labs/edge-avoiding-robot](https://github.com/MechaMind-Labs/edge-avoiding-robot)**. Workshop recording: [Build a Fully Autonomous Edge-Avoiding Robot from Scratch](https://youtu.be/luZq317FUrE) · Step-by-step handout: [edge-avoiding-robot-workshop-guide](https://github.com/MechaMind-Labs/edge-avoiding-robot-workshop-guide)

# 🤖 bot_ws – Simulated Edge-Avoidance Robot

This repository contains a ROS 2-based mobile robot simulation with an edge-avoidance behavior. The robot uses a simulated LIDAR sensor in Gazebo and responds to edges or drops detected in its environment.

---

## 📦 Prerequisites

* ✅ OS: Ubuntu 22.04
* ✅ ROS 2: Humble Hawksbill
* ✅ Gazebo and RViz (included in ROS 2 Desktop Full)
* ✅ Python 3.10+

---

## 🧰 Step-by-Step Installation

### 1️⃣ Install ROS 2 Humble

Follow the official ROS 2 installation instructions:

```bash
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html
```

### 2️⃣ Source ROS 2 and Add to `.bashrc`

```bash
source /opt/ros/humble/setup.bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

### 3️⃣ Set RMW Implementation (CycloneDDS)

```bash
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc
```

### 4️⃣ Source `.bashrc`

```bash
source ~/.bashrc
```

---

## 🧠 Workspace Setup

### 5️⃣ Install Git (if not already)

```bash
sudo apt install git
```

### 6️⃣ Clone This Repository

```bash
cd ~
git clone https://github.com/Curious-Utkarsh/bot_ws.git
cd ~/bot_ws
```

---

## ⚙️ Setup ROS Dependencies

### 7️⃣ Install `rosdep` and initialize

```bash
sudo apt install python3-rosdep
sudo rosdep init
rosdep update
```

### 8️⃣ Install Package Dependencies

```bash
rosdep install --from-paths src -y --ignore-src --skip-keys="ament_python"
```

---

## 🧱 Build the Workspace

```bash
cd ~/bot_ws
colcon build
```

### 9️⃣ Source the workspace

```bash
source install/setup.bash
echo "source ~/bot_ws/install/setup.bash" >> ~/.bashrc
```

---

## 🧩 (Optional) Shell Autocompletion

```bash
sudo apt install python3-colcon-argcomplete
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc

```

---

## 🚀 Run the Simulation

### 1️⃣ Terminal 1: Launch Gazebo with the robot

```bash
ros2 launch bot_bringup simulated_robot.launch.py
```

### 2️⃣ Terminal 2: Run the Edge Detection Node

```bash
ros2 run bot_script edge_detection
```

You should now see:

* Gazebo with the robot and a world environment
* The robot running an **edge avoidance** algorithm using LIDAR data

---

## 📁 Project Structure Overview

```
bot_ws/
├── src/
│   ├── bot_description/     # URDF and Gazebo assets
│   ├── bot_controller/      # Robot control nodes
│   ├── bot_bringup/         # Launch files
│   ├── bot_script/          # Edge detection and logic
```

---

## 🛠 Troubleshooting

* If you see LIDAR not detecting correctly, make sure LIDAR pose and scan angle are valid in `bot_description`.
* Always source the workspace in every terminal:

  ```bash
  source ~/bot_ws/install/setup.bash
  ```

---

## 🙌 Credits

This project is maintained by [Curious-Utkarsh](https://github.com/Curious-Utkarsh).
Inspired by real-world edge-avoidance scenarios in robotics.

---

Let me know if you want to add SLAM or wall-following next!
