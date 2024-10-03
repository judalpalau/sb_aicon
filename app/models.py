from mongoengine import Document, EmbeddedDocument, fields

class EmbeddedUser(EmbeddedDocument):
    id = fields.ObjectIdField()
    name = fields.StringField(max_length=150)
    email = fields.EmailField(null = True)
    

class EmbeddeUpdate(EmbeddedDocument):
    id = fields.ObjectIdField()
    name = fields.StringField(max_length=150)
    email = fields.EmailField(null = True)
    date = fields.DateTimeField()

class EmbeddedFormat(EmbeddedDocument):
   quantity = fields.IntField(min_value = 1)
   format = fields.StringField(default = 'Blister') 

####################################

class FieldsDefaultsAbstracts(Document):
    created_by = fields.EmbeddedDocumentField(EmbeddeUpdate, nulll = True)
    updated_by = fields.EmbeddedDocumentField(EmbeddeUpdate, nulll = True)
    active = fields.BooleanField(default=True, nulll = True)

    # Meta abstract
    meta = { 'abstract': True }

class Bill(FieldsDefaultsAbstracts):
    seller_name = fields.StringField(max_length=150)
    email = fields.EmailField(unique=True)
    phone = fields.StringField(max_length=15)
    country = fields.StringField(max_length=100, blank=True, null=True)

    seller_name = fields.StringField(max_length=150, default = "Unknown")
    seller_id = fields.StringField(max_length=13, default = "Unknown")
    seller_doc_type = fields.StringField(max_length=3, default = "Unknown")
    buyer_name = fields.StringField(max_length=150, default = "Unknown")
    buyer_id = fields.StringField(max_length=13, default = "Unknown")
    buyer_doc_type = fields.StringField(max_length=3, default = "Unknown")
    medicine_name = fields.StringField(max_length=150, default = "Unknown")
    medicine_quantity = fields.IntField(min_value = 1, default = 1)
    medicine_unit_price = fields.DecimalField(min_value=0, precision=2)
    medicine_total_price = fields.DecimalField(min_value=0, precision=2)
    bill_total_price = fields.DecimalField(min_value=0, precision=2)
    embedding = fields.ListField()
    price_anomaly = fields.BooleanField(default=False)

    # Meta collection name
    meta = { 'collection': f'embeddings' }

class MedicineValues(FieldsDefaultsAbstracts):
   brand = fields.StringField(max_length=150)
   name = fields.StringField(max_length=150)
   atc = fields.StringField(max_length=150)
   min_price = fields.DecimalField(min_value=0, precision=2)
   max_price = fields.DecimalField(min_value=0, precision=2)
   avg_price = fields.DecimalField(min_value=0, precision=2)
   embedding = fields.ListField()
      
   # Meta collection name
   meta = {
        'collection': f'medicine_values',
        'indexes': [
            "$name"
           ]
        }

