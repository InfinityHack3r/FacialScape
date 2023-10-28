<p align = "center">

<h1 align = "center">FacialScape: Insightful Image Analytics</h1>
<h2 align = "center">🐍 Python | 🤖 Image Classification | 🧠 Machine Learning | 🕵️‍♂️ Analysis </h2>
</p>


## **Introduction**
This project delves into the intricate world of image analytics, focusing on extracting valuable insights from a dataset of facial images. From understanding facial features and expressions to demographics and hair patterns, FacialScape aims to uncover the stories these images tell. A unique challenge is the identification of doppelgängers within the dataset and analyzing their striking similarities. The culmination of this analysis will be showcased in an interactive web application, complete with dashboards that allow for new data uploads and real-time analysis.

**Project name:** [FacialScape](https://github.com/InfinityHack3r/FacialScape/)

**Data Set:** [Kaggle](https://www.kaggle.com/datasets/jessicali9530/lfw-dataset)

**Language:** [Python](https://www.python.org/) 

**Libraries:** 
- [Django](https://www.djangoproject.com/) 

- [OpenCV](https://opencv.org/)

- [Docker](https://www.docker.com/)

- [YOLOv8](https://docs.ultralytics.com/)

- [labelImg](https://github.com/HumanSignal/label-studio)

<br>

## **Description**

FacialScape illuminates the intricate details hidden within facial images. At its core, this project is driven by the desire to extract and interpret the myriad of stories that every face narrates.

**Understanding Facial Features:** FacialScape dives into these features, using the a custom trained detection system YOLOv8 (You Only Look Once) to understand and categorize them, revealing patterns and insights that might otherwise go unnoticed.

**Expressions & Emotions:** Beyond the static features, our faces are canvases of emotions. 

**Demographics & Beyond:** gender and ethnicity - these are just the surface-level demographics. FacialScape delves deeper, aiming to correlate facial features with broader demographic trends, possibly uncovering new insights about population subsets.

**Hair Patterns & Styles:** Hair, often a canvas of personal expression, is another focal point. From analyzing hair colors and styles to understanding patterns of hair loss or graying, FacialScape provides a comprehensive analysis.

**The Doppelgänger:** Among the most intriguing aspects is the quest to identify doppelgängers. By comparing facial features across the dataset, the project aims to find individuals with striking resemblances, a task that combines the challenges of feature recognition and large-scale data comparison.

**Interactive Web Application:** The insights derived are not just confined to research papers or static reports. FacialScape's findings will be dynamically showcased in an interactive web application. This platform will not only display the results but also offer users the ability to upload new data, facilitating real-time analysis and insights generation.

By weaving together these elements, FacialScape promises to be more than just another analytics project. It's a journey into the heart of human identity, as told through the faces we wear.

## 🚀 Features

**Feature Recognition:** Advanced algorithms to detect and categorize facial features.

**Emotion Analysis:** Real-time detection and interpretation of facial expressions to understand conveyed emotions.

**Demographic Insights:** Analysis to correlate facial features with demographics like gender and ethnicity.

**Hair Analytics:** Comprehensive examination of hair colors.

**Doppelgänger Detection:** Feature comparison across the dataset to identify individuals with striking resemblances.

**Interactive Dashboard:** A user-friendly web application showcasing dynamic results, with options for users to upload new data for instant analysis.

**Data Visualization:** Graphical representation of analysis results, using charts, heatmaps and other visualization tools for better clarity.

**User Profiles:** Option for users to create profiles to save their data.

## What is this for?

This project serves as the Capstone for the "Software Technology 1 (4483)" course at the University of Canberra. The primary objective is for students to deeply analyze a chosen dataset and coherently present their findings. By employing analytical tools they will extract and process the data, transforming it into actionable insights. This endeavor evaluates not just their technical expertise, but also their capacity to convert raw data into valuable information, exemplifying the practical application of the skills cultivated throughout the course.

<br>

---
## 📈 **Development**

> **⚠️ Project state:**  🚩 Alpha

**Current Version:** 
- v0.1.0

 **Phase:**
 - 🚩 First Phase



**Documentation:**
- [Todo List](./doc/todo.md): Check to see the current workings and future plans.
- [Change Log](./doc/changelog.md): Stay updated with the latest changes and improvements in the project.


<br>


## 📦 **Installation**

General installation steps are as follows:

1. Clone the repository
2. open terminal and navigate to the project folder
3. run 
    ```bash
    pip install -r requirements.txt
    ```
4. Change directory to the src folder
    ```bash
    cd src
    ```
6. Migrate the database
    ```bash
    python manage.py migrate
    ```
7. Run the server
    ```bash
    python manage.py runserver
    ```
8. Open the browser and go to the following url
    ```
    http://127.0.0.1:8000/
    ```
9. locate the test file to upload in the [testdata folder](./testData/)

10. Click on the `Choose file` button and select the testdata.zip file

11. Click on the `Upload` button to upload the file

> Note: If this is the first time running this project, it will need to download the models from the internet and install them do not worry this will be a one time process which will take some time to complete depending on your internet speed once this is complete it will begin to analyze the uploaded file and then you will be able to see the results.

12. Once the analysis is complete you will be able to see the results on the screen.

>Note: this may take a time to display depending on your system speed and the size of the uploaded file as all the images are reconfigured to webp format for faster loading and storage.