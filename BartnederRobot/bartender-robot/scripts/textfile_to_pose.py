class PoseTextHelper:
    
    from geometry_msgs.msg import Pose, PoseStamped
    
    @staticmethod
    def parse_pose_string(pose_file):
        
        file1 = open("pre_grasp.txt","r") 
        valid_set = set(['x', 'y', 'z', 'w'])
        pose_list = []
        for t in file1.readlines():
            if t.split(':')[0].strip() in valid_set:
                val = float(t.split(':')[-1].split()[0])
    
                pose_list.append(val)
    
        return PoseTextHelper.list_to_pose(pose_list)
    
    @staticmethod
    def list_to_pose(pose_list):
        from geometry_msgs.msg import Pose
        pose_msg = Pose()
        
        if len(pose_list) == 7:
            pose_msg.position.x = pose_list[0]
            pose_msg.position.y = pose_list[1]
            pose_msg.position.z = pose_list[2]
            pose_msg.orientation.x = pose_list[3]
            pose_msg.orientation.y = pose_list[4]
            pose_msg.orientation.z = pose_list[5]
            pose_msg.orientation.w = pose_list[6]
  
        return pose_msg
    

if __name__ == '__main__':
   
   helper = PoseTextHelper()
   print(helper.parse_pose_string('pre_grasp.txt'))
