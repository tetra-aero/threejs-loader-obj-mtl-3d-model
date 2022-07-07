```
chiya@ujimatsu:~/JetsonWorks/threejs-loader-obj-mtl-3d-model$ ssh -i ~/.ssh/test-threejs.pem ec2-35-78-90-47.ap-northeast-1.compute.amazonaws.com
The authenticity of host 'ec2-35-78-90-47.ap-northeast-1.compute.amazonaws.com (35.78.90.47)' can't be established.
ECDSA key fingerprint is SHA256:J7G6VTuPxpdK92hP4Ex8IZuGAq0L/ZDJ/o+F/+ra4jY.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'ec2-35-78-90-47.ap-northeast-1.compute.amazonaws.com,35.78.90.47' (ECDSA) to the list of known hosts.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0664 for '/home/chiya/.ssh/test-threejs.pem' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "/home/chiya/.ssh/test-threejs.pem": bad permissions
chiya@ec2-35-78-90-47.ap-northeast-1.compute.amazonaws.com: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
chiya@ujimatsu:~/JetsonWorks/threejs-loader-obj-mtl-3d-model$ ls -ls ~/.ssh
total 56
 4 -rwx------ 1 chiya chiya  738 Feb 16 11:51 config
12 -rw------- 1 chiya chiya 9980 Jun 28 22:34 known_hosts
 4 -rw-rw-r-- 1 chiya chiya 1678 Jun 28 22:31 test-threejs.pem
chiya@ujimatsu:~/JetsonWorks/threejs-loader-obj-mtl-3d-model$ chmod 700 ~/.ssh/test-threejs.pem 
chiya@ujimatsu:~/JetsonWorks/threejs-loader-obj-mtl-3d-model$ ls -ls ~/.ssh
total 56
 4 -rwx------ 1 chiya chiya  738 Feb 16 11:51 config
12 -rw------- 1 chiya chiya 9980 Jun 28 22:34 known_hosts
 4 -rwx------ 1 chiya chiya 1678 Jun 28 22:31 test-threejs.pem
chiya@ujimatsu:~/JetsonWorks/threejs-loader-obj-mtl-3d-model$ ssh -i ~/.ssh/test-threejs.pem ec2-35-78-90-47.ap-northeast-1.compute.amazonaws.com
chiya@ec2-35-78-90-47.ap-northeast-1.compute.amazonaws.com: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
chiya@ujimatsu:~/JetsonWorks/threejs-loader-obj-mtl-3d-model$ ssh -i ~/.ssh/test-threejs.pem ec2-user@ec2-35-78-90-47.ap-northeast-1.compute.amazonaws.com

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
[ec2-user@ip-172-31-2-26 ~]$ git
-bash: git: command not found
[ec2-user@ip-172-31-2-26 ~]$ python
Python 2.7.18 (default, May 25 2022, 14:30:51) 
[GCC 7.3.1 20180712 (Red Hat 7.3.1-15)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit[]
  File "<stdin>", line 1
    exit[]
         ^
SyntaxError: invalid syntax
>>> exit()
[ec2-user@ip-172-31-2-26 ~]$ yum install git
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
You need to be root to perform this command.
[ec2-user@ip-172-31-2-26 ~]$ sudo yum install git
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
Resolving Dependencies
--> Running transaction check
---> Package git.x86_64 0:2.32.0-1.amzn2.0.1 will be installed
--> Processing Dependency: perl-Git = 2.32.0-1.amzn2.0.1 for package: git-2.32.0-1.amzn2.0.1.x86_64
--> Processing Dependency: git-core-doc = 2.32.0-1.amzn2.0.1 for package: git-2.32.0-1.amzn2.0.1.x86_64
--> Processing Dependency: git-core = 2.32.0-1.amzn2.0.1 for package: git-2.32.0-1.amzn2.0.1.x86_64
--> Processing Dependency: emacs-filesystem >= 27.1 for package: git-2.32.0-1.amzn2.0.1.x86_64
--> Processing Dependency: perl(Term::ReadKey) for package: git-2.32.0-1.amzn2.0.1.x86_64
--> Processing Dependency: perl(Git::I18N) for package: git-2.32.0-1.amzn2.0.1.x86_64
--> Processing Dependency: perl(Git) for package: git-2.32.0-1.amzn2.0.1.x86_64
--> Running transaction check
---> Package emacs-filesystem.noarch 1:27.2-4.amzn2.0.1 will be installed
---> Package git-core.x86_64 0:2.32.0-1.amzn2.0.1 will be installed
---> Package git-core-doc.noarch 0:2.32.0-1.amzn2.0.1 will be installed
---> Package perl-Git.noarch 0:2.32.0-1.amzn2.0.1 will be installed
--> Processing Dependency: perl(Error) for package: perl-Git-2.32.0-1.amzn2.0.1.noarch
---> Package perl-TermReadKey.x86_64 0:2.30-20.amzn2.0.2 will be installed
--> Running transaction check
---> Package perl-Error.noarch 1:0.17020-2.amzn2 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

==============================================================================================================================================
 Package                              Arch                       Version                                 Repository                      Size
==============================================================================================================================================
Installing:
 git                                  x86_64                     2.32.0-1.amzn2.0.1                      amzn2-core                     126 k
Installing for dependencies:
 emacs-filesystem                     noarch                     1:27.2-4.amzn2.0.1                      amzn2-core                      67 k
 git-core                             x86_64                     2.32.0-1.amzn2.0.1                      amzn2-core                     4.8 M
 git-core-doc                         noarch                     2.32.0-1.amzn2.0.1                      amzn2-core                     2.7 M
 perl-Error                           noarch                     1:0.17020-2.amzn2                       amzn2-core                      32 k
 perl-Git                             noarch                     2.32.0-1.amzn2.0.1                      amzn2-core                      43 k
 perl-TermReadKey                     x86_64                     2.30-20.amzn2.0.2                       amzn2-core                      31 k

Transaction Summary
==============================================================================================================================================
Install  1 Package (+6 Dependent packages)

Total download size: 7.8 M
Installed size: 38 M
Is this ok [y/d/N]: y
Downloading packages:
(1/7): emacs-filesystem-27.2-4.amzn2.0.1.noarch.rpm                                                                    |  67 kB  00:00:00     
(2/7): git-2.32.0-1.amzn2.0.1.x86_64.rpm                                                                               | 126 kB  00:00:00     
(3/7): git-core-doc-2.32.0-1.amzn2.0.1.noarch.rpm                                                                      | 2.7 MB  00:00:00     
(4/7): git-core-2.32.0-1.amzn2.0.1.x86_64.rpm                                                                          | 4.8 MB  00:00:00     
(5/7): perl-Error-0.17020-2.amzn2.noarch.rpm                                                                           |  32 kB  00:00:00     
(6/7): perl-Git-2.32.0-1.amzn2.0.1.noarch.rpm                                                                          |  43 kB  00:00:00     
(7/7): perl-TermReadKey-2.30-20.amzn2.0.2.x86_64.rpm                                                                   |  31 kB  00:00:00     
----------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                          25 MB/s | 7.8 MB  00:00:00     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : git-core-2.32.0-1.amzn2.0.1.x86_64                                                                                         1/7 
  Installing : git-core-doc-2.32.0-1.amzn2.0.1.noarch                                                                                     2/7 
  Installing : 1:perl-Error-0.17020-2.amzn2.noarch                                                                                        3/7 
  Installing : 1:emacs-filesystem-27.2-4.amzn2.0.1.noarch                                                                                 4/7 
  Installing : perl-TermReadKey-2.30-20.amzn2.0.2.x86_64                                                                                  5/7 
  Installing : perl-Git-2.32.0-1.amzn2.0.1.noarch                                                                                         6/7 
  Installing : git-2.32.0-1.amzn2.0.1.x86_64                                                                                              7/7 
  Verifying  : perl-TermReadKey-2.30-20.amzn2.0.2.x86_64                                                                                  1/7 
  Verifying  : git-core-doc-2.32.0-1.amzn2.0.1.noarch                                                                                     2/7 
  Verifying  : perl-Git-2.32.0-1.amzn2.0.1.noarch                                                                                         3/7 
  Verifying  : 1:emacs-filesystem-27.2-4.amzn2.0.1.noarch                                                                                 4/7 
  Verifying  : git-2.32.0-1.amzn2.0.1.x86_64                                                                                              5/7 
  Verifying  : git-core-2.32.0-1.amzn2.0.1.x86_64                                                                                         6/7 
  Verifying  : 1:perl-Error-0.17020-2.amzn2.noarch                                                                                        7/7 

Installed:
  git.x86_64 0:2.32.0-1.amzn2.0.1                                                                                                             

Dependency Installed:
  emacs-filesystem.noarch 1:27.2-4.amzn2.0.1      git-core.x86_64 0:2.32.0-1.amzn2.0.1      git-core-doc.noarch 0:2.32.0-1.amzn2.0.1        
  perl-Error.noarch 1:0.17020-2.amzn2             perl-Git.noarch 0:2.32.0-1.amzn2.0.1      perl-TermReadKey.x86_64 0:2.30-20.amzn2.0.2     

Complete!
[ec2-user@ip-172-31-2-26 ~]$ git clone https://github.com/tetra-aero/threejs-loader-obj-mtl-3d-model.git
Cloning into 'threejs-loader-obj-mtl-3d-model'...
remote: Enumerating objects: 38, done.
remote: Counting objects: 100% (38/38), done.
remote: Compressing objects: 100% (33/33), done.
remote: Total 38 (delta 4), reused 31 (delta 0), pack-reused 0
Receiving objects: 100% (38/38), 1.71 MiB | 24.29 MiB/s, done.
Resolving deltas: 100% (4/4), done.
[ec2-user@ip-172-31-2-26 ~]$ ls
threejs-loader-obj-mtl-3d-model
[ec2-user@ip-172-31-2-26 ~]$ cd threejs-loader-obj-mtl-3d-model/
[ec2-user@ip-172-31-2-26 threejs-loader-obj-mtl-3d-model]$ ls
build  document  jsm  LICENSE  main.css  models  README.md  webgl_loader_obj_mtl.html
[ec2-user@ip-172-31-2-26 threejs-loader-obj-mtl-3d-model]$ python -m http.server 80
/usr/bin/python: No module named http
[ec2-user@ip-172-31-2-26 threejs-loader-obj-mtl-3d-model]$ python3
Python 3.7.10 (default, Jun  3 2021, 00:02:01) 
[GCC 7.3.1 20180712 (Red Hat 7.3.1-13)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
[ec2-user@ip-172-31-2-26 threejs-loader-obj-mtl-3d-model]$ python3 -m http.server 80
Traceback (most recent call last):
  File "/usr/lib64/python3.7/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/usr/lib64/python3.7/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/usr/lib64/python3.7/http/server.py", line 1262, in <module>
    test(HandlerClass=handler_class, port=args.port, bind=args.bind)
  File "/usr/lib64/python3.7/http/server.py", line 1230, in test
    with ServerClass(server_address, HandlerClass) as httpd:
  File "/usr/lib64/python3.7/socketserver.py", line 452, in __init__
    self.server_bind()
  File "/usr/lib64/python3.7/http/server.py", line 137, in server_bind
    socketserver.TCPServer.server_bind(self)
  File "/usr/lib64/python3.7/socketserver.py", line 466, in server_bind
    self.socket.bind(self.server_address)
PermissionError: [Errno 13] Permission denied
[ec2-user@ip-172-31-2-26 threejs-loader-obj-mtl-3d-model]$ sudo python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
210.175.195.94 - - [28/Jun/2022 13:39:45] "GET / HTTP/1.0" 200 -
210.175.195.94 - - [28/Jun/2022 13:39:45] code 404, message File not found
210.175.195.94 - - [28/Jun/2022 13:39:45] "GET /favicon.ico HTTP/1.0" 404 -
210.175.195.94 - - [28/Jun/2022 13:39:48] "GET /webgl_loader_obj_mtl.html HTTP/1.0" 200 -
210.175.195.94 - - [28/Jun/2022 13:39:48] "GET /main.css HTTP/1.0" 200 -
210.175.195.94 - - [28/Jun/2022 13:39:48] "GET /build/three.module.js HTTP/1.0" 200 -
210.175.195.94 - - [28/Jun/2022 13:39:48] "GET /jsm/loaders/OBJLoader.js HTTP/1.0" 200 -
210.175.195.94 - - [28/Jun/2022 13:39:48] "GET /jsm/loaders/MTLLoader.js HTTP/1.0" 200 -
210.175.195.94 - - [28/Jun/2022 13:39:49] "GET /models/obj/teTra-Mk5-miniature-model/teTra-Mk5-miniature-model.mtl HTTP/1.0" 200 -
210.175.195.94 - - [28/Jun/2022 13:39:49] "GET /models/obj/teTra-Mk5-miniature-model/teTra-Mk5-miniature-model.obj HTTP/1.0" 200 -
210.175.195.94 - - [28/Jun/2022 13:39:49] code 404, message File not found
210.175.195.94 - - [28/Jun/2022 13:39:49] "GET /models/obj/teTra-Mk5-miniature-model/*1 HTTP/1.0" 404 -
210.175.195.94 - - [28/Jun/2022 13:39:49] "GET /models/obj/teTra-Mk5-miniature-model/textures/textured_0_v2.jpg HTTP/1.0" 200 -
34.203.234.144 - - [28/Jun/2022 13:40:23] "GET /webgl_loader_obj_mtl.html HTTP/1.1" 200 -
34.207.139.175 - - [28/Jun/2022 13:40:23] code 404, message File not found
34.207.139.175 - - [28/Jun/2022 13:40:23] "GET /favicon.ico HTTP/1.1" 404 -
66.240.205.34 - - [28/Jun/2022 13:41:08] code 400, message Bad request version ("x64|'|'|No|'|'|0.7d|'|'|..|'|'|AA==|'|'|112.inf|'|'|SGFjS2VkDQoxOTIuMTY4LjkyLjIyMjo1NTUyDQpEZXNrdG9wDQpjbGllbnRhLmV4ZQ0KRmFsc2UNCkZhbHNlDQpUcnVlDQpGYWxzZQ==12.act|'|'|AA==")
66.240.205.34 - - [28/Jun/2022 13:41:08] "145.ll|'|'|SGFjS2VkX0Q0OTkwNjI3|'|'|WIN-JNAPIER0859|'|'|JNapier|'|'|19-02-01|'|'||'|'|Win 7 Professional SP1 x64|'|'|No|'|'|0.7d|'|'|..|'|'|AA==|'|'|112.inf|'|'|SGFjS2VkDQoxOTIuMTY4LjkyLjIyMjo1NTUyDQpEZXNrdG9wDQpjbGllbnRhLmV4ZQ0KRmFsc2UNCkZhbHNlDQpUcnVlDQpGYWxzZQ==12.act|'|'|AA==" 400 -
```
