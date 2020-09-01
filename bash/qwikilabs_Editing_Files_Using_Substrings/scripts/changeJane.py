#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1]) as file:
        oldname=file.readlines()
        oldname=[name.strip()for name in oldname]
        newname=[name.replace("jane","jdoe") for name in oldname]
        print(newname)
        for x in range(len(oldname)):
                subprocess.run(["mv",oldname[x],newname[x]])
        file.close()