#!/usr/bin/env python
# imports required
import rospy
from geometry_msgs.msg import Twist
import time

class Move_BB8():
    # Constructor for Move_BB8 class for cmd_vel publisher
    def __init__(self):
        self.bb8_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        #self.ctrl_c = False
        #rospy.on_shutdown(self.shutdownhook)
        self.rate = rospy.Rate(10) # 10hz
    
    # cmd_vel publisher function
    def publish_once_in_cmd_vel(self, cmd):
        while not rospy.is_shutdown():
            connections = self.bb8_vel_publisher.get_num_connections()
            # check for node connections and publish cmds
            if connections > 0:
                self.bb8_vel_publisher.publish(cmd)
                rospy.loginfo("Published to /cmd_vel")
                break
            else:
                self.rate.sleep()

    # Halt Robot function
    def stop_bb8(self):
        rospy.loginfo("Stop the Robot")
        cmd = Twist()
        cmd.linear.x = 0.0
        cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel(cmd)

    # Movement function used by move_square
    def move_x_time(self, moving_time, linear_speed=0.2, angular_speed=0.2, **kwargs):
        cmd = Twist()
        cmd.linear.x = linear_speed
        cmd.angular.z = angular_speed
        self.publish_once_in_cmd_vel(cmd)
        time.sleep(moving_time)
        self.stop_bb8()
        
    # Creates a square using move_x_time and side param
    def move_square(self, side):
        i = 0
        time_magnitude = side/0.2 
        
        while not rospy.is_shutdown() and i < 4:
            # Forwards
            self.move_x_time(moving_time=2.0*time_magnitude, linear_speed=0.2, angular_speed=0.0)
            # Stop
            self.move_x_time(moving_time=2.5, linear_speed=0.0, angular_speed=0.0)
            # Turn 
            self.move_x_time(moving_time=3.9, linear_speed=0.0, angular_speed=0.2)
            # Stop
            self.move_x_time(moving_time=2.5, linear_speed=0.0, angular_speed=0.0)
            i += 1