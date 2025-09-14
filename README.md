# PROHI Dashboard Example

**Author**: Matija Matic
<!-- As main author, do not write anything in the line below.
The collaborator will edit the line below in GitHub -->
**Collaborator**: Anton Altmeyer

_Note that this file is written in **MarkDown** language. A reference is available here: <https://www.markdownguide.org/basic-syntax/>_

_Here you can include images, like the logo from SU_

![Your dashboard](./assets/project-logo.jpg)

These are screenshots of some of my Dashboard components/widgets:
![alt text](image.png)
![alt text](image-1.png)
![alt text](image-3.png)
![alt text](image-4.png)

## Introduction

For Individual Assignment II in the project management class at Stockholm University, I was tasked with creating a custom Streamlit Dashboard. The purpose of this task was to familiarize me with Streamlit. This will enable me to provide valuable contributions to the major Streamlit Dashboard group project that will be completed as part of this course. In the system description below you will find what the components of this dashboard are. 

## System description
A Streamlit dashboard containing 2 pages was created that included three input widgets, one data widget and one chart widget on the page named Dashboard. The second page named About included the author's name as well as information about the data set used and the data science pipeline completed during the spring semester of 2025. Synthetic data was used for the dashboard. 
### Installation of libraries
In order to create the Streamlit dashboard, I had to follow the following steps which had already been provided to me:
Run the commands below in a terminal to configure the project and install the package dependencies for the first time.

If you are using Mac, you may need to install Xcode. Check the official Streamlit documentation [here](https://docs.streamlit.io/get-started/installation/command-line#prerequisites).

1. Create the environment with `python -m venv env`
2. Activate the virtual environment for Python
   - [Linux/Mac] `source env/bin/activate` 
   - [Windows command prompt] `.\env\Scripts\activate.bat` 
   - [in Windows PowerShell] `.\env\Scripts\Activate.ps1`
3. Make sure that your terminal is in the environment (`env`) not in the global Python installation. The terminal should start with the word `env`
4. Install required packages `pip install -r ./requirements.txt`
5. Check that the installation works running `streamlit hello`
6. Stop the terminal by pressing **Ctrl+C**

### Execute custom Dashboard

First, make sure that you are running Python from the environment. Check the steps 2 and 3 above. Then, to run the custom dashboard execute the following command:

```
> streamlit run Dashboard.py
# If the command above fails, use:
> python -m streamlit run Dashboard.py
```
After making changes and adding different elements to the dashboard I followed the steps listed above to execute the dashboard and see what it looked like in a web browser.

### Dependencies

Tested on Python 3.12.7 with the following packages:
  - Jupyter v1.1.1
  - Streamlit v1.46.1
  - Seaborn v0.13.2
  - Plotly v6.2.0
  - Scikit-Learn v1.7.0
  - shap v0.48.0

## Contributors

Author: Matija Matic
Contact Information: matija.matic@stud.ki.se
