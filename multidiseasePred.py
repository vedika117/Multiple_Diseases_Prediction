import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model=pickle.load(open("C:/Users/Vedika khede/OneDrive/Desktop/Multiple Diseases Prediction System/diabetes_trained_model.sav",'rb'))

heart_disease_model=pickle.load(open("C:/Users/Vedika khede/OneDrive/Desktop/Multiple Diseases Prediction System/heart_disease_trained_model.sav",'rb'))

parkinson_model=pickle.load(open("C:/Users/Vedika khede/OneDrive/Desktop/Multiple Diseases Prediction System/ParkinsonDisease_trained_model.sav",'rb'))

#side bar for navigation
with st.sidebar:
    selected=option_menu('Multiple Diseases Prediction System',
                        ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Disease Prediction'],
                        icons=['activity','heart','person'],default_index=0)

#Diabetes Prediction Page
if(selected=='Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction Using Machine Learning')

    #getting input data from user in columns

    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
        Glucose=st.text_input('Glucose Level')
    with col3:    
        BloodPressure=st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')
    with col2:
        Insulin=st.text_input('Insulin Level')
    with col3:    
        Bmi=st.text_input('BMI Value')
    with col1:    
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    with col2:    
        Age=st.text_input('Age of the Person')

    #code for prediction
    diab_diagnosis=''

    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,Bmi,DiabetesPedigreeFunction,Age]])

        if(diab_prediction[0]==1):
            diab_diagnosis='The Person is Diabetic'
        else:
            diab_diagnosis='The Person is Non Diabetic'   
    
    st.success(diab_diagnosis)         

#Heart disease prediction page
if(selected=='Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction Using Machine Learning')
    col1,col2,col3=st.columns(3)
    with col1:
        age=st.text_input('Age of the Person')
    with col2:
        sex=st.text_input('Sex')
    with col3:    
        cp=st.text_input('Chest Pain Type')
    with col1:
        trestbps=st.text_input('Resting Blood Pressure')
    with col2:
        chol=st.text_input('Serum Cholestoral in mg/dL')
    with col3:    
        fbs=st.text_input('Fasting Blood Sugar > 120 mg/dL')
    with col1:    
        restecg=st.text_input('Resting Electrocardiographic results')
    with col2:    
        thalach=st.text_input('Maximum Heart Rate Achieved')
    with col3:    
        exang=st.text_input('Exercise Induced Angina')
    with col1:    
        oldpeak=st.text_input('ST depression induced by exercise')
    with col2:    
        slope=st.text_input('Slope of the peak exercise ST segment')  
    with col3:    
        ca=st.text_input('Major vessels coloured by flourosopy')
    with col1:    
        thal=st.text_input('thal:0=normal; 1=fixed defect; 2=reversible defect')

    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[int(age), int(sex), int(cp), int(trestbps),int (chol),int (fbs), int(restecg),int(thalach),int(exang),int(oldpeak),int(slope),int(ca),int(thal)]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)                      

#parkinsons disease prediction page
if(selected=='Parkinsons Disease Prediction'):
    #page title
    st.title('Parkinsons Disease Prediction Using Machine Learning')
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        Rap = st.text_input('MDVP:RAP')
        
    with col2:
        Ppq = st.text_input('MDVP:PPQ')
        
    with col3:
        Ddp = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        Apq3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        Apq5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        Apq = st.text_input('MDVP:APQ')
        
    with col4:
        Dda = st.text_input('Shimmer:DDA')
        
    with col5:
        Nhr = st.text_input('NHR')
        
    with col1:
        Hnr = st.text_input('HNR')
        
    with col2:
        Rpde = st.text_input('RPDE')
        
    with col3:
        Dfa = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        Ppe = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinson_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, Rap, Ppq,Ddp,Shimmer,Shimmer_dB,Apq3,Apq5,Apq,Dda,Nhr,Hnr,Rpde,Dfa,spread1,spread2,D2,Ppe]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)