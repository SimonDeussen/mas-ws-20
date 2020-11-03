# Notes for ROS Day One 191020

## Task 2: Explore the turtlesim demo

### 1. List all nodes currently running
  * /rosout
  * /sim
  * /teleop
  * /turtle1_tf2_broadcaster
  * /turtle2_tf2_broadcaster
  * /turtle_pointer
### 2. Which nodes publish to the /tf topic.
  * /turtle2_tf2_broadcaster (http://ThinkPad-L14-Gen-1:41095/)
  * /turtle1_tf2_broadcaster (http://ThinkPad-L14-Gen-1:33969/)
### 3. What message format is used by the /tf topic and give the format of that message
  `rosmsg` gives following info:
  ```
  geometry_msgs/TransformStamped[] transforms
  std_msgs/Header header
    uint32 seq
    time stamp
    string frame_id
  string child_frame_id
  geometry_msgs/Transform transform
    geometry_msgs/Vector3 translation
      float64 x
      float64 y
      float64 z
    geometry_msgs/Quaternion rotation
      float64 x
      float64 y
      float64 z
      float64 w
  ```
### 4. Which topic receives information from the keyboard 
  `rosnode info /teleop` gives following info:
  ```
  Publications: 
  * /rosout [rosgraph_msgs/Log]
  * /turtle1/cmd_vel [geometry_msgs/Twist]
  ```
  That means that rosout and turtle one get the infos.

### 5. Which turtle is controlled by the keyboard, turtle1 or turtle2? 
  `rostopic info /turtle1/cmd_vel` displays that teleop publishes here:
  ```
  Type: geometry_msgs/Twist

  Publishers: 
  * /teleop (http://ThinkPad-L14-Gen-1:43241/)

  Subscribers: 
  * /sim (http://ThinkPad-L14-Gen-1:43557/)
  ``` 
  Turtle2 does not have the teleop puplisher.
### 6. Bonus: Find the publishing rate of the /turtle2/pose topic
  * I checked with `rostopic hz` there is says `average rate: 62.499`

