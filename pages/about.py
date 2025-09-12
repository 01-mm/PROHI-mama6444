import streamlit as st 
st.title("Matija Matic")
st.markdown("""
    ## DSHI Project Information ##             
    In the data science course taken during the spring semester of 2025, I created a data science
    pipeline, where I checked for missing values, renamed columns and variables. I conducted an exploratory data
    analysis and then I built prediction models to predict whether a Portuguese retailer's wholesale
    customers came from the HORECA or Retail channel based on annual spending on different 
    product categories. Channel was the binary target class and the product categories Fresh, 
    Frozen, and Delicatessen were the selected numerical features for the model. After training the models
    with the selected features, cross validation was performed to evaluate model performance. KNN7 was found to be the best performing classifier for this domain as well as the one that 
    performed best on this dataset. Based on the cross validation it provided the best predictions.
                    """)
