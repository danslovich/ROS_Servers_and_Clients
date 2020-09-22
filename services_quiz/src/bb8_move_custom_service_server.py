#! /usr/bin/env python
# imports required
import rospy 
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from move_bb8 import Move_BB8

########## Server callback function ##########
def callback(request):
    # User feedback to confirm service launch
    rospy.loginfo("\"move_bb8_in_square_custom\" service launched")
    # Creating a movement object of Move_BB8 class
    movebb8_object = Move_BB8()
    # Storing custom msg data for use
    num_squares = request.repetitions 
    new_side = request.side 

########## Loop to pub square movements ##########  
    for i in range (num_squares):
        # User feedback at start of movement 
        rospy.loginfo("Squares starting... Side ="+str(new_side) + " Repetition = "+str(i))
        # Calling move_square with desired params
        movebb8_object.move_square(side = new_side)

########## Service completion message response ##########     
    rospy.loginfo("The service \"move_bb8_in_square_custom\" has ended")
    response = BB8CustomServiceMessageResponse()
    # Set custom message bool to show successful completion
    response.success = True 
    return response
    
########## Node/Service init and user feedback ##########
rospy.init_node('service_move_bb8_in_square_server')
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, callback)
rospy.loginfo("The service \"move_bb8_in_square_custom\" is ready for call...")
rospy.spin()