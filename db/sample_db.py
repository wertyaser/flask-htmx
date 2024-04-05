from random import randint

db = {
  "users": [
    {
      "id": "1",
      "name": "Leoniel Nacman",
      "type": "Transaction 1",
    },
    {
      "id": "2",
      "name": "Leoniel Garin",
      "type": "Transaction 2",
    },
    {
      "id": "3",
      "name": "Leoniel Ragonot",
      "type": "Transaction 3",
    },
    {
      "id": "4",
      "name": "Leoniel",
      "type": "Transaction 4",
    },
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