# X_DOMAINS = ['example.com','mysite.org','']
X_DOMAINS = '*'

MONGO_URI = 'mongodb://localhost:27017/eve-course'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
schema = {
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 30,
        },
    'lastname': {
        'type': 'string',
        'maxlength': 50,
        'required': True,
        'unique': True,
    },
    'born': {'type': 'datetime'},
    'age': {'readonly': True},
    'role': {
        'type': 'list',
        'allowed': ['author', 'contributor', 'copy'],
        'default': ['author']
    },
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string', 'required': True}
        }
    }
}

DOMAIN = {
    'people': {
        'schema': schema
    },
    'works': {
        'resource_methods': ['GET'],
        'item_methods': ['GET']
    }

}
