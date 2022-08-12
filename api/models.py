import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from config import GlobalConfig
from sqlalchemy.ext.automap import automap_base
import os


"""
Engine and metadata setup
"""
db_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), GlobalConfig.config( "GLOBAL.db_name")))
engine = db.create_engine("sqlite:////{}".format(db_file_name))

metadata = db.MetaData(engine)
metadata.reflect(engine, only=[GlobalConfig.config("GLOBAL.db_table_name")])
Base = automap_base(metadata=metadata)


class Employees(Base):
    __tablename__  = GlobalConfig.config("GLOBAL.db_table_name")
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String)
    
    def __repr__(self):
        return "<Employee {} is a {}>".format(self.id, self.gender)

    def export_data(self):
        return {
            'id' : self.id,
            'gender' : self.gender
        }

    
Base.prepare()
def loadSession():
    Session = sessionmaker(engine)
    session = Session()
    return session
