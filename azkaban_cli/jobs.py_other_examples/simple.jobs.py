#!/usr/bin/env python
# encoding: utf-8

"""
  Azkaban CLI syntax definition of the `basic_flow` project
"""

from azkaban import Job, Project

PROJECT = Project('azkaban_examples')

JOBS = {
  # `basic_flow` example
  'basic_step_1.cmd':  Job({'type': 'command', 'command': 'echo "job: basic_step_1.cmd"'}),
  'basic_step_2.cmd':  Job({'type': 'command', 'command': 'echo "job: basic_step_2.cmd"', 'dependencies': 'basic_step_1.cmd'}),
  'basic_step_3.cmd':  Job({'type': 'command', 'command': 'echo "job: basic_step_3.cmd"', 'dependencies': 'basic_step_2.cmd'}),
  'basic_step_4.cmd':  Job({'type': 'command', 'command': 'echo "job: basic_step_4.cmd"', 'dependencies': 'basic_step_3.cmd'}),
  'basic_step_5.cmd':  Job({'type': 'command', 'command': 'echo "job: basic_step_5.cmd"', 'dependencies': 'basic_step_4.cmd'}),
  'basic_step_6.cmd':  Job({'type': 'command', 'command': 'echo "job: basic_step_6.cmd"', 'dependencies': 'basic_step_4.cmd'}),
  'basic_step_7.cmd':  Job({'type': 'command', 'command': 'echo "job: basic_step_7.cmd"', 'dependencies': 'basic_step_2.cmd'}),
  'basic_step_8.cmd':  Job({'type': 'command', 'command': 'echo "job: basic_step_8.cmd"', 'dependencies': 'basic_step_2.cmd'}),
  'basic_flow':        Job({'type': 'noop'   , 'dependencies': 'basic_step_5.cmd,basic_step_6.cmd,basic_step_7.cmd,basic_step_8.cmd'})
}

for name, job in JOBS.items():
  PROJECT.add_job(name, job)
