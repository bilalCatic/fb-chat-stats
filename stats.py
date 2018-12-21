import json

with open('message.json') as f:
    data = json.load(f)

messages = data['messages']
messages_count = len(messages)

person_stats = {}

for message in messages:
    if message['sender_name'] in person_stats:
        person_stats[message['sender_name']] += 1
    else:
        person_stats[message['sender_name']] = 1

for name, count in person_stats.items():
    print(u'{0} : {1} [{2:.2f} %]'.format(name, count, count*100.0/messages_count))

print('===========')
print('Total count : {0}'.format(messages_count))
