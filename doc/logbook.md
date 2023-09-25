# Logbook

## 1. Planning/Design and Research
**Date: 21/09/2023**

Today, I initiated the planning and research phase of the project. My primary focus was on understanding the scope of the project and delineating the essential tasks that need to be undertaken.

I began by examining the dataset that has been provided looking at the images. During this initial analysis, I started to conceptualize the kind of data that would be most pertinent to utilize for the project questions.

Furthermore, I delved into exploring various data visualization techniques. I am in the process of identifying the most effective visualization methods to represent the data accurately and insightfully. This involves considering different types of diagrams and charts that would best illustrate the data patterns and trends.

As I move forward, I aim to finalize the selection of data and visualization techniques.

### Frameworks and Libraries

I have decided to use the following frameworks and libraries for the project:

- **Python**: I will be using Python as the primary programming language for the project.
- **OpenCV**: I will be using OpenCV for image processing and feature extraction.

Furthermore, I will be using the following frameworks and libraries for the web application:

- **Django**: I will be using Django to create the data visualization web application and interactive dashboards to upload new data for analysis.
- **Docker**: I will be using Docker to containerize the web application and interactive dashboards.

### Data Visualization Techniques

I have decided to use the following data visualization techniques for the project:

- **Histograms/Density plots**: To visualize the distribution of sizes and separations.
- **Heatmaps**: To visualize the common positions for different features.
- **Box plots/ Violin plots**: To visualize the distribution and variability of the data.
- **Bar Charts/Pie Charts**: To visualize the frequency of each facial expression in the dataset.
- **Gallery View**: To showcase and visualize some of the doppelgänger pairs identified.

## 2. Family Discussion on the Project
**Date: 23-24/09/2023**

Today, I had an insightful discussion with my family about my ongoing project. I delved into the project's idea, its broad scope and the data visualization techniques I intend to deploy. As always, my family's perspective brought forward some valuable feedback and intriguing suggestions.

### Feedback & Suggestions:

- **Height Measurement Idea**: They proposed an intriguing method to estimate a person's height from a photograph. By leveraging the size of a person's head (from chin to top) and considering variables like age and gender, one might be able to deduce body proportions. This concept is substantiated by resources on [body proportions](https://hpc.anatomy4sculptors.com/). While it's fascinating, I might not be incorporating this in the current project. However, I'm certainly interested in the concept for future exploration.

- **Face Proportions**: Another suggestion revolved around the measurement of face proportions. This is another area I'm keen to delve into in subsequent projects.

- **Pain Scale**: as my mother and brother are nurses by profession, they suggested the incorporation of a pain scale. This would involve analyzing facial expressions to determine the level of pain a person is experiencing. This is a fascinating concept, and I'm keen to explore it.

### Discussions with My Brother:

On the technical front, my brother and I discussed the possibility of him assisting me in creating a training set for the detection system. This would necessitate manually annotating the images in the dataset. considering the use of a custom detection model based on YOLOv8. By training this model on a specific portion of my dataset, I aim to enhance feature detection. Notably, this method might enable the identification of unique features not found in other pre-trained datasets. Nonetheless, there are challenges to consider. The training process for such a model requires significant time and resources. Given the project's timeline, I'm uncertain about achieving this without additional help, particularly in developing a robust training set for the detection system.

## 3. Training Data Selection
**Date: 25/09/2023**

Today, I commenced the data selection process for the project. My first task was to discern the data that resonates best with the project's objectives. Given that our total dataset comprises of [100 images spanning various scenarios], I meticulously examined it to cherry-pick the images that align most closely with the project.

To facilitate this, I devised a random [sampling tool](../tools/randomImages.py) that would earmark approximately 100 images from the dataset. These images will serve as the foundation for training, validating and testing the YOLOv8 model. Given the project's evolving nature, I'm keeping options open to expand this image set in the future.

The next phase involves annotation. I've zeroed in on [Roboflow](https://roboflow.com/) for this task. With Roboflow, I can adeptly annotate these images and more crucially, export these annotations in the YOLO-specific format. I will get my family into assisting me with this task. I'm confident that with their help, I can complete this process in a timely manner.

I'm currently weighing the pros and cons of training venues. While Google Colab emerged as an initial option, I'm wary of its limited resource time limits. I'm toying with the idea of harnessing the power of my local GPU (RTX 3090) for this task. For context, my machine is equipped with [448 GB RAM, Intel Xeon E5-2667 v3 @ 3.20 GHz (2 Processors)]. In the coming days, I'll be dissecting the cost-benefit analysis of training on Google Colab vis-à-vis my local machine and or buying a pro membership for google Colab to remove the time limits.

Should neither prove feasible, I'm considering using a pretrained model from hugging face this option would be a devestating blow to the project's scope and objectives. Nonetheless, I'm keeping this option open as a last resort.
