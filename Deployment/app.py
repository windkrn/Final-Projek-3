from re import split
import flask
import numpy as np
import pickle


model = pickle.load(open("model/model_rf.pkl", "rb"))
app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))

if __name__ == '__main__':
    app.run()


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
     # ngambil nilai inputan dari form dibikin bentuk dict
    features = dict(flask.request.form)

    # karena fitur name itu kategori jadi kita encode
    features_sex = []
    for i in range(1, 2):
        if i == int(features['sex']):
            features_sex.append(1)
        else:
            features_sex.append(0)

    features_smoking = []
    for i in range(1, 2):
        if i == int(features['smoking']):
            features_smoking.append(1)
        else:
            features_smoking.append(0)

    features_diabetes = []
    for i in range(1, 2):
        if i == int(features['diabetes']):
            features_diabetes.append(1)
        else:
            features_diabetes.append(0)

    features_anaemia = []
    for i in range(1, 2):
        if i == int(features['anaemia']):
            features_anaemia.append(1)
        else:
            features_anaemia.append(0)

    features_high_blood_pressure = []
    for i in range(1, 2):
        if i == int(features['high_blood_pressure']):
            features_high_blood_pressure.append(1)
        else:
            features_high_blood_pressure.append(0)

    int_features =  [float(features['age']),
                    float(features['creatinine_phosphokinase']),
                    float(features['ejection_fraction']),
                    float(features['serum_creatinine']),
                    float(features['serum_sodium']),
                    float(features['platelets']),
                    float(features['time']),
                    ] + features_sex + features_smoking + features_diabetes + features_anaemia  + features_high_blood_pressure



    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = {0: 'Survived', 1: 'Not Survived'}

    return flask.render_template('main.html', prediction_text='Prediction : {}'.format(output[prediction[0]]))

if __name__ == "__main__":
    app.run(debug=True)