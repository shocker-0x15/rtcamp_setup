import paramiko

key_path = R'/Users/shocker_0x15/.ssh/id_rsa'
hostname = '90.149.9.146'
port = 56131
username = 'shocker_0x15'

ssh = paramiko.SSHClient()
key = paramiko.RSAKey(filename=key_path)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, port=port, username=username, pkey=key)

cmd = f'Get-ChildItem -Path $home -File | Select-Object -ExpandProperty Name'
_, stdout, _ = ssh.exec_command(cmd)
file_list = stdout.read().decode().splitlines()

cmd = f'echo $env:home'
_, stdout, _ = ssh.exec_command(cmd)
home_dir = stdout.read().decode().rstrip()

sftp = ssh.open_sftp()
sftp.get(f'{home_dir}\\{file_list[0]}',
         f'/Users/shocker_0x15/{file_list[0]}')
sftp.close()

ssh.close()