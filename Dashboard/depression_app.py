# Import packages
import streamlit as st
import pandas as pd 
import plotly.express as px
import plotly.io as pio

# Set the plotly template
pio.templates.default = "plotly_white"

# Setting the title of the tab and the favicon
st.set_page_config(page_title='Examining Depression Using Health Care Data', page_icon = ':rain_cloud:', layout = 'centered')

# Setting the title on the page with some styling
st.markdown("<h1 style='text-align: center'>Examining Depression Using Health Care Data</h1><hr style='height:2px;border-width:0;color:gray;background-color:gray'>", unsafe_allow_html=True)

# Putting in personal details with some styling
st.markdown("<body style='text-align: center'> <b>Created by Vivienne DiFrancesco</b><br>- viviennedifrancesco@gmail.com<br><a href=https://github.com/AnyOldRandomNameWillDOo/Capstone-Project>- Project repository on GitHub</a><hr style='height:2px;border-width:0;color:gray;background-color:gray'></body>", unsafe_allow_html=True)

# Project information
st.header('Introduction')
st.markdown('Millions of people globally suffer from depression and it is a debilitating condition. At best it can be difficult for people to live their lives normally and happily, and at worst it leads to death by suicide. Primary care doctors are overwhelmingly finding that they are faced with the need to treat mental health conditions such as depression without any particular training of how to handle such cases.')
st.markdown('There is evidence that an integrated approach where physicians regularly screen patients for mental health disorders and work together with psychologists and other mental health professionals to treat patients leads to reduced costs and better patient outcomes. However, this approach can require a lot of buy-in from many individuals, require extra training, and is often not logistically feasible.')
st.markdown('Using data from the [CDC National Health and Examination Survey](https://wwwn.cdc.gov/nchs/nhanes/default.aspx), machine learning was applied to predict patients who may have depression based on information that could typically be found in a medical file. These predictions could be used to put patients in touch with experienced mental health professionals sooner and easier.')
st.markdown("This dashboard provides an interactive tool for users to explore more of the data from the machine learning project. It is meant to be a companion piece to the larger project which can be found [here](https://github.com/AnyOldRandomNameWillDOo/Capstone-Project). These plots are interactive with hover text and zooming capabilities. The figures may take a moment to update when changed.<hr style='height:2px;border-width:0;color:gray;background-color:gray'>", unsafe_allow_html=True)

# Add the data
df = pd.read_csv('StreamlitData.csv')

# Creating a list of numerical columns
num_cols = ['Age', 'Asthma Onset', 'Arthritis Onset', 'Heart Failure Onset', 'Heart Disease Onset', 
'Angina Onset', 'Heart Attack Onset', 'Stroke Onset', 'Emphysema Onset', 'Bronchitis Onset', 
'Liver Condition Onset', 'Thyroid Problem Onset', 'Cancer Onset', 'Weight', 'Height', 'BMI', 
'Pulse', 'Systolic', 'Diastolic', 'Total Cholesterol', 'HDL', 'Triglycerides', 'LDL', 'Albumin', 
'ALT', 'AST', 'ALP', 'BUN', 'Calcium', 'CO2', 'Creatinine', 'GGT', 'Glucose', 'Iron', 'LHD', 
'Phosphorus', 'Bilirubin', 'Total Protein', 'Uric Acid', 'Sodium', 'Potassium', 'Chloride', 
'Osmolality', 'Globulin', 'White BCC', 'Lymphocyte Percent', 'Monocyte Percent', 'Neutrophils Percent', 
'Eosinophils Percent', 'Basophils Percent', 'Lymphocyte Count', 'Monocyte Count', 'Neutrophils Count', 
'Eosinophils Count', 'Basophils Count', 'RBC Count', 'Hemoglobin', 'Hematocrit', 'MCV', 'MCH', 'MCHC', 
'RDW', 'Platelet Count', 'MPV', 'Time In Current Job', 'Sleep Hours', 'Sedentary Time', 
'Drinks Per Occasion', 'Drinks Past Year', 'Marijuana Per Month', 'Cocaine Per Month', 'Heronine Per Month', 
'Meth Per Month', 'Start Smoking Age', 'Previous Cigarettes Per Day', 'Current Cigarettes Per Day', 
'Days Quit Smoking']

# Creating a list of categorical columns with a "None" option included
none_included = ['None','Gender', 'Race', 'Citizenship', 'Education Level', 'Marital Status', 'Pregnant', 'Birth Place', 
'Veteran', 'Household Income', 'Asthma', 'Asthma Currently', 'Asthma Emergency', 'Anemia', 'Ever Overweight', 
'Blood Transfusion', 'Arthritis', 'Heart Failure', 'Heart Disease', 'Angina', 'Heart Attack', 'Stroke', 
'Emphysema', 'Bronchitis', 'Liver Condition', 'Thyroid Problem', 'Bronchitis Currently', 
'Liver Condition Currently', 'Thyroid Problem Currently', 'Cancer', 'First Cancer Type', 'Second Cancer Type', 
'Third Cancer Type', 'Fourth Cancer Count', 'Heart Attack Relative', 'Asthma Relative', 'Diabetes Relative', 
'Hay Fever', 'Arthritis Type', 'First Cancer Count', 'Second Cancer Count', 'Third Cancer Count', 
'Irregular Pulse', 'Full Time Work', 'Work Type', 'Out Of Work', 'Trouble Sleeping History', 
'Vigorous Recreation', 'Moderate Recreation', 'Vigorous Work', 'Moderate Work', 'Lifetime Alcohol Consumption', 
'Cant Work', 'Limited Work', 'Walking Equipment', 'Memory Problems', 'Limitations', 'Healthcare Equipment', 
'Health Problem Other Impairment', 'Health Problem Bone Or Joint', 'Health Problem Weight', 
'Health Problem Back Or Neck', 'Health Problem Arthritis', 'Health Problem Cancer', 'Health Problem Other Injury', 
'Health Problem Breathing', 'Health Problem Stroke', 'Health Problem Emotional', 'Health Problem Blood Pressure', 
'Health Problem Mental Retardation', 'Health Problem Hearing', 'Health Problem Heart', 'Health Problem Vision', 
'Health Problem Diabetes', 'Health Problem Birth Defect', 'Health Problem Senility', 
'Health Problem Other Developmental', 'Marijuana Use', 'Cocaine Use', 'Cocaine Number Uses', 'Heroine Use', 
'Meth Use', 'Meth Number Uses', 'Inject Drugs', 'Rehab Program', 'Current Smoker', 'Household Smokers', 
'Household Size']

# Creating a list of regular categorical columns without "None"
cat_cols = none_included.copy()
cat_cols.remove('None')

# Creating a dictionary of categorical feature information to display
cat_cols_dict = {'Gender': 'Is the person male or female?', 
                 'Race': 'What race best describes the person?', 
                 'Citizenship': 'Is the person a citizen?', 
                 'Education Level': 'What level of education as the person completed?', 
                 'Marital Status': 'What is the marital status of the person?', 
                 'Pregnant': 'Is the person pregnant?', 
                 'Birth Place': 'Where was the person born?', 
                 'Veteran': 'Is the person a veteran?', 
                 'Household Income': 'What is the household income of the person?', 
                 'Asthma': 'Has the person ever been diagnosed with asthma?', 
                 'Asthma Currently': 'Does the person currently have asthma?', 
                 'Asthma Emergency': 'Has the person had an emergency care visit for asthma in the last year?', 
                 'Anemia': 'Is the person taking treatment for anemia?', 
                 'Ever Overweight': 'Has a doctor ever told the person they were overweight?', 
                 'Blood Transfusion': 'Has the person ever recieved a blood transfusion?', 
                 'Arthritis': 'Has the person ever been diagnosed with arthritis?', 
                 'Heart Failure': 'Has the person ever been diagnosed with heart failure?', 
                 'Heart Disease': 'Has the person ever been diagnosed with heart disease?', 
                 'Angina': 'Has the person ever been diagnosed with angina?', 
                 'Heart Attack': 'Has the person ever been diagnosed with a heart attack?', 
                 'Stroke': 'Has the person ever been diagnosed with a stroke?', 
                 'Emphysema': 'Has the person ever been diagnosed with emphysema?', 
                 'Bronchitis': 'Has the person ever been diagnosed with chronic bronchitis?', 
                 'Liver Condition': 'Has the person ever been diagnosed with a liver condition?', 
                 'Thyroid Problem': 'Has the person ever been diagnosed with a thyroid problem?', 
                 'Bronchitis Currently': 'Does the person currently have chronic bronchitis?', 
                 'Liver Condition Currently': 'Does the person currently have a liver condition?', 
                 'Thyroid Problem Currently': 'Does the person currently have a thyroid problem?', 
                 'Cancer': 'Has the person ever been diagnosed with cancer?', 
                 'First Cancer Type': 'If the person has had a first cancer, what kind was it?', 
                 'Second Cancer Type': 'If the person has had a second cancer, what kind was it?', 
                 'Third Cancer Type': 'If the person has had a third cancer, what kind was it?', 
                 'Fourth Cancer Count': 'Was the person ever diagnosed with a fourth cancer?', 
                 'Heart Attack Relative': 'Does the person have a close relative who has been diagnosed with a heart attack?', 
                 'Asthma Relative': 'Does the person have a close relative who has been diagnosed with asthma?', 
                 'Diabetes Relative': 'Does the person have a close relative who has been diagnosed with diabetes?', 
                 'Hay Fever': 'Has the person had an episode of hay fever in the last year?', 
                 'Arthritis Type': 'If the person has arthritis, what type is it?', 
                 'First Cancer Count': 'Was the person ever diagnosed with a first cancer?', 
                 'Second Cancer Count': 'Was the person ever diagnosed with a second cancer?', 
                 'Third Cancer Count': 'Was the person ever diagnosed with a third cancer?', 
                 'Irregular Pulse': 'Does the person have an irregular pulse?', 
                 'Full Time Work': 'Does the person usually work a full time schedule?', 
                 'Work Type': 'What kind of worker is the person?', 
                 'Out Of Work': 'If person is out of work, what is the reason?', 
                 'Trouble Sleeping History': 'Has the person ever told a doctor they have trouble sleeping?', 
                 'Vigorous Recreation': 'Does the person engage in vigorous physical exercise during their free time?', 
                 'Moderate Recreation': 'Does the person engage in moderate physical exercise during their free time?', 
                 'Vigorous Work': 'Does the person have a job that requires vigorous physical activity?', 
                 'Moderate Work': 'Does the person have a job that requires moderate physical activity?', 
                 'Lifetime Alcohol Consumption': 'Has the person ever consumed alcohol in their lifetime?', 
                 'Cant Work': 'Are long term health problems keeping the person from working?', 
                 'Limited Work': 'Are long term health problems limiting the type or amount of work the person can do?', 
                 'Walking Equipment': 'Does the person need special equipment to walk because of a long termp health problem?', 
                 'Memory Problems': 'Does the person experience confusion or memory problems?', 
                 'Limitations': 'Is the person limited in any way because of physical, mental, or emotional problems?', 
                 'Healthcare Equipment': 'Does the person require any special healthcare equipment?', 
                 'Health Problem Other Impairment': 'Does the person have some other impairment or problem that causes difficulty?', 
                 'Health Problem Bone Or Joint': 'Does the person have a bone or joint problem/impairment that causes difficulty?', 
                 'Health Problem Weight': 'Does the person have a weight problem/impairment that causes difficulty?', 
                 'Health Problem Back Or Neck': 'Does the person have a back or neck problem/impairment that causes difficulty?', 
                 'Health Problem Arthritis': 'Does the person have an arthritis problem/impairment that causes difficulty?', 
                 'Health Problem Cancer': 'Does the person have a cancer problem/impairment that causes difficulty?', 
                 'Health Problem Other Injury': 'Does the person have a problem/impairment from some other injurty that causes difficulty?', 
                 'Health Problem Breathing': 'Does the person have a breathing or lung problem/impairment that causes difficulty?', 
                 'Health Problem Stroke': 'Does the person have a stroke problem/impairment that causes difficulty?', 
                 'Health Problem Emotional': 'Does the person have an emotional problem/impairment that causes difficulty?', 
                 'Health Problem Blood Pressure': 'Does the person have a blood pressure problem/impairment that causes difficulty?', 
                 'Health Problem Mental Retardation': 'Does the person have a mental retardation problem/impairment that causes difficulty?', 
                 'Health Problem Hearing': 'Does the person have a hearing problem/impairment that causes difficulty?', 
                 'Health Problem Heart': 'Does the person have a heart problem/impairment that causes difficulty?', 
                 'Health Problem Vision': 'Does the person have a vision problem/impairment that causes difficulty?', 
                 'Health Problem Diabetes': 'Does the person have a diabetes problem/impairment that causes difficulty?', 
                 'Health Problem Birth Defect': 'Does the person have a birth defect problem/impairment that causes difficulty?', 
                 'Health Problem Senility': 'Does the person have a senility problem/impairment that causes difficulty?', 
                 'Health Problem Other Developmental': 'Does the person have some other developmental problem/impairment that causes difficulty?', 
                 'Marijuana Use': 'Has the person ever used marijuana?', 
                 'Cocaine Use': 'Has the person ever used cocaine?', 
                 'Cocaine Number Uses': 'How many times total in their lifetime has the person used cocaine?', 
                 'Heroine Use': 'Has the person ever used heroine?', 
                 'Meth Use': 'Has the person ever used methamphetamine?', 
                 'Meth Number Uses': 'How many times total in their lifetime has the person used methamphetamine?', 
                 'Inject Drugs': 'Has the person ever used needles to inject illegal drugs?', 
                 'Rehab Program': 'Has the person ever been in a drug treatment/rehabilitation program?', 
                 'Current Smoker': 'Does the person currently smoke?', 
                 'Household Smokers': 'How many people in the person\'s household smoke?', 
                 'Household Size': 'How many people live in the person\'s household?'}

# Creating a dictionary of numerical feature information to display
num_cols_dict = {'Age': 'What is the age of the person?',
 'Asthma Onset': 'If person has asthma, what age was the person at onset?',
 'Arthritis Onset': 'If person has arthritis, what age was the person at onset?',
 'Heart Failure Onset': 'If person has heart failure, what age was the person at onset?',
 'Heart Disease Onset': 'If person has heart disease, what age was the person at onset?',
 'Angina Onset': 'If person has angina, what age was the person at onset?',
 'Heart Attack Onset': 'If person had a heart attack, what age was the person at onset?',
 'Stroke Onset': 'If person had a stroke, what age was the person at onset?',
 'Emphysema Onset': 'If person has emphysema, what age was the person at onset?',
 'Bronchitis Onset': 'If person has chronic bronchitis, what age was the person at onset?',
 'Liver Condition Onset': 'If person has/had a liver condition, what age was the person at onset?',
 'Thyroid Problem Onset': 'If person has/had a thyroid problem, what age was the person at onset?',
 'Cancer Onset': 'If person has/had cancer, what age was the person at onset?',
 'Weight': 'Weight of the person in kg',
 'Height': 'Height of the person in cm',
 'BMI': 'Body mass index of the person',
 'Pulse': '60 second pulse of the person',
 'Systolic': 'Systolic blood pressure reading of the person in mmHg',
 'Diastolic': 'Diastolic blood pressure reading of the person in mmHg',
 'Total Cholesterol': 'Total cholesterol of the person in mg/dL',
 'HDL': 'Direct HDL cholesterol of the person in mg/dL',
 'Triglycerides': 'Triglyceride level of the person in mg/dL',
 'LDL': 'Friedewald equation LDL cholesterol of the person in mg/dL',
 'Albumin': 'Serum albumin in g/dL',
 'ALT': 'Alanine Aminotransferase in IU/L',
 'AST': 'Aspartate Aminotransferase in IU/L',
 'ALP': 'Alkaline Phosphatase in IU/L',
 'BUN': 'Blood Urea Nitrogen in mmol/L',
 'Calcium': 'Total calcium in mg/dL',
 'CO2': 'Bicarbonate in mmol/L',
 'Creatinine': 'Serum creatinine in mg/dL',
 'GGT': 'Gamma Glutamyl Transferase in IU/L',
 'Glucose': 'Serum glucose in mg/dL',
 'Iron': 'Serum iron in ug/dL',
 'LHD': 'Lactate Dehydrogenase in IU/L',
 'Phosphorus': 'Phosphorus in mg/dL',
 'Bilirubin': 'Total bilirubin in mg/dL',
 'Total Protein': 'Total protein in g/dL',
 'Uric Acid': 'Uric acid in mg/dL',
 'Sodium': 'Sodium in mmol/L',
 'Potassium': 'Potassium in mmol/L',
 'Chloride': 'Chloride in mmol/L',
 'Osmolality': 'Osmolality in mmol/Kg',
 'Globulin': 'Globulin in g/dL',
 'White BCC': 'White blood cell count in 1000 cells/uL',
 'Lymphocyte Percent': 'Lymphocyte percent (%)',
 'Monocyte Percent': 'Monocyte percent (%)',
 'Neutrophils Percent': 'Segmented neutrophils percent (%)',
 'Eosinophils Percent': 'eosinophils percent (%)',
 'Basophils Percent': 'Basophils percent (%)',
 'Lymphocyte Count': 'Lymphocyte number in 1000 cells/uL',
 'Monocyte Count': 'Monocyte number in 1000 cells/uL',
 'Neutrophils Count': 'Segmented neutrophils number 1000 cells/uL',
 'Eosinophils Count': 'Segmented eosinophils number in 1000 cells/uL',
 'Basophils Count': 'Basophils number in 1000 cells/uL',
 'RBC Count': 'Red blood cell count in million cells/uL',
 'Hemoglobin': 'Hemoglobin in g/dL',
 'Hematocrit': 'Hematocrit percent',
 'MCV': 'Mean cell volume in fL',
 'MCH': 'Mean cell hemoglobin in pg',
 'MCHC': 'Mean cell hemoglobin concentration in g/dL',
 'RDW': 'Red cell distribution width percent',
 'Platelet Count': 'Platelet count in 1000 cells/uL',
 'MPV': 'Mean platelet volume in fL',
 'Time In Current Job': 'How many months has the person worked in their current job?',
 'Sleep Hours': 'Number of hours the person usually sleeps at night',
 'Sedentary Time': 'How many minutes does the person usually spend sedentary in a typical day?',
 'Drinks Per Occasion': 'On the days that the person drinks alcohol, how many drinks on average does the person consume?',
 'Drinks Past Year': 'How many alcoholic drinks has the person had in the past year?',
 'Marijuana Per Month': 'How many days has the person used marijuana or hashish in the past month?',
 'Cocaine Per Month': 'How many days has the person used cocaine in any form in the past month?',
 'Heronine Per Month': 'How many days has the person used heroin in the past month?',
 'Meth Per Month': 'How many days has the person used methamphetamine in the past month?',
 'Start Smoking Age': 'If the person has smoked cigarettes regularly, at what age did they start?',
 'Previous Cigarettes Per Day': 'If the person quit smoking, about how many cigarettes did they smoke per day before they quit?',
 'Current Cigarettes Per Day': 'If the person currently smokes, about how many cigarettes per day have they smoked in the last month?',
 'Days Quit Smoking': 'If the person has quit smoking, about how many days has it been since they quit?'}

# Creating the container for the first plot
with st.beta_expander('Look at the percentage of depression among categorical features'):

# Creating a selectbox dropdown with the categorical features to choose from
    cat_option = st.selectbox('Select a feature to examine', cat_cols, key='cat_cols1')

# The function to run the first plot
    def percentage_plot(col):

        # Creates a temporary dataframe to get the percentages
        temp_df = df.groupby(col)['Depression'].value_counts(normalize=True)
        temp_df = temp_df.mul(100).rename('Percent').reset_index()
        temp_df['Percent'] = temp_df['Percent'].round(decimals=1)

        # Plot the percentages with the temporary dataframe
        fig = px.bar(temp_df[temp_df['Depression']=='Depressed'], x=col, y='Percent', color='Percent', 
                    barmode="group", text='Percent', color_continuous_scale='geyser', title=f"Percent Depression By {col}")

        # Explaination of the features displays along with the graph
        st.markdown('**Explaination of the feature selected:**')
        st.markdown(f'**- {cat_option}: {cat_cols_dict[cat_option]}**')
        return fig

# Running the function
    st.plotly_chart(percentage_plot(cat_option))




# Creating the container for the second plot
with st.beta_expander('Look at depression in numerical features plotted together'):

# Creating selectbox dropdowns with the numerical features to choose from
    num_optionX = st.selectbox('Select a feature for the X-axis', num_cols, key='x1')
    num_optionY = st.selectbox('Select a feature for the Y-axis', num_cols, key='y1')


# The function to run the second plot
    def scatter_plot(x, y):

        # Plot the features selected by the user
        fig = px.scatter(df, x=x, y=y, color="Depression", color_discrete_sequence=['#268d87', '#d26a3e'], 
                title=f"{y} vs {x} and Depression")

        # Explaination of the features displays along with the graph
        st.markdown('**Explaination of the features selected:**')
        st.markdown(f'**- {num_optionX}: {num_cols_dict[num_optionX]}**')
        st.markdown(f'**- {num_optionY}: {num_cols_dict[num_optionY]}**')
        return fig

# Running the function
    st.plotly_chart(scatter_plot(num_optionX, num_optionY))




# Creating the container for the third plot
with st.beta_expander('Look at depression in a numerical feature alone or add a categorical feature'):

# Creating selectbox dropdowns with the features to choose from, 'None' will render by default for the categorical option
    num_optionX2 = st.selectbox('Select a numerical feature for the X-axis', num_cols, key='x2')
    cat_optionY = st.selectbox('Select a categorical feature for the Y-axis if desired', none_included, key='y2')

# The function to run the third plot
    def strip_plot(x, y='None'):

        # Plot the features selected by the user when y is set to 'None'
        if y=='None':
            fig = px.strip(df, x=x, orientation="h", color="Depression", color_discrete_sequence=['#268d87', '#d26a3e'],
                        title=f'{x} and Depression')

            # Explaination of the feature to display along with the graph
            st.markdown('**Explaination of the feature selected:**')
            st.markdown(f'**- {num_optionX2}: {num_cols_dict[num_optionX2]}**')
            return fig

        # Plot the features selected by the user when y is not 'None'
        else:
            fig = px.strip(df, x=x, y=y, orientation='h', color='Depression', color_discrete_sequence=['#268d87', '#d26a3e'],
                        title=f"{x} with {y} and Depression")

            # Explaination of the features displays along with the graph
            st.markdown('**Explaination of the features selected:**')
            st.markdown(f'**- {num_optionX2}: {num_cols_dict[num_optionX2]}**')
            st.markdown(f'**- {cat_optionY}: {cat_cols_dict[cat_optionY]}**')
            return fig

# Running the function
    st.plotly_chart(strip_plot(num_optionX2, cat_optionY))