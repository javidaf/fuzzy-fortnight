# fuzzy-fortnight
## Project 2 TEK5020

Source code and results can be explored [here](tek5020-p2/tek5020_p2).

The project description can be found in the included PDF file: [Project description](Prosjektoppgave2.pdf).

## Project Description

### Introduction

The task involves image segmentation, i.e., dividing images into meaningful and/or perceptually uniform regions. Segmentation is often used in image analysis to simplify the image for further analysis, for example, to find physical objects of specific types in the scene. An example of segmentation is shown in Fig. 1.

Figure 1: Example of segmentation. The original image (left) is divided into regions corresponding to "street", "sidewalk", "buildings", "sky", etc. (right).

There are many ways to perform image segmentation. In this task, the idea is to do this by classifying each individual pixel in the image into one of the desired segment types (i.e., classes), based on color and intensity in the image. It is also possible to include properties that depend on neighboring pixels, e.g., calculating various measures of local texture, but this should not be done in this task.

### Problem description
Each pixel in a digital color image is associated with three intensity values in red, green, and blue (R, G, B). Each pixel can therefore be considered as a point in a three-dimensional feature space (the RGB space), so that the pixel is represented by the feature vector

$X = [R,G,B]^T$

where R, G, and B indicate the strength of each color component. In the attached image files, these values range from 0 to 255. A classifier should be trained to assign each feature vector of this type to one of the selected classes (segments).

Figure 2: Examples showing the segmentation process. In the original image on the left, selected regions for three classes are marked; sky, white buildings/fences, and ground, etc. The image on the right is the segmentation result, where the three classes are shown in blue, cyan, and yellow, respectively.

The first step in solving the task is to select a rectangular area of appropriate size (see Fig. 2) from each of the classes you want to divide the image into. The pixels in each area should be used as training samples for the respective class. You are free to choose the classifier type and training method. Feel free to use one of the classifier types (training methods) you implemented in project assignment 1 (e.g., the minimum error rate method) to generate a classifier for the selected classes, based on the three color components.

Then use the classifier to assign all pixels in both the training image and a similar test image to one of the classes (in the example in Fig. 2, the classifier is used to segment the training image), and convert the result back to a color-coded result image that shows the segmentation achieved. Comment on the result. Was the segmentation as desired? If not, what could be the reason?
Example images that can be used in the task are shown in Fig. 3 (attached to the task description). Image 1 can be divided into three segments by training the classifier on the pixels in three regions, as shown in the image (this marking is not included in the downloadable image), and then classifying all pixels in the image; this is to test that the software works. The other two images should be divided into three segments, "red ring binder", "blue ring binder" and "background". Feel free to use image 2 (3b) as the training image and image 3 (3c) as the test image.
To make the classifier more robust to variations in intensity (light/shadow, reflections, etc.), it may be a solution to normalize the RGB values, e.g., by the transformation

$X = [t_1 = R/(R+G+B),t_2= G/(R+G+B),t_3= B/(R+G+B)]^T$

and use two of these values (normalized tristimulus values), e.g., t1 and t2, as features.
Note that t3 is then unnecessary since it is determined by the other two, and will cause the minimum-error-rate classifier to fail because the determinant of the covariance matrices becomes zero.
Figure 3: Examples of images that can be used in the task. The image on the left can, for example, be used for both training and testing to try out the method, while the other two can be used for training and testing, respectively. 

Feel free to use your own images in the task; at least two images with similar content, where one is used for training and the rest for testing. The task can be carried out as a group work with 2-3 students in the group. A report (maximum of about 10 pages) should be submitted, describing what has been done, what has been achieved, and showing examples of results. Feel free to include printouts of code, but this is not a requirement.

### Summary
The process is as follows:
- Select a training image and find suitable regions for selecting training sets for the desired classes,
- Train a classifier for the problem, e.g., a minimum-error-rate classifier with normal distribution assumption,
- Use the classifier to segment the training image to see if it works as expected,
- Segment one or more test images,
- Provide a brief discussion of the results (what worked well/poorly and why?).

As mentioned, you are free to use images other than those provided, and any classifier type with an associated training method.
