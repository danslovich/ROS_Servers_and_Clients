#! /usr/bin/env python
# imports required
import rospkg 
import rospy 
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

########## Node/Client init and Service connection ##########
rospy.init_node('service_move_bb8_in_square_custom_client') 
#rospy.wait_for_service('/move_bb8_in_square_custom')
move_bb8_in_square_service_client = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)
# Instance of msg request created
move_bb8_in_square_request_object = BB8CustomServiceMessageRequest()

# Assign message params for small squares
move_bb8_in_square_request_object.side = 0.2 
move_bb8_in_square_request_object.repetitions = 2 

# User Feedback
rospy.loginfo("Creating two small squares...")
# Send trajectory to the service
result = move_bb8_in_square_service_client(move_bb8_in_square_request_object)
rospy.loginfo(str(result))

# Assign message params for big square
move_bb8_in_square_request_object.side = 0.4 
move_bb8_in_square_request_object.repetitions = 1 

# User Feedback
rospy.loginfo("Creating one big square...")
# Send trajectory to the service
result = move_bb8_in_square_service_client(move_bb8_in_square_request_object)
rospy.loginfo(str(result)) #Print the result 

rospy.loginfo("End of service call")