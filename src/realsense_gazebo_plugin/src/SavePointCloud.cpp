/*
Used to save the point cloud data in an OBJ file 
Application: Would be used while training Dex-net 
Disclaimer: Not used for Comparison of the Grasping Algorithms
Reason for not using: Used Pre-trained model for the project
*/

#include <iostream> 
#include <stdio.h> 
#include <fstream>
#include <time.h>

#include <ros/ros.h>
#include <sensor_msgs/Image.h>

#include <cv_bridge/cv_bridge.h>
#include <opencv2/highgui/highgui.hpp>

// PCL specific includes
#include <pcl_ros/point_cloud.h>

using namespace cv;

void rgb_cb(const sensor_msgs::Image::ConstPtr& msg){

        cv_bridge::CvImageConstPtr cv_ptr;
        cv_ptr = cv_bridge::toCvShare(msg);
        cv::Mat image2;
	cvtColor( cv_ptr->image, image2, cv::COLOR_BGR2RGB );



        imshow("RGB Stream", image2);
        cv::imwrite("/home/rox/Scrivania/original/catkin_ws/src/img_cloud_point/Capture.jpg", image2);

        std::cout << "\nImmagine salvata " << std::endl;

}

int main (int argc, char** argv)
{
  // Initialize ROS
  ros::init (argc, argv, "Save_PointCloud");
  ros::NodeHandle nh;

  std::cout << "\nStarting the subscribers" << std::endl;

  // Create a ROS subscriber for the rgb & point cloud
  ros::Subscriber sub_rgb = nh.subscribe ("/r200/camera/color/image_raw", 1, rgb_cb);

  
  namedWindow("RGB Stream");
  ros::spin ();
  destroyWindow("RGB Stream");
  std::cout << "Code Terminated\n" << std::endl;

  return 0;
}

