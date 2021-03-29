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
def buildOpenApi():
    import subprocess

    subprocess.check_output(
        "openapi-generator generate -i openapi_server/kms-leancloud.yaml -g python-flask -o openapi_server/",
        shell=True,
    )


@task
def buildOpenApiYaml():
    import subprocess

    subprocess.check_output(
        "npx swagger-cli bundle api/openapi.yaml --outfile api/openapi-dist.yaml --type yaml",
        shell=True,
    )