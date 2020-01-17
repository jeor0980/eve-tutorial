from app import PeopleAuth
# X_DOMAINS = ['example.com','mysite.org','']
X_DOMAINS = '*'

MONGO_URI = 'mongodb://localhost:27017/eve-course'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# DATE_FORMAT = '%d $b %Y'
# QUERY_WHERE = 'find'
# QUERY_SORT = 'orderby'
# Disable filters
# ALLOWED_FILTERS = []
# SORTING = False
# MONGO_QUERY_BLACKLIST = []
# QUERY_PAGE = 'section'
# MAX_QUERY_RESULT = 'max_results'
# PAGINATION_DEFAULT = 25
# PAGINATION_LIMIT = 50
# OPTIMIZE_PAGINATION_FOR_SPEED = True
# PROJECTION = False
# QUERY_PROJECTION = 'fields'
# IF_MATCH = False
# ENFORCE_IF_MATCH = False
# ETAG = 'etag'
# HATEOAS = True
# LINKS = 'links'

# num of req, secs
RATE_LIMIT_GET = (1, 60)

JSON_SORT_KEYS = True

# PAGINATION = False

schema = {
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
}

DOMAIN = {
    'people': {
        'authentication': PeopleAuth,
        'datasource': {'projection': {'lastname': 0}},
        'projection': True,
        'pagination': True,
        # 'hateoas': False,
        'schema': schema
    },
    'works': {
        'resource_methods': ['GET'],
        'item_methods': ['GET']
    }

}
