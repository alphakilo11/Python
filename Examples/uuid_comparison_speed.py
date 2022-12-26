import random, string
relevant_chars = ''
relevant_chars += string.ascii_lowercase + string.digits
def create_uuidlookalike():
  uuid_lookalike = ''
  uuid_lookalike += ''.join(random.choices(relevant_chars, k=8))
  uuid_lookalike += '-'
  for i in range(3):
    uuid_lookalike += ''.join(random.choices(relevant_chars, k=4))
    uuid_lookalike += '-'
  uuid_lookalike += ''.join(random.choices(relevant_chars, k=12))
  return uuid_lookalike

lookalikes = []
for i in range(int(1e6)):
  lookalikes.append(create_uuidlookalike())
  
for i in random.choices(lookalikes, k=1000):
  lookalikes.index(i)
del lookalikes

import uuid
uuids = []
for i in range(int(1e6)):
  uuids.append(uuid.uuid4())

for i in random.choices(uuids, k=1000):
  uuids.index(i)
del uuids

foo = uuid.uuid4()
print(foo.__str__())
del foo
