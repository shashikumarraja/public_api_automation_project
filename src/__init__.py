import os

#
# Global Variables
#

global_src_dir = os.path.dirname(__file__)

global_base_dir = os.path.dirname(global_src_dir) 

global_test_dir = os.path.join(global_base_dir, 'tests')

global_logs_dir = os.path.join(global_base_dir, 'logs')