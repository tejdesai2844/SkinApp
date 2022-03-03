import hashlib
import re

def make_hashes(password):   
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()

# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(FirstName TEXT,LastName TEXT,Mobile TEXT,Email TEXT,password TEXT,Cpassword TEXT)')
def add_userdata(FirstName,LastName,Mobile,Email,password,Cpassword):
    c.execute('INSERT INTO userstable(FirstName,LastName,Mobile,Email,password,Cpassword) VALUES (?,?,?,?,?,?)',(FirstName,LastName,Mobile,Email,password,Cpassword))
    conn.commit()
def login_user(Email,password):
    c.execute('SELECT * FROM userstable WHERE Email =? AND password = ?',(Email,password))
    data = c.fetchall()
    return data




# title
st.title('Skin-Cancer Classfication App')
menu1 = ["Home","Login", "Signup"]
choice1 = st.sidebar.selectbox("menu",menu1)
if choice1=="Home":
    #html
    testp="<p style='text-align: center;'>Skin cancer is the most common and prevalent type of cancer over the world. More precise analysis needs to be performed to identify the category of the skin lesion because skin lesions look quite similar to each other. Early screening and detection of skin cancer is the most hopeful sign of making a full recovery. Our Aim to make a system that detect types of skin cancer along with stages of cancer as fast as possible for effective treatment, which cause in increasing the survival rate from Skin cancer</p>"
    st.markdown(testp,unsafe_allow_html=True)
    image=Image.open('home.jpeg')
    st.image(image)
if choice1=="Login":
    st.subheader("Login Section")
    Email=st.sidebar.text_input('Email')
    password=st.sidebar.text_input('Password',type='password')
    b1=st.sidebar.checkbox("login")
    if b1:
        #Validation
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, Email):
            create_usertable()
            hashed_pswd = make_hashes(password)
            result = login_user(Email,check_hashes(password,hashed_pswd))
            if result:
                imgur=st.file_uploader("Browse Skin Image")
                image=Image.open(imgur)
                st.image(image)
                menu2 = ["Gaussian Filter","Average Filter", "Median Filter"]
                choice2 = st.selectbox("Select Filter",menu2)
                menu3 = ["Color","Texture", "Hybrid"]
                choice3 = st.selectbox("Select Feature",menu3)
                menu4 = ["SVM (Support Vector Machine)","KNN (K-Nearest Neighbour)", "RF (Random Forest)","DT (Decision Tree)"]
                choice4 = st.selectbox("Select Method",menu4)
                b2=st.button("Predict")
                if b2:
                   st.success("The Skin Cancer Type is= ")
            else:
                st.warning("Incorrect Email/Password")       
        else:
            st.warning("Not Valid Email")

if choice1=="Signup":
    st.subheader("Signup Section")
    FirstName=st.text_input('First Name')
    LastName=st.text_input('Last Name')
    Mobile=st.text_input('Contact No')
    Email=st.text_input('Email')
    new_password=st.text_input('Password',type='password')
    Cpassword=st.text_input('Confirm Password',type='password')
    b4=st.button("Sign up")
    if b4:
        if new_password==Cpassword:
            #Validation
            pattern=re.compile("(0|91)?[7-9][0-9]{9}")
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if (pattern.match(Mobile)):
                if re.fullmatch(regex, Email):
                    create_usertable()
                    add_userdata(FirstName,LastName,Mobile,Email,make_hashes(new_password),make_hashes(Cpassword))
                    st.success("You have successfully created a valid Account")
                    st.info("Go to Login Menu to login")
                else:
                    st.warning("Not Valid Email")               
            else:
                st.warning("Not Valid Mobile Number")
        else:
            st.warning("Password Does not Match")
            
            
            
            
            
            
