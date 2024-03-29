import os
import json
import requests

def run_stratify():

    api_url = os.environ['STRATIFY_REST_ENDPOINT_URL'] + "/run_job/stratify"

    f = open("./cron_module/config.conf")

    config = json.load(f)

    config_str = json.dumps(config)
    headers =  {"accept":"application/json"}
    response = requests.post(api_url, data=config_str, headers=headers)
    print(response)

if __name__ == '__main__': 
    run_stratify()