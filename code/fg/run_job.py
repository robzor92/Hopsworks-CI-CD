import hopsworks

import argparse

parser = argparse.ArgumentParser(description='Arguments for Feature Group creation.')

parser.add_argument('--version', default=1, required=False)

args = parser.parse_args()



project = hopsworks.login()

jobs_api = project.get_jobs_api()

job = jobs_api.get_job("create_fg")

# Run the job
execution = job.run(args="--version " + str(args.version), await_termination=True)

# Download logs
out, err = execution.download_logs()

f_out = open(out, "r")
print(f_out.read())

f_err = open(err, "r")
print(f_err.read())
