#这一节首先我们学习如何编写一段网站程式（在上传云端之前，网站程式必须24h运行，否则一旦停掉就无法登录网站；且你只能在你自己的电脑上打开这个网站）
from flask import Flask
app=Flask(__name__)#__name__是Python内建的一个变数，可以用来储存目前这个程式在哪个模组下执行

@app.route("/")#这是函式的装饰：以函式为基础基础，提供一些附加的功能
def home():
    return "Hello Flask!\nFuckyou Flask!"

@app.route("/test")#我们可以将其理解为：这是网站的子页面。具体内容看最后的备注
def test():
    return "This is a test."

@app.route("/zhairui")
def zhairui():
    return "蛆瑞我是你爹略略略"

@app.route("/jiaxin")
def jiaxin():
    return "鑫哥牛逼"

if __name__=="__main__":#如果__name__以主程式运行
    app.run()#那么就启动伺服器

#比如说，以网站 http://127.0.0.1:5000/test 为例：
    #http://127.0.0.1:5000 是网站的“主机”，你可以理解为一个网站的主页
    #/ 是网站的“根目录”
    #test 是网站的“子目录”，你可以理解为一个网站的子页面



#接下来我们学习如何将自己制作的网站上传至云端
    #首先，我们需要在Visual Studio Code上编写Python Flask程式
        #先编写主档案app.py
        #然后创建runtime.txt，在里面输入我们使用的Python版本（即python-3.14.4）
        #接着创建requirements.txt，在里面输入我们所使用到的套件（即Flask和gunicorn）
        #最后创建一个Procfile，告诉render我们的程序应当如何运行
    #然后，将编写的Python Flask程式上传至Github的代码库保存
        #先在Github首页创建一个代码库
        #然后在Visual Studio Code中依次执行：
            #git init（这一步是为了初始化本地Git仓库）
            #git add .（这一步是为了将项目文件添加到暂存区）
            #git commit -m "First commit"
        #在输入这行代码之后，会要求你输入你的用户名和邮箱（如果没要求就不用管它）:
            #git config --global user.name "你的用户名"
            #git config --global user.email "你的邮箱"
        #接下来，需要将本地仓库连接到我们上一步中所创建的Github代码库
            #git branch -M main
            #git remote add origin https://github.com/"Github用户名"/"代码库名称"
            #git push -u origin main
    #接着，我们就可以在Render上直接将网站部署到云端了
        #先在首页新建一个web service
        #然后选择build and deploy from a Git repository
        #在面板中设置我们的Render部署设置
            #其中，Region选择离主要使用者最近的地区
            #其中，构建命令Buid command选择pip.install -r requirements.txt
            #其中，启动命令Start command选择gunicorn app:app --bind 0.0.0.0:$PORT
                
            #其中，实体配置Instance Type可以选择$0的那个