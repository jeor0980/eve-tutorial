from app import MyBasicAuth

people = {
    'authentication': MyBasicAuth,
    'datasource': {'projection': {'lastname': 0}},
    'projection': True,
    'pagination': True,
    # 'hateoas': False,
    'schema': {
        # 'allowed_filters': ['lastname'],
        # 'sorting': False,
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
        'middlename': {
            'dependencies': ['firstname', 'lastname'],
        },
        'born': {'type': 'datetime'},
        'age': {
            'type': 'integer',
            'isodd': True
        },
        'role': {
            'type': 'list',
            'allowed': ['author', 'contributor', 'copy'],
            'default': ['author']
        },
        'location': {
            'type': 'dict',
            'required': False,
            'schema': {
                'address': {'type': 'string'},
                'city': {'type': 'string', 'required': True}
            }
        },
        'email': {'type': 'email'}
    },
}
