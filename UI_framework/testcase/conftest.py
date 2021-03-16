import os
import signal
import subprocess

import pytest

# 录屏
from UI_framework.page.logger import log_init


@pytest.fixture(scope="session", autouse=True)
def record():
    log_init()
    # 用例运行前做的一些事情
    os.system('chcp 65001')
    cmd = "scrcpy -Nr tmp.mp4"
    p = subprocess.Popen(cmd, shell=True)
    yield
    # 用例运行后做的一些事情
    # os.kill(p.pid,signal.SIGINT)
    os.popen('taskkill.exe/pid:' + str(p.pid))
