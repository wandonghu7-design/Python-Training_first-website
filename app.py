#这一节我们学习如何编写一段网站程式（网站程式必须24h运行，否则一旦停掉就无法登录网站）
from flask import Flask
app=Flask(__name__)#__name__是Python内建的一个变数，可以用来储存目前这个程式在哪个模组下执行

@app.route("/")#这是函式的装饰：以函式为基础基础，提供一些附加的功能
def home():
    return "Hello Flask!\nFuckyou Flask!"

@app.route("/test")#我们可以将其理解为：这是网站的子页面。具体内容看最后的备注
def test():
    return "This is a test."

if __name__=="__main__":#如果__name__以主程式运行
    app.run()#那么就启动伺服器

#比如说，以网站 http://127.0.0.1:5000/test 为例：
    #http://127.0.0.1:5000 是网站的“主机”，你可以理解为一个网站的主页
    #/ 是网站的“根目录”
    #test 是网站的“子目录”，你可以理解为一个网站的子页面



#接下来我们学习如何将网站部署到云端，其流程为：
    #第一步，建立Flask专案描述档案，其目的是为了告诉别人我们的专案是如何运作的
        #首先要建立runtime.txt文档以描述我们使用的python环境
        #然后再建立requirements.txt以描述我们的程式在运行时所需要的套件
        #在Procfile文档里告诉Heroku如何执行我们的程式
    #第二步，安装Git工具
    #第三步，到Heroku上注册账号，并在Heroku上建立一个应用程式
    #第四步，安装Heroku命令列套件，即Heroku CLI
    #第五步，将专案部署到Heroku App并测试（这一步必须使用命令列模式执行）
        #在命令列上我们会写入heroku login
        #然后我们将会初始化专案
            #第一个命令：git init
            #第二个命令：heroku git:remote-a专案名称
        #之后是更新专案（每次有新的程式需要部署到云端时，都需要运行以下三个命令）
            #第一个命令：git add .
            #第二个命令：git commit-m "更新讯息，这里可以自己随便写"
            #第三个命令：git push heroku master