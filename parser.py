import re

OBJECTS = {}

class Card(object):
    def __init__(self, id, **kwargs):
        self.id = id
        for key, value in kwargs:
            setattr(self, key, value)

def parse_power(string):
    string = ''.join(string.split(') - ')[1:])
    if 'TAG_CHANGE' in string:
        kwargs = string.split(' ')
        entity, tag, value = None, None, None
        for kwarg in kwargs:
            if 'Entity=' in kwarg:
                entity = get_card(string)
                if not entity:
                    entity = kwarg.split('=')[1]
            elif 'tag=' in kwarg:
                tag = kwarg.split('=')[1]
            elif 'value=' in kwarg:
                value = kwarg.split('=')[1]
        if entity:
            print 'POWER:', entity, tag, value, string

def get_card(string):
    cards = re.findall('\[.*\]', string)
    if cards:
        return cards[0]
    return ''

def parse_zone(string):
    string = ''.join(string.split(') - ')[1:])
    if 'TRANSITIONING' in string:
        card = get_card(string)
        print card

with open('/Users/nilesnelson/Library/Logs/Unity/Player.log') as f:
    while f.read():
        pass
    while True:
        line = f.readline()
        if line:
            striped_line = line.rstrip(' ').rstrip('\n')
            if striped_line:
                if '[Zone]' in striped_line:
                    parse_zone(striped_line)
                elif '[Power]' in striped_line:
                    parse_power(striped_line)
