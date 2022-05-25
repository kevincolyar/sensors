#!/usr/bin/env python3
from db.base import Base

class Errors(Base):
    def __init__(self, db):
        super(Errors, self).__init__(db, 'errors')
