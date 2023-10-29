<p align = "center">

<h1 align = "center">FacialScape: Insightful Image Analytics</h1>
<h2 align = "center">🐍 Python | 🤖 Image Classification | 🧠 Machine Learning | 🕵️‍♂️ Analysis </h2>
</p>


## **Introduction**
FacialScape delves into the rich domain of image analytics, with a spotlight on extracting profound insights from a facial image dataset. This venture encompasses the exploration of facial features and expressions, along with digging into demographic dimensions.


**Project name:** [FacialScape](https://github.com/InfinityHack3r/FacialScape/)

**Data Set:** [Kaggle](https://www.kaggle.com/datasets/jessicali9530/lfw-dataset)

**Language:** [Python](https://www.python.org/) 

**Libraries:** 
- [Django](https://www.djangoproject.com/) 

- [OpenCV](https://opencv.org/)

- [Deepface](https://github.com/serengil/deepface)

- [Plotly](https://plotly.com/)

<br>

## **Description**

**FacialScape** unveils the nuanced details encapsulated within facial imagery. Rooted in the passion to unravel and interpret the multitude of narratives each face portrays, this project stands as a testament to the power of facial analysis.

- **Understanding Facial Features:** FacialScape ventures into the realm of facial features, categorizing them to unveil patterns and insights that might otherwise remain obscured.

- **Expressions & Emotions:** Our visages are the canvases of emotions. Exploring beyond static features, this project delves into the dynamic expressions that paint our faces.

- **Demographics & Beyond:** Gender and ethnicity represent just the tip of the demographic iceberg. FacialScape aims to correlate facial features with broader demographic trends.

## 🚀 Features

- **Feature Recognition:** Detection and categorization of facial features.
- **Emotion Analysis:** Interpretation of facial expressions to grasp the emotions conveyed.
- **Demographic Insights:** Analytical correlations of facial features with demographics like gender and ethnicity.
- **Data Visualization:** Graphic elucidation of analysis outcomes through charts and other visualization aids for enhanced clarity.

## Purpose

This initiative serves as the Capstone project for the "Software Technology 1 (4483)" course at the University of Canberra. The prime goal is to enable students to meticulously analyze a chosen dataset and coherently articulate their findings. Leveraging analytical tools, students will distill and process the data, metamorphosing it into actionable insights. This venture evaluates not merely their technical acumen but also their aptitude to transmute raw data into invaluable information, epitomizing the practical application of the competencies honed throughout the course.

<br>

---
## 📈 **Development**

> **⚠️ Project state:**  🚩 Alpha

**Current Version:** 
- v0.1.0

 **Phase:**
 - 🚩 First Phase




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
    cd src/facialscape
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