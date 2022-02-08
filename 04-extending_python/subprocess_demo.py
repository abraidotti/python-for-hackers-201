import subprocess

# spawn the calculator app in windows:
# subprocess.call("calc")

# add complexity:
# subprocess.call(["calc"], shell=True)

# out = subprocess.check_call(["cmd", "/c", "dir"])

out = subprocess.check_output(["cmd", "/c", "dir"])
print(f"the output was {out.decode()}")
