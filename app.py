from redis import Redis
from eve import Eve

from auth import MyBasicAuth
from validation import MyValidator
from callbacks import add_age, inject_signature

app = Eve(validator=MyValidator, redis=Redis(), auth=MyBasicAuth)

@app.route('/hello')
def hello():
    return 'Hello, Jesus!'
# attach a callback function to GET requests.
app.on_fetched_item += inject_signature
# attach a callback function to POST requests.
app.on_insert += add_age
