#!/usr/bin/env python
#sabryr 15-06-2021

import sys
sys.path.insert(0, '/cluster/installations/easybuild/hooks')
import reference_database_path

def parse_hook(self):
        MODULES_TO_CHECK=reference_database_path.get_modules_to_fix()
        if self.name in MODULES_TO_CHECK:
                DB_LOC=reference_database_path.read_info_for_module_name(self.name)
                self['modloadmsg']=DB_LOC

