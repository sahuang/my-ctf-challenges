import ipinfo, random
from tqdm import tqdm

access_token = '0d7a35778b6022'
handler = ipinfo.getHandler(access_token)

# write header ip, city, latitude, longitude to csv
# with open('result.csv', 'w') as f:
#     f.write('ip,city,latitude,longitude\n')

# query 20k times and save to csv
for _ in tqdm(range(20000)):
    try:
        # generate random ip address
        ip_address = '.'.join(str(random.randint(1, 255)) for _ in range(4))
        details = handler.getDetails(ip_address)
        # save to csv ip, city, latitude, longitude
        assert details.ip == ip_address
        # city name should be all printable characters
        assert all(ord(c) < 128 for c in details.city)
        with open('result.csv', 'a') as f:
            # city case insensitive
            f.write(f'{ip_address},{details.city.lower().strip()},{details.latitude},{details.longitude}\n')
    except:
        pass
