import argparse

parser = argparse.ArgumentParser(description='Arguments for Job creation.')

parser.add_argument('--name', required=True)
parser.add_argument('--appPath', required=True)

args = parser.parse_args()


import hopsworks

project = hopsworks.login()

jobs_api = project.get_jobs_api()

py_job_config = jobs_api.get_configuration("PYTHON")

py_job_config['appPath'] = args.appPath


job=None

try:
  job = jobs_api.get_job(args.name)
except:
  job = jobs_api.create_job(args.name, py_job_config)


