import joblib
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/farmers_database'
db = SQLAlchemy(app)

class FarmersInquiry(db.Model):
    __tablename__ = 'farmers_inquiry'
    serial_number = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    pin = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    type_of_farming = db.Column(db.String(255), nullable=False)
    contact_method = db.Column(db.String(100), nullable=False)
    query = db.Column(db.Text, nullable=False)

class FormSubmit(db.Model):
    __tablename__ = 'form_submissions'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    rating=db.Column(db.Integer,nullable=False)
    message = db.Column(db.Text, nullable=False)


# Load the trained model
crop_model = joblib.load('crop_recommendation_model.joblib')
plant_disease_model = load_model('plant_disease_model.h5')
plant_disease_model1 = load_model('plant_disease_model (2).h5')


labels = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry_(including_sour)___healthy', 'Cherry_(including_sour)___Powdery_mildew',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
    'Corn_(maize)___healthy', 'Corn_(maize)___Northern_Leaf_Blight', 'Grape___Black_rot', 
    'Grape___Esca_(Black_Measles)', 'Grape___healthy', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
    'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 
    'Potato___healthy', 'Potato___Late_blight', 'Raspberry___healthy', 'Soybean___healthy',
    'Squash___Powdery_mildew', 'Strawberry___healthy', 'Strawberry___Leaf_scorch', 
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___healthy', 'Tomato___Late_blight', 
    'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
    'Tomato___Target_Spot', 'Tomato___Tomato_mosaic_virus', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus'
]


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home1():
    return render_template('home.html')

@app.route('/test')
def testing():
    return render_template('testimonial.html')

@app.route('/Recommend')
def recommend():
    return render_template('Index.html')

@app.route('/form', methods=["POST"])
def brain():
    try:
        Nitrogen = float(request.form['Nitrogen'])
        Phosphorus = float(request.form['Phosphorus'])
        Potassium = float(request.form['Potassium'])
        Temperature = float(request.form['Temperature'])
        Humidity = float(request.form['Humidity'])
        Ph = float(request.form['ph'])
        Rainfall = float(request.form['Rainfall'])
        
        if 0 < Ph <= 14 and 0 <= Temperature < 100 and 0 <= Humidity:
            values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]
            arr = [values]
            prediction = crop_model.predict(arr)[0]
            return render_template('prediction.html', prediction=str(prediction))
        else:
            return "Invalid input values. Please check the input ranges."
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route('/Predict')
def prediction():
    return render_template('plant_disease_prediction_form.html')

@app.route('/predict', methods=["GET", "POST"])
def plant_disease_prediction():
    if request.method == 'POST':
        try:
            uploaded_file = request.files['file']

            if uploaded_file.filename != '':
                temp_path = 'temp_image.jpg'
                uploaded_file.save(temp_path)

                img = image.load_img(temp_path, target_size=(128, 128))
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                result = plant_disease_model.predict(img_array)
                predicted_label = labels[np.argmax(result)]

                return render_template('plant_disease_prediction_result.html', prediction=predicted_label)
            
            else:
                return "No file uploaded. Please choose an image for prediction."
            
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template('plant_disease_prediction_form.html')

@app.route('/query')
def openquery():
    return render_template('queryform.html')


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        location = request.form.get('location')
        pin = int(request.form.get('pin'))
        state = request.form.get('state')
        phone = request.form.get('phone')
        type_of_farming = request.form.get('typeOfFarming')
        contact_method = request.form.get('contactMethod')
        query = request.form.get('query')

        new_entry = FarmersInquiry(
            name=name,
            age=age,
            location=location,
            pin=pin,
            state=state,
            phone=phone,
            type_of_farming=type_of_farming,
            contact_method=contact_method,
            query=query
        )

        db.session.add(new_entry)
        db.session.commit()
        last_inserted_serial_number = new_entry.serial_number

        alert_message = f"Query received successfully! Your question is {last_inserted_serial_number} in line."

        return render_template('queryform.html', alert_message=alert_message)

    # Render the initial contact page with an empty form
    return render_template('queryform.html', alert_message=None)

@app.route("/formsubmit", methods=['GET', 'POST'], endpoint='formsubmit')
def review():
    if request.method == 'POST':
        name = request.form.get('name1')
        rating = int(request.form.get('rating'))
        phone = request.form.get('phone1')
        message = request.form.get('message')

        new_entry = FormSubmit(
            name=name,
            phone=phone,
            rating=rating,
            message=message
        )

        db.session.add(new_entry)
        db.session.commit()

        alert_message = f"Review Submitted!"

        return render_template('home.html', alert_message=alert_message)

    return render_template('home.html', alert_message=None)

@app.route("/testimonial", methods=['GET'])
def testimonial():
    testimonials = FormSubmit.query.all()
    return render_template('testimonial.html', testimonials=testimonials)

@app.route("/policies")
def policies():
    return render_template('terms.html')

@app.route("/knowmore")
def knowmore():
    return render_template('know.html')

if __name__ == '__main__':
    app.run(debug=True)
