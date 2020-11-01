from flask_api import app, db
from flask_api.models import Patient, patient_schema, patients_schema
from flask import jsonify, request

#Import JsonWebToken(JWT)
import jwt

@app.route('/patients/create', methods = ['POST'])
def create_patient():
    name = request.json['full_name']
    gender = request.json['gender']
    address = request.json['address']
    ssn = request.json['ssn']
    blood_type = request.json['blood_type']
    email = request.json['email']

    patient = Patient(name,gender,address,ssn,blood_type,email)
    results = patient_schema.dump(patient)
    return jsonify(results)

@app.route('/patients', methods = ['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify(patients_schema.dump(patients))

@app.route('/getkey', methods = ['GET'])
def get_key():
    token = jwt.encode({'public_id':'10002','email':'joel@codingtemple.com'},app.config['SECRET_KEY'])
    return jsonify({'token': token.decode('utf-8')})

@app.route('/patients/<id>', methods = ['GET'])
def get_patient(id):
    patient = Patient.query.get(id)
    results = patient_schema.dump(patient)
    return jsonify(results)

@app.route('/patients/<id>', methods = ['POST', 'PUT'])
def update_patient(id):
    patient = Patient.query.get(id)
    
    patient.name = request.json['full_name']
    patient.gender = request.json['gender']
    patient.address = request.json['address']
    patient.ssn = request.json['ssn']
    patient.blood_type = request.json['blood_type']
    patient.email = request.json['email']

    db.session.commit()

    return patient_schema.jsonify(patient)

@app.route('/patients/delete/<id>', methods = ['DELETE'])
def delete_patient(id):
    patient = Patient.query.get(int(id))
    db.session.delete(patient)
    db.session.commit()
    result = patient_schema.dump(patient)
    return jsonify(result)