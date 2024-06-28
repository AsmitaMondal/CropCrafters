# CropCrafters 🪴
#### This project was done as a part of the final project submission for the web development course in the university data science postgraduate degree. 🌐

# About

This comprehensive website integrates predictive crop analytics, intelligent disease detection, and a dedicated inquiry system to empower farmers and elevate farming practices into the digital era.

# Vision and Impact:

CropCrafters envisions a future where technology seamlessly integrates with traditional farming wisdom. By providing accessible and user-friendly tools,
the platform aims to ensure food security, environmental sustainability, and economic prosperity for farming communities. CropCrafters stands as a beacon of transformation, redefining agriculture through innovation, community collaboration, and the convergence of traditional wisdom with modern technology.

# Features 💖
- Home Page
- About Us Section
- Information Page
- Recommendation System for Crops
- Prediction System for Plant Diseases
- Query Form for Question Inputs
- Testimonial Page for Dynamic Display of Reviews
- Contact Us Information

# Flow of Website Functionalities 🍀🍁

- **Recommendation System:** This system provided a form that took inputs of elements such as nitrogen, phosphorus, temperature, humidity etc. to recommend a crop based on the environmental conditions. The model achieved 94% accuracy. The [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) dataset from Kaggle was used to train the model.
- **Prediction System:** This feature provided a form to accept user input in the form of a jpg, jpeg, or png image and based on the features of the image classified it as diseased or healthy. The specific disease names were displayed. The model achieved 82% accuracy. It was trained on the [Major Plant Disease Detection](https://www.kaggle.com/datasets/dinodev/majorplantdiseasedetection) dataset from Kaggle.
- **Query Form:** The idea was to make solutions available to all people. This was a simple database implementation where another form took user inputs such as name, phone number, type of farming, location, and query box. This was followed by an option to choose between *answer via call* or *answer via sms*. This filled up form got saved in the MYSQL database which the admin could view. Based on user's choice of whether he wants his query to be answered through call, or sms, the necessary service could be provided.
- **Dynamic Testimonials:** This was another simple database implementation which accepted user reviews in the form of names, star rating and review in words. These inputs got stored in the database which were dynamically called to display on the webpage. In case, admin wanted to delete a review, the deletion could directly be perfomed in the database which would automatically reflect in the webpage and the review would no longer be displayed.

# Technologies Used 🖥️

## Front-End 
- HTML
- Vanilla CSS
- JavaScript

## Back-End
- Flask
- SQLAlchemy 

## Model Building
- Python

## Database
- MySQL phpMyAdmin

# Project Outline 📜
## 1: Planning 📝

### Phase 1: Defining The Mission 🥅

1. **Website Purpose:** Creating a website dedicated to farmers and farming has always been a passion of mine, spurred by the realization that this crucial field is often overlooked. Moreover, considering the potential for significant development in agriculture in the near future, I saw an opportunity to contribute to this space. This motivation led to the inception of my project, Crop Crafters, aimed at providing valuable services to farmers. 
2. **Target Audience:** Identifying key users becomes crucial. In focus are farmers, agricultural experts, and enthusiasts seeking comprehensive agricultural support. Crop Crafters serves as a comprehensive platform offering three key features: crop recommendations, leaf disease predictions, and a user-friendly enquiry system. By recommending suitable crops, predicting potential diseases, and addressing user queries, the website aims to foster a healthy and supportive environment for farmers, ensuring they feel secure and confident in their agricultural endeavors. 
3. **Site Structure:** Mapping out the structure entails outlining the specific web pages needed for seamless navigation through our diverse set of services. The website contains a basic home page , followed by links to recommendation, prediction and enquiry. To achieve this, an interactive website was designed with dedicated pages for recommendation, prediction, and enquiries. Additionally, a testimonials page dynamically displays feedback from satisfied users.

### Phase 2: Orchestrating Team Synergy 🧑‍🤝‍🧑

This was a self-built project and hence organization was done purely by myself for myself. In terms of development, the project breaks down into four pivotal components. 
- **Firstly**, the overall look and feel were crafted using ``` HTML ```,``` CSS ```, and``` JavaScript ```. 
- **Secondly**, machine learning algorithms were developed to empower the website with predictive functionalities. 
- **Thirdly**, databases were established to store vital information, utilizing the ```XAMPP MySQL``` database. 
- **Lastly**, the integration of the backend was accomplished through ```Flask```, chosen for its ease of use and flexibility, resulting in a cohesive and efficient system that brings together all elements of the project. 


## 2: Crafting Identity 🥸

### Phase 1: Branding and Layout Blueprinting 📘

1. **Brand Essence:** The choice of the name "CropCrafters" encapsulates the essence of agriculture, highlighting the intricate blend of science and artistry that defines this profession. Those involved in agriculture are true crafters, skillfully contributing to the happiness of society through their work. The tagline "Yielding Joy" reflects the website's commitment to exploring the subtleties of agriculture and its role in fostering joy. CropCrafters focuses on enhancing farming production through advanced recommendations and predictions, making it a fitting representation of the platform's mission. 
2. **Visual Harmony:** The visual elements, including the logo, color palette, fonts, and page layouts, are harmonized to create a distinctive online presence. Most styling and animation has been handled by CSS and JavaScript. The thematic essence of the website revolves around agriculture, with dominant colors of green, gray, and yellow ocre, aligning with the subject matter.
Carefully chosen graphics and videos enhance the overall aesthetic, contributing to a visually appealing and informative platform. 
3. **Navigational Map:** The sitemap is intricately crafted, mapping out the structure and flow of the web pages.

### Phase 2: Preparing Content Grounds 🗞️

1. **Content Blueprint:** Content mainly included diverse graphics and information about agricultural aspects, including farming practices and motto of the website. It also contains information about the terms of usage, features available, how to get in touch and details about better farming practices in the form of a blog. I wanted to include not just functionalities but also information about usage as well as other knowledge which could be beneficial. Hence terms, privacy policies and webpages describing certain aspects of agriculture were included. 
2. **Media Collation:** Relevant stock images and graphics are curated to enrich the online narrative. Immense time was taken to gather high quality images that are relevant to the theme of the website.CropCrafters strives for a balance between aesthetics and practicality, creating a platform that is both visually appealing and highly functional. Canva was used to create personalized images that would suit the website. Non copyright as well as self designed images were used in most cases. 
3. **Content Repository:** A well-organized content repository was established, streamlining the retrieval process. A Folder named crop was created with python files along with the basic Flask structure of templates that contained the html pages and static containing the javascript and css files. Every image was stored under the style folder in the static directory. The python models of type joblib and h5 were also saved under this folder. 

### Phase 3: Crafting Visuals and Code 💮

1. **Page Design:** Our web pages take shape with visually appealing designs handled by HTML,CSS and JavaScript. The main idea was to make the page attractive with transitions, and card sliders and soothing with the color palette. The design philosophy emphasizes minimalism, ensuring a user-friendly interface that is both easy to interact with and visually refreshing. The dominant colors of green, gray, and yellow ocre were deliberately chosen for their soothing qualities, providing users with a calming and pleasant experience. Green, in particular, is associated with nature, growth, and harmony, making it an ideal choice for a website centered around agriculture.
2. **Element Crafting:** Engaging page elements such as buttons, hover effects and testimonials are meticulously crafted to enhance user interaction. Graphics and animations were intentionally kept simple, avoiding excessive animations to prioritize functionality over flashy elements. This approach ensures that users can navigate the website seamlessly, focusing on the core features without unnecessary distractions. 
3. **Technical Alchemy:** The marriage of HTML, CSS, and JavaScript is orchestrated to ensure seamless functionality. Every form had JavaScript validations to ensure proper entry of data. 
4. **Feature Development:** The crop prediction model, disease detection system, and farmer's inquiry form are brought to life, forming the backbone of our services. This is executed using python where the joblib library helps save the model. ```Convolutional Neural Networks``` and simple Classification algorithms of ```Random Forest``` and ```Decision Trees``` were used to implement the models. These models are called using Flask to ultimately deploy the final system. 

## 3: Bringing It All Together 🎊

### Assurance and Optimization 🌞

1. **Quality Validation:** Rigorous testing against current web standards ensures a high-quality user experience. It is new, refreshing and without copyright issues. No plagiarism of content has been practiced. 
2. **Issue Resolution:** Any identified issues are promptly addressed, guaranteeing a glitch-free experience. 
  - For example, the tensorflow model was used for disease prediction. However, I did not realize initially that tensorflow was not supported by Python 3.2.1. All libraries including flask, joblib, python had to be reinstalled with version 3.1.1 to ensure proper functioning of the system. 
  - The auto increment feature of the primary key of the database would create a problem in the very first iteration if manually an entry would not be registered. Hence, this issue was resolved too. 

### Phase 2: Cross-Browser Compatibility and Responsiveness 

The designing of css files was such that it could be used across multiple webpages of a certain format. This reduced the load on the Flask deployment thus resulting in faster rendering. JavaScript was only used for validation and hence was minimal too. The website is responsive with the help of ``` @media ``` due to its elaborate designing. 

# Demo Video 👓

The entire working and flow of the website is demostrated below:

https://github.com/AsmitaMondal/CropCrafters/assets/108891810/3e480f1a-fb8f-44c2-a227-94ef22205612

