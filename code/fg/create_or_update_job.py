import hopsworks

project = hopsworks.login()

jobs_api = project.get_jobs_api()

py_job_config = jobs_api.get_configuration("PYTHON")

py_job_config['appPath'] = "Jupyter/Hopsworks-CI-CD/code/fg/create_fg.ipynb"


job=None

try:
  job = jobs_api.get_job("create_fg")
except:
  job = jobs_api.create_job("create_fg", py_job_config)


