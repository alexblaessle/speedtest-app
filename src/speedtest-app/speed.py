import logging
import os
import typing

from datetime import datetime
from speedtest import Speedtest


class SpeedtestLogger(Speedtest):

    def __init__(self, out):

        self.out = out

    def log_test(self):

        mode = "a" if os.path.exists(self.out) else "w"
        logging.info(f"Writing to file {self.out} with mode = {mode}.")

        with open(self.out, mode) as f:
            if mode == "w":
                f.write("timestamp,download,upload,ping\n")
            result = self.test_speed()
            result = [str(r) for r in result]
            f.write(f"{','.join(list(result))}\n")

    def log_tests(self, ntests):

        for i in range(ntests):
            logging.info("Making test #{}".format(i + 1))
            self.log_test()

    def test_speed(self):
        s = Speedtest(secure=True)
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        return self.get_timestamp(), res["download"], res["upload"], res["ping"]

    def get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
