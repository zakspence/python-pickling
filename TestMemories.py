import unittest
from margaret import *
from mary import *


class TestMemories(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global margaret
        global mary
        self.margaret = Margaret()
        self.mary = Mary()
        margaret = self.margaret
        mary = self.mary

    def test_deserialize_memories(self):
        mary.deserialize_messages()
        mary_messages = mary.messages
        margaret.deserialize_messages()
        margaret_messages = margaret.messages

        self.assertIn('Hello', mary_messages['margaret'])
        self.assertIn('Goodbye', margaret_messages['mary'])

    def test_serialize_messages(self):
        mary.serialize_messages({'margaret': ['Hello'], 'mary': ['Goodbye']})

        try:
            with open('messages', 'rb') as m:
                messages = pickle.load(m)
                self.assertEqual(messages, {'margaret': ['Hello'],
                                            'mary': ['Goodbye']})

        except EOFError:
            pass
