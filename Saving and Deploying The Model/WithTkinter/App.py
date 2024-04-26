from tkinter import *
import  joblib
model = joblib.load("MyLinerModel")
def Predict():
   
    condition = int(entries[0].get())
    bathrooms = int(entries[1].get())
    bedrooms = int(entries[2].get())
    sqft_living = int(entries[3].get())

    print("Condition:", condition)
    print("Bathrooms:", bathrooms)
    print("Bedrooms:", bedrooms)
    print("Sqft Living:", sqft_living)

    Answer = "Answer:- " + str(model.predict([[condition, bathrooms, bedrooms, sqft_living]]))
    print(Answer)

    L = Label(text=Answer)
    L.pack()



root = Tk()
root.geometry("400x400")
root.title("My ML App")

labels = ["Condition", "Bathrooms", "Bedrooms", "Sqft Living"]
entries = []

for label_text in labels:
    label = Label(root, text=label_text)
    label.pack()

    entry = Entry(root)
    entry.pack()

    entries.append(entry)

B1 = Button(text="Predict", command=Predict)
B1.pack()

root.mainloop()
