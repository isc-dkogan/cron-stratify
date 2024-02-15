import os
import json
import requests

def run_stratify():

    print('Running Stratify')

    api_url = os.environ['STRATIFY_REST_ENDPOINT_URL'] + "/run_job/stratify"

    print(f'Endpoint: {api_url}')

    f = open("./cron_module/config.conf")

    config = json.load(f)

    config_str = json.dumps(config)
    print(f'Config: {config_str}')
    headers =  {"accept":"application/json"}
    response = requests.post(api_url, data=config_str, headers=headers)

if __name__ == '__main__': 
    run_stratify()