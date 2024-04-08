from random import randint

db = {
  "users": [
    {
      "id": "1",
      "name": "Leoniel Nacman",
      "type": "Transaction 1"
    },
    {
      "id": "2",
      "name": "Leoniel Garin",
      "type": "Transaction 2"
    },
    {
      "id": "3",
      "name": "Leoniel Ragonot",
      "type": "Transaction 3"
    },
    {
      "id": "4",
      "name": "Leoniel",
      "type": "Transaction 4"
    },
    {
      "id": "5",
      "name": "John Doe",
      "type": "Transaction 1"
    },
    {
      "id": "6",
      "name": "Jane Smith",
      "type": "Transaction 2"
    },
    {
      "id": "7",
      "name": "Michael Johnson",
      "type": "Transaction 3"
    },
    {
      "id": "8",
      "name": "Emily Brown",
      "type": "Transaction 4"
    },
    {
      "id": "9",
      "name": "David Martinez",
      "type": "Transaction 1"
    },
    {
      "id": "10",
      "name": "Sarah Williams",
      "type": "Transaction 2"
    },
    {
      "id": "11",
      "name": "Alex Lee",
      "type": "Transaction 3"
    },
    {
      "id": "12",
      "name": "Olivia Nguyen",
      "type": "Transaction 4"
    },
    {
      "id": "13",
      "name": "Daniel Brown",
      "type": "Transaction 1"
    },
    {
      "id": "14",
      "name": "Sophia Garcia",
      "type": "Transaction 2"
    },
    {
      "id": "15",
      "name": "James Wilson",
      "type": "Transaction 3"
    }
  ]
}


def get_users():
	global db
	return db['users']

def get_user(user_id):
    global db
    for user in db['users']:
        if user['id'] == user_id:
            return user
    return None

def update_user(user_id, name, type):
  global db
  for user in db['users']:
    if user['id'] == user_id:
      user['name'] = name
      user['type'] = type
      return user
  return None

def add_user(name, type):
	global db
	user = {
		'id': str(randint(1000, 9999)),
		'name': name,
		'type': type,
	}
	db['users'].insert(0, user)
	return user

def set_user(id, name, type):
	global db
	for user in db['users']:
		if user['id'] == id:
			user['name'] = name
			user['type'] = type
			return user
	return None

def delete_user(id):
	global db
	db['users'] = [ user for user in db['users'] if user['id'] != id ]