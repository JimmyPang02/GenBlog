# Git

## git配置

查看本地配置

```
git config -l
```

查看系统配置

```
git config --system --list
```

查看全局配置

```
git config --global --list
```



全局配置用户名与邮箱

```
git config --global user.name "aker"
git config --global user.email "1144280511@qq.com"
```



## Git基本理论（核心）





## 创建版本库

```git
git init
#在目标目录下，把这个目录变成Git可以管理的仓库
git add readme.txt
#把文件添加到仓库（缓存区，不是真正的提交）
git commit -m "xxx"
#把文件提交到仓库,-m后面输入的是本次提交的说明
```

## 版本管理

```git
git status
#查看仓库当前的状态，是否有文件需要提交
git diff <文件名>
#查看文件修改的内容 
```



## 远程部署仓库

生成密钥

```
ssh-keygen -t rsa
```

显示连接的远程仓库

```
git remote
```

查看当前配置的远程仓库地址

```
git remote -v  
```



## 通过多个ssh密钥部署多个账户的仓库

一个公钥只能配置一个账户，一个账户可以关联多个公钥。比如你拥有多个设备，每个设备上可以生成一个公钥和你的账户相关联，关联后此公钥便不能与其它的账户或项目进行关联.否则会出现报错

```
Key is already in use  
```

**步骤**

创建仓库

```
git init 
git add .
git commit -m "xxx"
```

分枝重命名

```
git branch -m master main
```

> git init创建的分枝名默认为master，而github仓库的默认分枝是main，所以要更改名字

创建新的密钥，-t rsa是默认加密方式 -C是密钥注释，密钥名称在接下来反馈的命令中设置

```
ssh-keygen -t rsa -C "youremail@example.com"
```

把公钥配置到github仓库中

在`.ssh\config`文件中配置（多仓库才用到）

```
# Default github account: 1144280511
Host github.com
    HostName github.com
    IdentityFile ~/.ssh/id_rsa
    IdentitiesOnly yes
    
 # Other github account: aker114428
 Host github-aker114428
    HostName github.com
    IdentityFile ~/.ssh/id_gmail
    IdentitiesOnly yes
```

添加私有密钥到代理

```
$ eval `ssh-agent -s` //启用ssh代理才能添加
$ ssh-add ~/.ssh/id_rsa
$ ssh-add ~/.ssh/id_gmail
```

检查连接

```
$ github.com
$ ssh -T git@github-aker114428
```

> @后使用不同的Host会通过不同的ssh密钥连接到指定托管网站

关联远程仓库

```git
git remote add origin git@github-aker114428:aker114428/anniversary.git
```

提交仓库

```
git push -u origin main
```

