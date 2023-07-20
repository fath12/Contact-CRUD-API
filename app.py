from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema

# Create Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost:3306/contact"
db = SQLAlchemy(app)

# Model
class Contact(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20))
    lastName = db.Column(db.String(20))
    numberPhone = db.Column(db.String(20))
    address = db.Column(db.String(100))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, firstName, lastName, numberPhone, address):
        self.firstName = firstName
        self.lastName = lastName
        self.numberPhone = numberPhone
        self.address = address

    def __repr__(self):
        return f"{self.firstName} {self.lastName}"

# Create all database tables
with app.app_context():
    db.create_all()

# Schema
class ContactSchema(SQLAlchemySchema):
    class Meta:
        model = Contact
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    firstName = fields.String(required=True)
    lastName = fields.String(required=True)
    numberPhone = fields.String(required=True)
    address = fields.String(required=True)

# POST endpoint - Create a contact
@app.route('/api/v1/contact', methods=['POST'])
def create_contact():
    data = request.get_json()
    contact_schema = ContactSchema()
    contact = contact_schema.load(data)

    # Create a new instance of the Contact model using the loaded data
    new_contact = Contact(**contact)
    db.session.add(new_contact)
    db.session.commit()

    result = contact_schema.dump(new_contact)
    return make_response(jsonify({"contact": result}), 200)

# GET endpoint - Get all contacts
@app.route('/api/v1/contact', methods=['GET'])
def get_all_contacts():
    get_contacts = Contact.query.all()
    contact_schema = ContactSchema(many=True)
    contacts = contact_schema.dump(get_contacts)
    return make_response(jsonify({"contacts": contacts}))

# GET endpoint - Get a specific contact by ID
@app.route('/api/v1/contact/<id>', methods=['GET'])
def get_contact_by_id(id):
    get_contact = Contact.query.get(id)
    if not get_contact:
        return make_response(jsonify({"message": "Contact not found"}), 404)
    contact_schema = ContactSchema()
    contact = contact_schema.dump(get_contact)
    return make_response(jsonify({"contact": contact}), 200)

# PUT endpoint - Update a contact by ID
@app.route('/api/v1/contact/<id>', methods=['PUT'])
def update_contact_by_id(id):
    data = request.get_json()
    get_contact = Contact.query.get(id)
    if not get_contact:
        return make_response(jsonify({"message": "Contact not found"}), 404)
    if data.get('firstName'):
        get_contact.firstName = data['firstName']
    if data.get('lastName'):
        get_contact.lastName = data['lastName']
    if data.get('numberPhone'):
        get_contact.numberPhone = data['numberPhone']
    if data.get('address'):
        get_contact.address = data['address']
    db.session.add(get_contact)
    db.session.commit()
    contact_schema = ContactSchema()
    contact = contact_schema.dump(get_contact)
    return make_response(jsonify({"contact": contact}), 200)

# DELETE endpoint - Delete a contact by ID
@app.route('/api/v1/contact/<id>', methods=['DELETE'])
def delete_contact_by_id(id):
    get_contact = Contact.query.get(id)
    if not get_contact:
        return make_response(jsonify({"message": "Contact not found"}), 404)
    db.session.delete(get_contact)
    db.session.commit()
    return make_response(jsonify({"message": "Contact deleted successfully"}), 204)

if __name__ == "__main__":
    app.run(debug=True)
