## **Questions**

### **Facial Landmarks**
- **What is the distribution of various facial features (like nose size, eye separation, etc.) in the dataset?**
    - Develop an algorithm to recognize different facial features in the images.
    - Visualize the distribution of various facial features in the dataset.
        - **Recommended Diagram**: Histograms/Density plots for continuous data and Pie charts for categorical data.

#### **Feature Extraction**
- **Nose**
    - Visible nose
        - **Recommended Diagram**: Pie Chart
    - Nose position
        - **Recommended Diagram**: Heatmap
- **Eyes**
    - Visible eyes
        - Yes
        - No
        - **Recommended Diagram**: Pie Chart
    - Eye separation
        - Sliding scale Close to Far
        - **Recommended Diagram**: Histogram/Density Plot
    - Eye position
        - Pixel position
        - **Recommended Diagram**: Scatter Plot, HeatMap
- **Mouth**
    - Visible mouth
        - Yes
        - No
        - **Recommended Diagram**: Pie Chart
    - Mouth shape
        - Sliding scale Small to Large
        - **Recommended Diagram**: Histogram/Density Plot
    - Mouth position
        - Pixel position
        - **Recommended Diagram**: Scatter Plot
- **Hair**
    - Visible hair
        - **Recommended Diagram**: Pie Chart
    - Has hair
        - Yes
        - No
        - **Recommended Diagram**: Pie Chart
    - Hair color
        - Sliding scale Light to Dark
        - **Recommended Diagram**: Histogram/Density Plot
- **Ears**
    - Visible ears
        - Yes
        - No
        - **Recommended Diagram**: Pie Chart
    - Ear size
        - Sliding scale Small to Large
        - **Recommended Diagram**: Histogram/Density Plot
    - Ear position
        - Pixel position
        - **Recommended Diagram**: Scatter Plot
- **Eyebrows**
    - Visible eyebrows
        - Yes
        - No
        - **Recommended Diagram**: Pie Chart
    - Eyebrow position
        - Pixel position
        - **Recommended Diagram**: Scatter Plot
- **Cheeks**
    - Visible cheeks
        - Yes
        - No
        - **Recommended Diagram**: Pie Chart
    - Cheek position
        - Pixel position
        - **Recommended Diagram**: Scatter Plot
- **Facial Hair**
    - Visible facial hair
        - Yes
        - No
        - **Recommended Diagram**: Pie Chart
    - Facial hair color
        - Light
        - Dark
        - **Recommended Diagram**: Bar Chart
    - Facial hair style
        - mustache
        - beard
        - goatee
        - **Recommended Diagram**: Bar Chart
    - Wrinkle position
        - Pixel position
        - **Recommended Diagram**: Scatter Plot
- **Pain scale**
    - Sliding scale 0 to 10
        - **Recommended Diagram**: Histogram/Density Plot

### **Facial Expression Analysis**
- **Can we identify common facial expressions (smile, anger, etc.) in the dataset?**
    - Develop an algorithm to recognize different facial expressions in the images.
    - Visualize the distribution of various facial expressions in the dataset.
        - **Recommended Diagram**: Bar Chart

#### **Facial Expressions**
- Happy
- Anger
- Surprise
- Sadness
- Disgust
- Fear
- Contempt
- Neutral
- Lust
    - **Recommended Diagram for all**: Bar Chart

### **Demographics Analysis**
- **What is the distribution of different demographics (age, gender, etc.) in the dataset?**
    - Develop an algorithm to recognize different demographics in the images.
    - Visualize the distribution of various demographics in the dataset.
        - **Recommended Diagram**: Bar Chart for age groups and Pie Chart for gender and skin color.

#### **Demographics Features**
- **Age Groups**
    - Child
    - Teen
    - Young Adult
    - Adult
    - Middle Aged
    - Senior
        - **Recommended Diagram for all**: Bar Chart
- **Gender**
    - Male
    - Female
        - **Recommended Diagram**: Pie Chart
- **Skin Color**
    - White
    - Black
    - Brown
    - Yellow
    - Other
        - **Recommended Diagram**: Pie Chart

### **Hair Analysis**
- **Can we categorize the dataset based on different Colours?**
    - Develop an algorithm to recognize different styles of hair in the images.
    - Visualize the distribution of various hair styles in the dataset.
        - **Recommended Diagram**: Bar Chart

#### **Hair Features**
- **Hair Color**
    - Black
    - Brown
    - Blonde
    - Red
    - Grey
    - White
    - Other
        - **Recommended Diagram for all**: Bar Chart

### **Doppelgänger Detection**
- **Can we identify pairs of individuals in the dataset who are not the same person but look strikingly similar?**
    - Utilize facial recognition algorithms to find pairs of individuals who look very similar but are not the same person.
    - Showcase and visualize some of the doppelgänger pairs identified.
        - **Recommended Diagram**: Gallery View for showcasing pairs and Bar Chart for features similarity.

#### **Doppelgänger Features**
- **Doppelgänger**
    - Yes
    - No
        - **Recommended Diagram**: Pie Chart
- **Doppelgänger Confidence**
    - Sliding scale 0 to 100
        - **Recommended Diagram**: Histogram/Density Plot
- **What Features are similar**
    - Eyes
    - Nose
    - Mouth
    - Hair
    - Ears
    - Eyebrows
    - Cheeks
    - Facial Hair
    - Wrinkles
        - **Recommended Diagram for all**: Bar Chart
