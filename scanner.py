import rfid
import actions

import csv

# global to store the map of uids to actions
uid_map = {}


def get_action(uid):
    # getattr will return function in the actions module
    return getattr(actions, uid_map[uid])


def loop():
    while True:
        print("Waiting for a Mifare tag...")
        uid = rfid.read_card()

        # format uid for pretty printing
        formatted = ''.join('{:02x}'.format(x) for x in uid)
        print("Read a card with UID: {}".format(formatted))

        # perform what is mapped to that uid in the csv file
        action = get_action(formatted)
        action() # call action

        print('\n')


def parse_csv_map(reader):
    global uid_map
    for row in reader:
        uid_map[row[0]] = row[1]


if __name__ == '__main__':
    with open('map.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        parse_csv_map(reader)

    loop()
    
