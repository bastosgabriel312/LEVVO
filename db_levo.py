import email
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, insert, delete
import pymysql
from sqlalchemy.ext.declarative import declarative_base
 
#base para criação de engine
Base = declarative_base()
 
#Conectanto e criando a máquina para utilizar o sql alchemy
engine = create_engine('mysql+pymysql://b74s0om2wm3diiii:kaucriymr5qrj7oa@uyu7j8yohcwo35j3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/vxaohtuqm8mtxuxc')
Session = sessionmaker(bind=engine)
db_session = Session()
 
class Cliente(Base):
   __tablename__ = 'tb_cliente'
   id = Column(Integer, primary_key=True)
   nome = Column(String(100))
   email = Column(String(50))
   senha = Column(String(50))
   telefone = Column(String(20))
 
class Entregador(Base):
   __tablename__ = 'tb_entregador'
   id = Column(Integer, primary_key=True)
   nome = Column(String(100))
   email = Column(String(50))
   senha = Column(String(50))
   telefone = Column(String(20))
   placa = Column(String(10))
 
class Entrega(Base):
   __tablename__ = 'tb_entrega'
   id = Column(Integer, primary_key=True)
   descricao = Column(String(200))
   id_endereco_coleta = Column(Integer)
   id_endereco_final = Column(Integer)
 
########################## 
class Endereco(Base):
   __tablename__ = 'tb_endereco'
   id = Column(Integer, primary_key=True)
   rua = Column(String(200))
   numero = Column(Integer)
   complemento = Column(String(200))
   CEP = Column(String(10))
   id_bairro = Column(Integer)
 
#Realiza a criação das tabelas solicitadas
Base.metadata.create_all(engine)
 
#Insere dados do usuário na tabela usuários
# cliente = Cliente(nome="Vinicius",email="vinicius@gmail.com",senha="vinicius123",telefone="11991677867")
 
# db_session.add(cliente)
# db_session.commit()
 
#Select de dados dados
for cliente in db_session.query(Cliente).filter_by(nome="Vinicius"):
   print(cliente.nome)