import pickle
import sys


class Mary:

    def __init__(self):
        try:
            self.messages = dict()
            self.deserialize_messages()

        except FileNotFoundError:
            pass

    def deserialize_messages(self):
            with open('messages', 'rb') as f:
                self.messages = pickle.load(f)

    def serialize_messages(self):
        try:
            with open('messages', 'wb+') as m:
                pickle.dump(self.messages, m)

        except EOFError:
            pass

    def list_messages(self):
        for person in self.messages.keys():
            print('--------------------{}--------------------'.format(person))
            i = 1

            for message in self.messages[person]:
                print('    {}: {}'.format(i, message))
                i += 1

            print('\n')


if __name__ == '__main__':
    mary = Mary()
    try:
        message = sys.argv[1]
        mary.messages['mary'].append(message)

    except IndexError:
        mary.list_messages()
        sys.exit()

    except KeyError:
        mary.messages['mary'] = list()
        mary.messages['mary'].append(message)

    mary.serialize_messages()
