import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    username = Column(String(250), unique=True, nullable=False)

class Planeta(Base):
    __tablename__ = 'planeta'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer, nullable=False)

class Personaje(Base):
    __tablename__ = 'personaje'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    planeta_id = Column(Integer, ForeignKey("planeta.id"))
    planeta = relationship(Planeta)
    
class Vehiculo(Base):
    __tablename__ = 'vehiculo'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    max_atmospheric_speed = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)

class Favorito(Base):
    __tablename__ = 'favorito'
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    usuaris = relationship(Usuario)
    personaje_id = Column(Integer, ForeignKey("personaje.id"))
    personaje = relationship(Personaje)
    planeta_id = Column(Integer, ForeignKey("planeta.id"))
    planeta = relationship(Planeta)
    vehiculo_id = Column(Integer, ForeignKey("vehiculo.id"))
    vehiculo = relationship(Vehiculo)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
