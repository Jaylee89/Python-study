
import os, zipfile
from os.path import join, getsize
import paramiko

"""
zipfile file
ssh
file scp push
"""

def make_zip(source_dir, output_filename):
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        print(parent, "consumes ", end="")
        print(sum([getsize(join(parent, name)) for name in dirnames]), end="")
        print("bytes in", len(filenames), "non-directory files")
        if "help" in dirnames:
            dirnames.remove("help")
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)   #相对路径
            zipf.write(pathfile, arcname)
    zipf.close()

def filter_expect_directory(folder_name):
    pass

def ssl_logon():
    paramiko.util.log_to_file('paramiko.log')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('47.92.52.175', username='root', password='H$bc1234')
    cmd = 'ls'
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.readlines())
    return ssh

    # cmd = 'ls >test'
    # stdin, stdout, stderr = ssh.exec_command(cmd)
    # print(stdout.readlines())
    #
    # cmd = 'cat test'
    # stdin, stdout, stderr = ssh.exec_command(cmd)
    # print stdout.readlines()

def logon_with_rsa():
    pkey = 'E:/wamp/www/tools/id_rsa'  # 本地密钥文件路径[此文件服务器上~/.ssh/id_rsa可下载到本地]
    key = paramiko.RSAKey.from_private_key_file(pkey, password='******')  # 有解密密码时,
    paramiko.util.log_to_file('paramiko.log')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.load_system_host_keys() #如通过known_hosts 方式进行认证可以用这个,如果known_hosts 文件未定义还需要定义 known_hosts
    ssh.connect('47.92.52.175', username='root', password='test1234', pkey=key)  # 这里要 pkey passwordkey 密钥文件
    stdin, stdout, stderr = ssh.exec_command('hostname')
    print(stdout.read())
    stdin, stdout, stderr = ssh.exec_command('ls')

def sftp_upload():
    ssh = ssl_logon()
    t = ssh.get_transport()
    sftp = paramiko.SFTPClient.from_transport(t)
    d = sftp.put("paramiko.log", "/root/mm.txt")
    print(d)
    t.close()

def sftp_download():
    ssh = ssl_logon()
    t = ssh.get_transport()
    sftp = paramiko.SFTPClient.from_transport(t)
    d = sftp.get("/root/mm.txt", "mm.txt")
    print(d)
    t.close()


if __name__ == "__main__":
    make_zip(r"D:\software\development\python\Python-study\demo_py3\AI", os.path.dirname(__file__) + "/test.zip")
    # sftp_upload()
    # sftp_download()
