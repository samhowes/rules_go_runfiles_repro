import sys
import os
import subprocess

from rules_python.python.runfiles import runfiles

if __name__ == "__main__":
    r = runfiles.Create()

    program = sys.argv[1]
    if not program.startswith("bazel"):
        # are we in the genrule?
        rpath = "__main__/" + sys.argv[1]
        program = r.Rlocation(rpath)

        if program is None:
            sys.stderr.write("failed to find cat: " + rpath)
            exit(1)

    env = r.EnvVars()
    completed = subprocess.run([],
                               executable=program,
                               capture_output=True,
                               shell=False,
                               env=env,
                               cwd=os.path.dirname(program) # make sure it can't find files in cwd
                               )

    out = str(completed.stdout, 'utf-8')
    err = str(completed.stderr, 'utf-8')
    sys.stdout.write(out)
    if err != "":
        sys.stdout.write("Error: " + err)
