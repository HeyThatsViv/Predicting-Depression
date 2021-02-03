# Predicting Depression Using Health Care Data

**Author**: Vivienne DiFrancesco

<b> A companion dashboard for exploring the data used in this project can be found [here](https://share.streamlit.io/anyoldrandomnamewilldoo/capstone-project/main/Dashboard/depression_app.py)</b>

The contents of this repository is an analysis of using machine learning models to predict depression in people using health care data. This analysis is detailed in hopes of making the work accessible and replicable.

![Depression](https://raw.githubusercontent.com/AnyOldRandomNameWillDOo/Capstone-Project/main/Images/Depression.jpg?token=AQAPWE7MNYJURLAG54DV3RTABZSVK)

## Repository Structure

- <b>README.md:</b> The top level README for reviewers of this project
- <b>first_notebook.ipynb:</b> Beginning narrative documentation of analysis in jupyter notebook up through the data cleaning stages
- <b>second_notebook.ipynb:</b> Continuation of the narriative documentation that begins after data cleaning at the explore stage of the project
- <b>PredictingDepressionSlides.pdf:</b> PDF version of project presentation slides
- <b>project_functions folder:</b> Contains the custom functions written for use in the first_notebook and second_notebook
- <b>Dashboard folder:</b> Folder containing files for creating the companion dashboard for this project

## Abstract

Millions of people globally suffer from depression and it is a debilitating condition. At best it can be difficult for people to live their lives normally and happily, and at worst it leads to death by suicide. Primary care doctors are overwhelmingly finding that they are faced with the need to treat mental health conditions such as depression without any particular training of how to handle such cases.

There is evidence that an integrated approach where physicians regularly screen patients for mental health disorders and work together with psychologists and other mental health professionals to treat patients leads to reduced costs and better patient outcomes. However, this approach can require a lot of buy-in from many individuals, require extra training, and is often not logistically feasible.

Using data from the CDC National Health and Examination Survey, machine learning was applied to predict patients who may have depression based on information that could typically be found in a medical file. These predictions could be used to put patients in touch with experienced mental health professionals sooner and easier.

The results show that 68% of those who have depression and 81% of those who don't have depression can be correctly identified. Though more work needs to be done to create a more accurate model, this shows proof of concept that this is a realistic prediction task. Better results could be yielded by adding more patient information to the data or testing more types of models.


## Introduction

According to the World Health Organization, more that 264 million people globally have depression. Many suicides each year are caused by depression with suicide being among the leading causes of death for young people especially.[1](https://www.who.int/news-room/fact-sheets/detail/depression) The National Institute of Mental Health found that the prevalence of a major depressive episode among U.S. adults in 2017 was 7.1% of people with young adults being the most affected.[2](https://www.nimh.nih.gov/health/statistics/major-depression.shtml) 

The American Psychological Association identified that primary care physicians are often being asked to diagnose mental disorders such as depression without adequate training on how to handle such treatments. According to their numbers, 70% of primary care visits are because of patients’ psychological problems,  more than 80% of patients who have symptoms with no diagnosis receive psychological treatment by a physician, and only 10% follow up to a mental health professional. Patients are not getting the care they desperately need as 70% of individuals with depression go undiagnosed. Among people who commit suicide, 90% of people had a mental disorder and 40% of people had visited their doctor within the last month.[3](https://www.apa.org/health/briefs/primary-care.pdf)

In a study published in JAMA, doctors looked at patient outcomes, cost of care, and other factors between patients that were provided more overt diagnosing and treatment for mental health at standard doctor appointments versus patients that were not. They found that for patients that receive mental health intervention, costs went down, health care services were better utilized, patient outcomes improved, primary care doctor visits declined, treatment interventions were started earlier, and hospital and emergency care visits declined.[4](https://jamanetwork.com/journals/jama/fullarticle/2545685)


## Goal

 The goal of this project is to gather data about people that would typically be in a patient’s medical record to predict depression.

Many clinics or doctors may find it impossible to have such integrated mental health services as cited in the previously mentioned study. Having standard services where patients are constantly screened for mental health disorders and treatment is tightly integrated with teams of physicians and psychological professionals can be expensive, requires a lot of training, requires participation from many individual doctors that may feel too overwhelmed, and may also not be possible in certain areas due to various logistical factors. Using machine learning and data that may otherwise be in a patient’s medical file, the goal is to predict who may have depression in a way that requires very little human participation from doctors and has lower time and money costs associated. The patients who are predicted to have depression could potentially be referred straight to mental health professionals in their area or who accept their health care coverage. The patient’s file could also be flagged to alert the medical staff the next time they have any kind of physician appointment to prompt doctors to start the conversation with patients. At the very least information and resources could be sent to patients directly to encourage them to take action on their own behalf.


## Data

The data for this project is from the Centers for Disease Control and Prevention National health and Nutrition Examination Survey. This data includes a vast array of health data done on a sample of the American population each year and is released every two years. The data can be found at this website: https://wwwn.cdc.gov/nchs/nhanes/default.aspx. 

For this project, data was taken from the years between 2005 and 2018 and comprised of 36259 entries total of U.S. adults. Only data that was consistent across years was used and there was effort to only include data that would be reasonably found in a patient's medical file. Using as little data as possible while still being able to have accurate predictions is desirable as it would catch more people who may not have a very deep medical history and also puts less burden on providers to have to capture so much information.


## Approach

The target was calculated using the PHQ-9 depression screening tool that was asked of all participants in the NHANES data. A study showed that this screening tool has a specificity and sensitivity of 88% for major depression at a threshold score of 10 or more.[5](https://pubmed.ncbi.nlm.nih.gov/11556941/) People were divided into “depressed” and “not depressed” categories based on the score for their answers in the screening tool with a score of 10 or more being “depressed”.

The approach for this project was to create many different model types to see what performs the best and to compare and contrast the different types of models. The modeling effort was done starting with simpler models and moving to more complex models. The OSEMiN process is the overarching structure of this project. 


## Methods

The way the data was preprocessed with feature engineering, filling missing values, and scaling was done with the goal of increasing accuracy of the models. Undersampling and oversampling techniques were used in conjunction with each other to create a dataset with balanced classes to test against the unbalanced and non-resampled dataset. For each type of model, a model was first trained and fitted with default parameters as a base. Then, key parameters were chosen to tune using sklearn GridSearchCV and the best parameters were used to run the model. Finally, the tuned parameters were used to fit the same model using the resampled data for comparison. Performance was compared to the base model of each type, as well as between different model types. 


## Results

![ConfusionMatrix](https://raw.githubusercontent.com/AnyOldRandomNameWillDOo/Capstone-Project/main/Images/Tuned%20Logistic%20Regression.png?token=AQAPWE6RX5M2R57RIBYZI7LABZSLQ)

- <b>Overall the best model turned out to be the logistic regression.</b> Though many models were more accurate at classifying the not depressed class, the logistic regression was the simplest model that most accurately predicted the depression class while still having good predictions for the not depressed class. Logistic regression was also the simplest model to achieve these results. 

- <b>The depression class was particularly tricky to classify accurately.</b> Some models were able to accurately identify 95%+ of the true negatives but the highest percentage any models were able to achieve in capturing the true positives was 68%. That is certainly better than guessing and proves that this task is feasible, but more work will need to be done to find the best approach.

- <b>The most influencial features of the best model are shown in the chart below.</b>

![ImportantFeatures](https://raw.githubusercontent.com/AnyOldRandomNameWillDOo/Capstone-Project/main/Images/Most%20Important%20Features.png)


## Recommendations

- <b>Health care professionals should prepare themselves to help patients with depression and can especially watch out for the most important features from the model.</b> Right now physicians are still handling much of the first line care for patients with depression and should prepare themselves on how to better provide care for these patients. The most meaningful features for the model that providers can watch for included:
    - Having memory or emotional problems 
    - Lower income and not being able to work
    - Trouble sleeping and sleeping too much or too little


- <b>Don't use tree based models.</b> The XGBoost classifier had the best performance as the base model was actually similar in performance to the non-tree models. But once the XGBoost model was tuned, it got worse.

- <b>Add more data from the start.</b> Originally, a dataset with less features was used to model but performance of all the models was terrible. More features were added to the dataset and model performance improved enough to show some accuracy in classification, but having even more data from the start would set one up for greater success.

- <b>Don't use under sampling combined with SMOTE for evening out the class distribution.</b> It's possible other techniques/combinations of under sampling and over sampling could help modeling, but the combination used here of under sampling and SMOTE did worse overall in modeling. Using the balanced classes parameter worked better.

- <b>Everyone should prepare themselves on how to handle mental health problems and to push those they know to get proper help.</b> Help to destigmatize mental health problems and encourage those you know to seek help from experienced professionals. Also get help for yourself if you find yourself in need of it. It's highly likely that everyone will find themselves in need of professional help at some point or another.


## Future Directions

- <b>Try different models.</b> None of these models did particularly well and perhaps trying a different modeling tactic would do the trick like a neural network.

- <b>Add more data.</b> It is desirable to get a well performing model with as little information needed about patients as possible but after modeling options have been exhausted, more data is the best bet for improving performance. Finding the right balance between acceptable amount of error and amount of data needed to have an accurate model is definitely easier said than done.


## References

1. World health Organization Depression Overview: https://www.who.int/news-room/fact-sheets/detail/depression

2. National Institute of Mental Health on Major Depression: https://www.nimh.nih.gov/health/statistics/major-depression.shtml

3. American Psychological Association Briefing Series on the Role of Psychology in Health Care: https://www.apa.org/health/briefs/primary-care.pdf

4. Association of Integrated Team-Based Care With Health Care Quality, Utilization, and Cost: https://jamanetwork.com/journals/jama/fullarticle/2545685

5. The PHQ-9: validity of a brief depression severity measure https://pubmed.ncbi.nlm.nih.gov/11556941/

6. Take the PHQ-9 depression screener online: https://www.mdcalc.com/phq-9-patient-health-questionnaire-9
