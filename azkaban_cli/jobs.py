#!/usr/bin/env python
# encoding: utf-8

"""
  Azkaban example projects configuration script.
   • Azkaban CLI syntax definition to configure all examples in this project
"""

from azkaban import Job, Project

PROJECT = Project('azkaban_examples', root=__file__)
# Project level properties declared here are visible to all jobs.
PROJECT.properties = {
  'project_1': 'project-val1'
}

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
  'basic_flow':        Job({'type': 'noop'   , 'dependencies': 'basic_step_5.cmd,basic_step_6.cmd,basic_step_7.cmd,basic_step_8.cmd'}),
  # `template_flow` example
  #   • Demonstrates using one flow as a "template" that is embedded in another flow and reused multiple times.
  #   • The only work performed by job in this example template is to echo out the variables it receives to the log.
  #     NOTE: We have to `chmod 777` our script to make sure Azkaban can run it.
  '_template_chmod.cmd':  Job({'type': 'command', 'command': 'chmod 777 _echo.sh'}),
  '_template_echo_1.cmd': Job({'type': 'command', 'command': './_echo.sh "echo_1" ${project_1} ${custom_1} ${custom_2}', 'dependencies': '_template_chmod.cmd'}),
  '_template_echo_2.cmd': Job({'type': 'command', 'command': './_echo.sh "echo_2" ${project_1} ${custom_1} ${custom_2}', 'dependencies': '_template_echo_1.cmd'}),
  '_template':            Job({'type': 'noop'   , 'dependencies': '_template_echo_2.cmd'}),
  #   • Each of the following subflows embeds *ALL* of the steps from `_template` using the `flow.name` key.
  #   • Each defines `custom_1` and `custom_2` keys which are passed as variables ${custom_1} and ${custom_2} to `_template` during execution.
  'start.noop':           Job({'type': 'noop'}),
  'subflow_1.flow':       Job({'type': 'flow', 'flow.name': '_template', 'dependencies': 'start.noop', 'custom_1': 'subflow1-val1', 'custom_2': 'subflow1-val2'}),
  'subflow_2.flow':       Job({'type': 'flow', 'flow.name': '_template', 'dependencies': 'start.noop', 'custom_1': 'subflow2-val1', 'custom_2': 'subflow2-val2'}),
  'subflow_3.flow':       Job({'type': 'flow', 'flow.name': '_template', 'dependencies': 'start.noop', 'custom_1': 'subflow3-val1', 'custom_2': 'subflow3-val2'}),
  'subflow_4.flow':       Job({'type': 'flow', 'flow.name': '_template', 'dependencies': 'start.noop', 'custom_1': 'subflow4-val1', 'custom_2': 'subflow4-val2'}),
  'workflow':             Job({'type': 'noop', 'dependencies': 'subflow_1.flow,subflow_2.flow,subflow_3.flow,subflow_4.flow'})
}

for name, job in JOBS.items():
  PROJECT.add_job(name, job)

# The CLI requires any non-job files to be explicitly included. 
# Must declare the `root` in the project in order for this to work. 
FILES = {
  './_echo.sh': '_echo.sh'
}

for file, name in FILES.items():
  PROJECT.add_file(file, name)
