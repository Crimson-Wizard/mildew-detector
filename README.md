
# Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). 
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

## The rationale to map the business requirements to the Data Visualisations and ML tasks


## ML Business Case

## Dashboard Design

### 1. Home Page

- Purpose: Provide a brief introduction and overview of the dashboard.
- Features:
    - A welcoming message explaining the tool's purpose.
    - Links or navigation buttons to access different sections of the dashboard.
    - Key objectives of the tool outlined for the user.

### 2. Mildew Detector Page

- Purpose: Allow users to upload images of cherry leaves and predict whether the leaves are healthy or contain powdery mildew.
- Features:
    - File Uploader: Enables users to upload multiple images (.png, .jpg, .jpeg).
    -  Image Display: Displays the uploaded image along with its dimensions.
    - Prediction Output:
        - Visual representation of prediction probabilities (e.g., bar chart or pie chart).
        - Classifies each image as "Healthy" or "Powdery Mildew".
    - Results Table: Summarizes the results for all uploaded images in a tabular format.
    - Downloadable Report: Provides a downloadable CSV report containing the predictions.

### 3. ML Performance Metrics Page

- Purpose: Showcase the performance of the machine learning model used for mildew detection.
- Features:
    - Label Distribution: Visual representation of the class distribution (Healthy vs. Powdery Mildew) in the training, validation, and test datasets.
    - Training History:
        - Accuracy chart: Model’s accuracy over the training epochs.
        - Loss chart: Model’s loss over the training epochs.
    - Test Set Evaluation:
        - Displays key metrics such as loss and accuracy on the test dataset.
        - Data displayed in a table for clarity.

### 4. Dataset Page

- Purpose: Provide users with insights into the dataset used for training and testing the model.
- Features:
    - Dataset Overview: A summary of the dataset, including the number of samples, classes, and any preprocessing applied.
    - Sample Visualizations: Displays example images from each class (Healthy and Powdery Mildew).
    - Download Link: Offers a link to download the dataset for users who wish to explore it further.

## Bugs

### 1. Issue: Overlaying Average Validation Image

- Problem: Unable to overlay the average validation image as intended during development.

### 2. Issue: Large Files and Git Commit

- Problem: Encountered issues pushing to Git due to files being too large.
- Resolution: Spent 13 hours fixing this by identifying and deleting large files.

### 3. Issue: Streamlit Run Not Opening Selected File

- Problem: When using streamlit run, the app failed to open the file from the app_pages folder, but it worked when providing the file path manually in the terminal.

### 4. Issue: Case Sensitivity in Class Name

- Problem: app.py could not locate the app_pages folder because the Multipage class was miswritten as multipage, which is case-sensitive.
- Resolution: Corrected the class name to Multipage.

### 5. Issue: Missing Evaluation File and Large File Pushing

- Problem: Missing evaluation.pk1 file required rerunning the Jupyter notebook to regenerate it. However, the file was too large to push to Git.
- Resolution:
Pushed individual files to Git.
Identified that trained_model.h5 was the actual issue.
Used Git LFS (Large File Storage) to handle the large .h5 file.

### 6. Issue: Committed Files Ignored by .gitignore

- Problem: Previously committed files that were later added to .gitignore remained tracked.
- Resolution:
Used git rm --cached -r . to untrack files.
Re-added files with git add ., committed the changes, and pushed them back to the repository with .gitignore rules applied.

### 7. Issue: Conformance to PEP8 Standards

- Action: Ran autopep8 on Python code to ensure adherence to PEP8 standards.

### 8. Issue: Montage Section Not Working on Live Site

- Problem: The "create montage" section worked locally but failed on the live site.
Cause: The validation set was ignored in .gitignore, but the function needed it.
- Resolution: Removed the validation set from .gitignore and redeployed. The issue was resolved.

### 9. Issue: Predictive Analytics Stopped Working on Live Site

- Problem: The predictive analytics section worked locally but failed on the live site.
- Cause: Discovered TensorFlow version mismatch:
Local: TensorFlow Version 2.13.0
Live Site: TensorFlow Version 2.6.0
- Resolution:
Compressed files using Git LFS and adjusted Heroku build packs.
Despite model accuracy, reduced the layers in the model to make it smaller for deployment.
Identified Git LFS stored all .h5 files, which Heroku couldn’t read.
Removed LFS, uninstalled Git LFS, removed .h5 files from .gitattributes, and re-pushed the original file.

## Deployment

- I linked my GitHub repository to Heroku and chose the manual deployment option to avoid accidentally deploying untested or buggy code.

Older Python Version Issue:
- My app needed a specific Heroku stack (heroku-20) to support my code.

Using API Key to Log into Heroku via Terminal:
- I had to authenticate in my terminal using Heroku’s API key because the stack change wasn’t something I could handle directly from the Heroku dashboard.

Changed the Heroku Stack:
- I updated the stack to heroku-20 to work with the version of Python i was running

## Main Data Analysis and Machine Learning Libraries


## Credits


### Content


### Media

- Streamlit
- Jupyter Notebook
- NumPy
- Pandas
- Plotly
- Seaborn
- Matplotlib
- TensorFlow
- Python
- Heroku
- GitHub
- Vs Code
- GitPod
- Am I Responsive
- Code Institute Python Linter
- Chat Gpt
- Stack Overflow
- Slack PA community group

## Acknowledgements 


