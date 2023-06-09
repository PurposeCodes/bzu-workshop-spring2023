#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import math
import time
from std_srvs.srv import Empty


def move(speed, distance, is_forward):
        velocity_message = Twist()

        if (speed > 0.4):
            print('speed must be lower than 0.4')
            return

        if (is_forward):
            velocity_message.linear.x =abs(speed)
        else:
            velocity_message.linear.x =-abs(speed)
        
        distance_moved = 0.0
        loop_rate = rospy.Rate(10)
        cmd_vel_topic='/cmd_vel_mux/input/teleop'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        t0 = rospy.Time.now().to_sec()

        while True :
                rospy.loginfo("Turtlesim moves forwards")
                velocity_publisher.publish(velocity_message)

                loop_rate.sleep()
                t1 =  rospy.Time.now().to_sec()
                
                distance_moved = (t1-t0) * speed
                print(distance_moved)               
                if  not (distance_moved<distance):
                    rospy.loginfo("reached")
                    break
        
        velocity_message.linear.x =0
        velocity_publisher.publish(velocity_message)
    
def rotate (angular_speed_degree, relative_angle_degree, clockwise):
    

    velocity_message = Twist()
    velocity_message.linear.x=0
    velocity_message.linear.y=0
    velocity_message.linear.z=0
    velocity_message.angular.x=0
    velocity_message.angular.y=0
    velocity_message.angular.z=0

    angular_speed=math.radians(abs(angular_speed_degree))

    if (clockwise):
        velocity_message.angular.z =-abs(angular_speed)
    else:
        velocity_message.angular.z =abs(angular_speed)

    angle_moved = 0.0
    loop_rate = rospy.Rate(10)
    cmd_vel_topic='/cmd_vel_mux/input/teleop'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

    t0 = rospy.Time.now().to_sec()

    while True :
        rospy.loginfo("Turtlesim rotates")
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1-t0)*angular_speed_degree
        loop_rate.sleep()

        print ('current_angle_degree: ',current_angle_degree)
                       
        if  (current_angle_degree>relative_angle_degree):
            rospy.loginfo("reached")
            break

    velocity_message.angular.z =0
    velocity_publisher.publish(velocity_message)



if __name__ == '__main__':
    try:
        
        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        move (0.3, 0.5 , False)
        time.sleep(1.0)
        rotate (90, 90 , True)

    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")