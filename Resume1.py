import streamlit as st

st.set_page_config(layout="wide")

column1, column2 = st.columns(2)

with column1:
    # st.image("D:/Data Science/Pycharm Projects-2/app2.portfolio/images/vinayPic.JPG", width=300)
    st.image("vinayPic.JPG", width=300)
    st.title("Vinay Palusa")
with column2:

    st.info("Address :- ")
    st.write("H.No: 18-3-654/B/19,  ")
    st.write("GANESH  NAGAR,  ")
    st.write("Aliabad, Near Charminar,  ")
    st.write("HYDERABAD- 500053,  ")
    st.write("TELANGANA,  INDIA  ")
    st.write("Mobile No.:- +919030263855")


content2 = """
    Collection and verification of confidential client data via publically available and internal sources 
    Understand the firm’s KYC requirements when completing documentation inclusive of Customer 
    Identification Program (CIP), Enhanced Due Diligence (EDD), and the Product Due Diligence Questionnaire (PDD).
    Compare and contrast differences within KYC records , highlight and escalate any discrepancies
    Handling and maintenance of confidential client documentation.
     """
content1= """To work in a stimulating environment that would hone my skills and provide me ample opportunities for development in all spears so that
 I can give my best to the organization I work for . """
st.header("CAREER OBJECTIVE:")
st.info(content1)

st.subheader("EDUCATIONAL QUALIFICATION:- ")
#st.image("D:/Data Science/Pycharm Projects-2/app2.portfolio/images/Vinay_Education_Details.png", width=1000)
st.image("Vinay_Education_Details.png", width=1000)
st.subheader("EXPERIENCE-1:")
st.write("Working as KYC Operational Analyst in JP Morgan & Chase from April-2017 to July-2019.", unsafe_allow_html=True)
content3= """Summary:-- KYC Operations is a firm-wide utility supporting all Lines of Business in the completion of requirements to satisfy the firm’s Know Your Customer (KYC) standards and partner with Global Financial Crimes Compliance, all JPMorgan Lines of Business and their KYC Officers and Client Owners and other utilities such as Client List Screening and Client Reference Data Operations to support and maintain the integrity of our Client KYC information. """
st.write(content3)
st.info("JOB PROFILE:-")
content4= """Collection and verification of confidential client data via publically available and internal sources

Understand the firm’s KYC requirements when completing documentation inclusive of Customer 
Identification Program (CIP), Enhanced Due Diligence (EDD), and the Product Due Diligence Questionnaire (PDD).
Compare and contrast differences within KYC records , highlight and escalate any discrepancies

Handling and maintenance of confidential client documentation
 """
st.write(content4)

st.subheader("EXPERIENCE-2:")
content5= """Worked as Customer Due Diligence (CDD) Analyst in HSBC Electronic Data Processing (India) Pvt. Ltd. From April-2013 to March 2017. """
st.write(content5)
st.info("JOB PROFILE:-")
content6="""Responsible administration of the Banks due diligence regulations, bank policies and procedures applicable to the due diligence monitoring including “Transactions”. 
Review all high risk customers detected through the automated scoring system or additional supplemental processes and assess to determine if the customer risk is accurate and whether the risk is too heightened to continue the relationship. 
This includes the collection of specific due diligence (KYC) information for specific customer types as well as completing risk matrices for specific customer types. 
This process will also include identifying key individuals, especially beneficial owners and negative news searches on them - extensive internet searches. 
Ongoing reviews are conducted periodically and triggered based as determined by the customer’s risk rating. Escalate appropriate issues to management. """
st.write(content6)
st.subheader("HOBBIES:")
st.write("1.Playing chess")
st.write("2.Listening  to Music.")
st.write("3.Playing Snooker.")
st.write("4.Playing Carroms.")

st.subheader("PERSONAL PROFILE:-")
column3,column4,empty_column,empty_column2 = st.columns(4)

with column3:
    st.write("Name            :- ")
    st.write("Father's Name   :- ")
    st.write("Date of Birth   :- ")
    st.write("Gender          :- ")
    st.write("Marital Status  :- ")
    st.write("Nationality     :- ")
    st.write("Languages Known :- ")

with column4:
    st.write(" Vinay Goud Palusa")
    st.write(" Ranganayakulu Palusa")
    st.write(" 3rd May 1988")
    st.write(" Male")
    st.write(" Married")
    st.write(" Indian")
    st.write(" English, Hindi and Telugu")
