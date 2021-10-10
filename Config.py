import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
else:
    # Fill the Values 
    API_ID = "2774426"
    API_HASH = "e583437e972d1f801824a41d7aff65e7"
    BOT_TOKEN = "2039163053:AAH_vRb_T2Hg0-RR_9mNWdthPvVMkwUnOmI"
