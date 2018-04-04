##
Input: a sequence of street view imagesÂ (http://cs.iit.edu/~xchen/sample_drive.rar)
Output: a mask of the smear on the lens

##The source code is in the file 'smear_detection.py'
##Output images: 
	Average Image - 'AverageImg.jpg'
	Gaussian Filter Image - 'GaussianFilterImg.jpg'
	Adaptive Threshold Image - 'AdaptiveThresholdImg.jpg'
	Edge Detection Image - 'EdgeDetectionImg.jpg'
	Final output Image - 'FinalOutputImg.jpg'
	
##Steps to run the program:
1. Install python
2. Install following packages
	- opencv3
	- numpy
	- scipy
	- glob
3. To detect smear of lens used in cam_0 -> Run command 'python smear_detection.py <path to cam_0 folder>'
4. To detect smear of lens used in cam_1 -> Run command 'python smear_detection.py <path to cam_1 folder>'
5. To detect smear of lens used in cam_2 -> Run command 'python smear_detection.py <path to cam_2 folder>'
6. To detect smear of lens used in cam_3 -> Run command 'python smear_detection.py <path to cam_3 folder>'
7. To detect smear of lens used in cam_5 -> Run command 'python smear_detection.py <path to cam_5 folder>'  