import joblib

# Load the trained model
Model = joblib.load("./MyModel")


def Predict():
    # Collect input values from the user
    age = int(input("Enter value for age: "))
    sex = int(input("Enter value for sex (1 = male, 0 = female): "))
    cp = int(input("Enter value for cp (chest pain type): "))
    trestbps = int(input("Enter value for trestbps (resting blood pressure in mm Hg): "))
    chol = int(input("Enter value for chol (serum cholesterol in mg/dl): "))
    fbs = int(input("Enter value for fbs (fasting blood sugar > 120 mg/dl, 1 = true, 0 = false): "))
    restecg = int(input("Enter value for restecg (resting electrocardiographic results): "))
    thalach = int(input("Enter value for thalach (maximum heart rate achieved): "))
    exang = int(input("Enter value for exang (exercise induced angina, 1 = yes, 0 = no): "))
    oldpeak = float(input("Enter value for oldpeak (ST depression induced by exercise relative to rest): "))
    slope = int(input("Enter value for slope (the slope of the peak exercise ST segment): "))
    ca = int(input("Enter value for ca (number of major vessels (0-3) colored by fluoroscopy): "))
    thal = int(input("Enter value for thal (thalassemia): "))

    # Predict the outcome using the trained model
    Result = Model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    # Interpret and print the result
    if Result == 0:
        print("You Are Safe")
    else:
        print("Kabhi Alvida Na Kehna")


Predict()
