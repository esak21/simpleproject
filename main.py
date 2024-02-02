import sys

from lib import Utils
from lib.logger import Log4j


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usuage :: sbdl <ENV> <LOAD_DATE>")
        sys.exit(-1)

    job_run_env = sys.argv[1].upper()
    load_date = sys.argv[2]

    spark = Utils.get_spark_session(job_run_env)
    logger = Log4j(spark)

    logger.info("Finished creating Spark Session")
