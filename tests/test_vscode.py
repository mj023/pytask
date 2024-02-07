from __future__ import annotations

import textwrap

import pytest
import os
from pytask import cli
from pytask import build
from pytask import ExitCode



@pytest.mark.end_to_end()
def test_vscode_collect(runner, tmp_path):
    source = """
    def task_raises():
        return
    """
    os.environ["PYTASK_VSCODE"] = "True"
    tmp_path.joinpath("task_module.py").write_text(textwrap.dedent(source))

    result = runner.invoke(cli, ["collect", tmp_path.as_posix()])
    assert result.exit_code == ExitCode.OK

@pytest.mark.end_to_end()
def test_vscode_build(runner, tmp_path):
    source = """
    def task_raises():
        return
    """
    os.environ["PYTASK_VSCODE"] = "True"
    tmp_path.joinpath("task_module.py").write_text(textwrap.dedent(source))

    result = runner.invoke(cli, [tmp_path.as_posix()])
    assert result.exit_code == ExitCode.OK