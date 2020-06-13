#name of this grasp
string id

#pose of the end effector in pregrasp phase. RRT runs only for this approach
geometry_msgs/PoseStamped pre_grasp_pose

#pose of the end effector prior to closing fingers
geometry_msgs/PoseStamped grasp_pose

#pose of the end effector once fingers closed, where to go?
geometry_msgs/PoseStamped post_grasp_pose
