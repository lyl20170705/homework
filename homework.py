import os
def function3(cwd,branch,url,back_num):
    os.chdir(cwd)
    os.system('git checkout '+branch)#switch the selected branch
    os.system('git reset --hard HEAD~'+back_num)
    os.system('git pull '+url+' '+branch)
    os.system('git push '+url+' '+branch)
    return os.popen('git log').read()
cwd='D:/LTE/repository2'
branch='branchA'
url='https://github.com/lyl20170705/LTE1.git'
back_num='1'
print function3(cwd,branch,url,back_num)


