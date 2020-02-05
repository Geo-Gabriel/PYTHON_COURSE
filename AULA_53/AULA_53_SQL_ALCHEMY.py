# ENTENDENDO O MODELO ORM

# --- INSTALAÇÃO DO FRAMEWORK
# --- PIP3 INSTALL SQLALCHEMY

# --- CONECTOR DO MYSQL
# --- INSTALAÇÃO DO CONECTOR DO MYSQL
# --- pip3 install mysql-connector-python

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class NinjasModel(base):
    __tablname__ = 'Ninjas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    jutsu = db.Column(db.String(255))
    chakra = db.Column(db.String(255))

connect = db.create_engine()