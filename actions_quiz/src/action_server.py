#! /usr/bin/env python
import rospy
import time
import actionlib
from actions_quiz.msg import CustomActionMsgFeedback, CustomActionMsgResult, CustomActionMsgAction
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class CustomActionMsgClass(object):
    # Message assignment
    feedback = CustomActionMsgFeedback()
    result   = CustomActionMsgResult()

    def __init__(self):
        # Constructor for action server
        self.action_server = actionlib.SimpleActionServer("action_custom_msg_as", CustomActionMsgAction, self.goal_callback, False)
        self.action_server.start()

    def goal_callback(self, goal):
        # Publishers Assignment
        self.takeoff_pub = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
        self.land_pub = rospy.Publisher('/drone/land', Empty, queue_size=1)    
        goal_word = goal.goal
        r = rospy.Rate(1)
        success = True

        for i in range(4):
            # Check for preempt and set if required
            if self.action_server.is_preempt_requested():
                rospy.loginfo('The goal has been preempted')
                self.action_server.set_preempted()
                success = False
                break
            # Check for TAKEOFF goal word
            if goal_word == 'TAKEOFF':
                self.takeoff_pub.publish(Empty())
                self.feedback.feedback = 'Taking Off...'
                rospy.loginfo('Taking Off...')
                self.action_server.publish_feedback(self.feedback)
            # Check for LAND goal word
            if goal_word == 'LAND':
                self.land_pub.publish(Empty())
                self.feedback.feedback = 'Landing...'
                rospy.loginfo('Landing...')
                self.action_server.publish_feedback(self.feedback)
            # Send feedback once per second
            r.sleep()
        # Returning Empty result
        if success == True:
            self.result = Empty()
            self.action_server.set_succeeded(self.result)

# Main for function calls
if __name__ == '__main__':
    rospy.init_node('action_custom_msg')
    CustomActionMsgClass()
    rospy.spin()
