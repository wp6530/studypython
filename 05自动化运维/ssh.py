import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.1.5', 22, 'root', 'ROOTadmin123')
stdin, stdout, stderr = client.exec_command('ls -l')
s = stdout.readlines()

print("".join(str(line) for line in s))
