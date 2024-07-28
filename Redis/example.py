import redis
#setup ei vaan toimi, mutta perjaatteessa näin
r = redis.Redis(password='uIGJJuzNnLKvyebVqSN0fmN9lglR4gub', host='redis-18509.c9.us-east--1-4.ec2-cloud.redilabs.com', port=18509, decode_responses=True)
r.set('name', 'test')
print(r.get('name'))

#sorting
HSET user:bob

cache.get()
#django
#from django.core.cache import cache
#need backend and location in settings.py config

#searching
print(Customer.find(Customer.address.city == "pittsburg"). first())

#json format example
class Address(EmbeddedJsonModel):
    address_line_1: str
    address_line_2: Optional[str]
    city: str = Field(index=True)
    state: str = Field(index=True)
    country: str
    postal_code: str = Field(index=True)