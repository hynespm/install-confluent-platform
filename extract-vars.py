import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

branch = "refs/heads/7.2.2"#os.environ['GITHUB_REF']
branch_name = branch.split("/")
branch_name_value = branch_name[len(branch_name)-1]
major_version = branch_name_value.split(".")
maj_ver = major_version[0] + "." + major_version[1]
min_ver = maj_ver + major_version[2]
logging.info(maj_ver)
os.environ["CONFLUENT_MAJOR_VERSION"] = maj_ver
os.environ["CONFLUENT_MINOR_VERSION"] = min_ver
