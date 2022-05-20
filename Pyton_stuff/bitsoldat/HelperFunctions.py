import subprocess

host = "www.google.comsas"

ping = subprocess.Popen(
    ["ping", "-c", "5", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

out, error = ping.communicate()
print(out.decode(), error.decode())