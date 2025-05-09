# 1. Implemente os métodos create, read, update e delete do
# módulo crud.py.

import pandas as pd
from relacoes import Livro
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
import os

from crud_funcional import CRUD
from dotenv import load_dotenv
from relacoes import Livro
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

Base = declarative_base()


class Livro(Base):
    __tablename__ = "Livro"

    isbn = Column(String(13), primary_key=True)
    titulo = Column(String(255), nullable=False)
    autor = Column(String(255), nullable=False)
    ano_publicacao = Column(Integer, nullable=False)
    genero = Column(String(100), nullable=True)

class CRUD:
    def __init__(self, session: Session):
        self.__session = session

    def create(self, isbn, titulo, autor, ano_publicacao, genero=None):
        # TODO: recebe os parâmetros do livro e cria o registro no banco de dados
        create table Livro (
            isbn varchar(13) primary key,
            titulo varchar(255) not null,
            autor varchar(255) not null,
            ano_publicacao int not null check (ano_publicacao > 0),
            genero varchar(100)
            );
        

    def read(self, isbn=None):
        # TODO: retorna um livro específico pelo ISBN
        select * from Livro 
        where isbn = isbn;


    def update(self, isbn, titulo=None, autor=None, ano_publicacao=None, genero=None):
        # TODO: atualiza os valores dos parâmetros de um livro específico pelo ISBN
         update livros
         set titulo = titulo and autor = autor and ano_publicacao = ano_publicacao and genero = genero
         where isbn = isbn

        
    def delete(self, isbn):
        # TODO: delete um livro específico pelo ISBN
        delete from Livro
        where isbn = isbn

