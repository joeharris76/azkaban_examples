#!/usr/bin/env python
# encoding: utf-8

"""Azkaban example projects configuration script.

Azkaban CLI syntax definition to configure all examples in this project

"""

from azkaban import Job, Project

project = Project('azkaban_examples')

# `basic_flow` example
project.add_job('basic_1st_command', Job({'type': 'command', 'command': 'echo "basic_1st_command.job"'}))
project.add_job('basic_2nd_command', Job({'type': 'command', 'command': 'echo "basic_2nd_command.job"', 'dependencies': 'basic_1st_command'}))
project.add_job('basic_3rd_command', Job({'type': 'command', 'command': 'echo "basic_3rd_command.job"', 'dependencies': 'basic_2nd_command'}))
project.add_job('basic_4th_command', Job({'type': 'command', 'command': 'echo "basic_4th_command.job"', 'dependencies': 'basic_3rd_command'}))
project.add_job('basic_5th_command', Job({'type': 'command', 'command': 'echo "basic_5th_command.job"', 'dependencies': 'basic_4th_command'}))
project.add_job('basic_6th_command', Job({'type': 'command', 'command': 'echo "basic_6th_command.job"', 'dependencies': 'basic_4th_command'}))
project.add_job('basic_7th_command', Job({'type': 'command', 'command': 'echo "basic_7th_command.job"', 'dependencies': 'basic_2nd_command'}))
project.add_job('basic_8th_command', Job({'type': 'command', 'command': 'echo "basic_8th_command.job"', 'dependencies': 'basic_2nd_command'}))
project.add_job('basic_flow'       , Job({'type': 'noop'   , 'dependencies': 'basic_5th_command,basic_6th_command,basic_7th_command,basic_8th_command'}))

# `embedded_flows` example
project.add_job('embed_1st_command', Job({'type': 'command', 'command': 'echo "embed_1st_command.job"'}))
project.add_job('embed_2nd_command', Job({'type': 'command', 'command': 'echo "embed_2nd_command.job"', 'dependencies': 'embed_1st_command'}))
project.add_job('embed_3rd_command', Job({'type': 'command', 'command': 'echo "embed_3rd_command.job"'}))
project.add_job('embed_4th_command', Job({'type': 'command', 'command': 'echo "embed_4th_command.job"', 'dependencies': 'embed_3rd_command'}))
project.add_job('embed_5th_command', Job({'type': 'command', 'command': 'echo "embed_5th_command.job"'}))
project.add_job('embed_6th_command', Job({'type': 'command', 'command': 'echo "embed_6th_command.job"'}))
project.add_job('embed_7th_command', Job({'type': 'command', 'command': 'echo "embed_7th_command.job"'}))
project.add_job('embed_8th_command', Job({'type': 'command', 'command': 'echo "embed_8th_command.job"'}))
project.add_job('embed_flow_1'     , Job({'type': 'flow'   , 'flow.name': 'embed_flow_2', 'dependencies': 'embed_2nd_command'}))
project.add_job('embed_flow_2'     , Job({'type': 'flow'   , 'flow.name': 'embed_noop_1', 'dependencies': 'embed_4th_command'}))
project.add_job('embed_flow_3'     , Job({'type': 'flow'   , 'flow.name': 'embed_noop_2', 'dependencies': 'embed_2nd_command'}))
project.add_job('embed_noop_0'     , Job({'type': 'noop'   , 'dependencies': 'embed_flow_1,embed_flow_3'}))
project.add_job('embed_noop_1'     , Job({'type': 'noop'   , 'dependencies': 'embed_5th_command,embed_6th_command'}))
project.add_job('embed_noop_2'     , Job({'type': 'noop'   , 'dependencies': 'embed_7th_command,embed_8th_command'}))
project.add_job('embedded_flows'   , Job({'type': 'flow'   , 'flow.name': 'embed_noop_0'}))

# `reusing_flows` example
project.add_job('reuse_1st_command', Job({'type': 'command', 'command': 'echo "reuse_1st_command.job"'}))
project.add_job('reuse_2nd_command', Job({'type': 'command', 'command': 'echo "reuse_2nd_command.job"', 'dependencies': 'reuse_1st_command'}))
project.add_job('reuse_3rd_command', Job({'type': 'command', 'command': 'echo "reuse_3rd_command.job"', 'dependencies': 'reuse_flow_2'}))
project.add_job('reuse_4th_command', Job({'type': 'command', 'command': 'echo "reuse_4th_command.job"', 'dependencies': 'reuse_3rd_command'}))
project.add_job('reuse_5th_command', Job({'type': 'command', 'command': 'echo "reuse_5th_command.job"'}))
project.add_job('reuse_6th_command', Job({'type': 'command', 'command': 'echo "reuse_6th_command.job"'}))
project.add_job('reuse_7th_command', Job({'type': 'command', 'command': 'echo "reuse_7th_command.job"', 'dependencies': 'reuse_flow_2'}))
project.add_job('reuse_8th_command', Job({'type': 'command', 'command': 'echo "reuse_8th_command.job"', 'dependencies': 'reuse_flow_2'}))
project.add_job('reuse_flow_1'     , Job({'type': 'flow'   , 'flow.name': 'reuse_4th_command', 'dependencies': 'reuse_2nd_command'}))
project.add_job('reuse_flow_2'     , Job({'type': 'flow'   , 'flow.name': 'reuse_noop_1'}))
project.add_job('reuse_flow_3'     , Job({'type': 'flow'   , 'flow.name': 'reuse_noop_2', 'dependencies': 'reuse_2nd_command'}))
project.add_job('reuse_noop_0'     , Job({'type': 'noop'   , 'dependencies': 'reuse_flow_1,reuse_flow_3'}))
project.add_job('reuse_noop_1'     , Job({'type': 'noop'   , 'dependencies': 'reuse_5th_command,reuse_6th_command'}))
project.add_job('reuse_noop_2'     , Job({'type': 'noop'   , 'dependencies': 'reuse_7th_command,reuse_8th_command'}))
project.add_job('reusing_flows'    , Job({'type': 'flow'   , 'flow.name': 'reuse_noop_0'}))

