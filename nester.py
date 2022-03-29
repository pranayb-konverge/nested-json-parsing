nested_json = {
  "destination_addresses": [
    "Washington, DC, USA",
    "Philadelphia, PA, USA",
    "Santa Barbara, CA, USA",
    "Miami, FL, USA",
    "Austin, TX, USA",
    "Napa County, CA, USA"
  ],
  "origin_addresses": [
    "New York, NY, USA"
  ],
  "rows": [{
    "elements": [{
        "distance": {
          "text": "227 mi",
          "value": 365468
        },
        "duration": {
          "text": "3 hours 54 mins",
          "value": 14064
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "94.6 mi",
          "value": 152193
        },
        "duration": {
          "text": "1 hour 44 mins",
          "value": 6227
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "2,878 mi",
          "value": 4632197
        },
        "duration": {
          "text": "1 day 18 hours",
          "value": 151772
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "1,286 mi",
          "value": 2069031
        },
        "duration": {
          "text": "18 hours 43 mins",
          "value": 67405
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "1,742 mi",
          "value": 2802972
        },
        "duration": {
          "text": "1 day 2 hours",
          "value": 93070
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "2,871 mi",
          "value": 4620514
        },
        "duration": {
          "text": "1 day 18 hours",
          "value": 152913
        },
        "status": "OK"
      }
    ]
  }],
  "status": "OK"
}



def nester(json_data, key):
    required_data = []

    def extract(json_data, required_data, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(json_data, dict):
            for k, v in json_data.items():
                # if the valus is a json or list, get a recursive call, else we got the key
                if isinstance(v, (dict, list)):
                    extract(v, required_data, key)
                elif k == key:                    
                    required_data.append(v)
        elif isinstance(json_data, list):
            for item in json_data:
                extract(item, required_data, key)
        return required_data

    values = extract(json_data, required_data, key)
    return values
# end of nester()

data = nester(nested_json, "text")
distance_per_time = {}
keys, values = [], []
print(data)
length_of_data = len(data)
for k in range(0, length_of_data):
    # if the result is 1 then its true or else false
    if k % 2:
        values.append(data[k])
    else :
        keys.append(data[k])

distance_per_time = dict(zip(keys, values))
print()
print(distance_per_time)