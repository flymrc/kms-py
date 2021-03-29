#   -*- coding: utf-8 -*-
import logging

from pybuilder.core import use_plugin, init
from pybuilder.core import task

logger = logging.getLogger(__name__)

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "kms-py"
default_task = "publish"


@init
def set_properties(project):
    project.build_depends_on("mockito")


@task
def say_hello():
    logger.info("Hello, PyBuilder\n")

@task
def build_openapi():
    import subprocess
    subprocess.check_output('openapi-generator generate -i openapi.yaml -g python-flask -o openapi_server/', shell=True)
