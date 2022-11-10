import unittest
import os

from buissnes.Database.Builder import DBConnector


class TestConnection(unittest.TestCase):

    def test(self):
        pass



class TestUserVocabDatabase(unittest.TestCase):
    # Test the user vocab collection database

    def setUp(self):
        # create database
        self.db = DBConnector ('test_vocab.db')

        # create necessary tables
        msg = '''CREATE TABLE IF NOT EXISTS users(user_id integer primary key, username text, password text) '''
        self.db.c.execute(msg)
        self.db.conn.commit()

        msg = '''CREATE TABLE IF NOT EXISTS vocab_lists(list_id integer primary key, list_name text, list_number int, tags text, list_user_id integer, FOREIGN KEY(list_user_id) REFERENCES users(user_id) ) '''
        self.db.c.execute(msg)
        self.db.conn.commit()

        msg = '''CREATE TABLE IF NOT EXISTS words(word_id integer primary key, word text, meaning text, example_sentence text, tags text, word_list_id integer, FOREIGN KEY(word_list_id) REFERENCES vocab_lists(list_id)) '''
        self.db.c.execute(msg)
        self.db.conn.commit()

    def tearDown(self):
        if self.db.conn:
            self.db.conn.close()
        os.remove("test_vocab.db")