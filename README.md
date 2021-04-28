# Cityhack2021

1.	Background of this project: 
With the deteriorating situation of COVID-19, we need to emphasize more on the role of social distancing and the importance of wearing masks upon public health. The government has published a lot of policies. However, it is still difficult to detect whether people always obey the policies in the public area. There will be a need of many stuff to observe violations, which is quite time consuming and tiring. Therefore, we have designed a system to detect social distance and mask wearing situation.

2.	Solution 
* a.	Absence makes the heart grow fonder. This is particularly correct and vital during the tough pandemic period. 
* b.	One of the potential solutions is that we shall detect whether people in crowd wear masks, and whether the distance is safe. The solution could be done with the power of AI. 
* c.  The desired effect of our product is to detect the people without masks, calculate the distance between people, and give an alarm once the people without masks are found to be beyond the safe distance from others. If two or more people are gathering, an alert will be sent to administrator.
* d.  Our product is expected to be deployed on 华为ATLAS DK200, which can be easily deployed in public space. It must include a camera, to capture the environment, and a microprocessor with proper software installed so that our algorithm can run on it.

3.	Implementation
* a.	Transfer Learning. Programming is not that easy, but TensorFlow can help. Our project adopted one popular technique in deep learning, so-called Transfer Learning. Standing on the shoulders of giants, we shall be advancing. That’s the Zen of it. Using existing models as out input, we fed it with more samples and did fine-tuning, which allows it to learn new features and greatly reduces the time of training.  
* b.	Convolutional Neuron Network. The video is imported as a sequence of images, to a convolutional neuron network for feature extraction. Then the high-level features are fed into a fully connect network for logistic regression. 
* c.	DISTANCE. The distance is from 
* d.	Warning. The system gives warning if two people are too close. This could definitely be helpful in detecting people in queues for some high-density areas.

6.	Further Application 
* a.	The product can be deployed in area with high-density population like shopping malls and subway stations. 
* b.	We can improve our product by optimizing the face mask detection model, which can be done by providing more training samples. After installing the first batch of products, with the help of the camera, we can collect a lot of photos of people with mask and videos with moving persons.  
