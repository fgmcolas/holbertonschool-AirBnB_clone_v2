#!/usr/bin/python3
""" Module for testing DBStorage"""
import unittest
from models.engine.db_storage import DBStorage
from models import storage
import os
STORAGE_ENV = os.getenv("HBNB_TYPE_STORAGE")


@unittest.skipIf(STORAGE_ENV != "db", "no testing with db storage")
class TestDBStorage(unittest.TestCase):
    """ Class to test the DBStoage """

    def setUp(self):
        del_list = []
        for key in storage.all().keys():
            del_list.append(key)
        for key in del_list:
            storage._DBStorage__session.delete(storage.all()[key])
            storage._DBStorage__session.commit()

    def test_storage_instance(self):
        """ """
        self.assertEqual(type(storage), TestDBStorage)
