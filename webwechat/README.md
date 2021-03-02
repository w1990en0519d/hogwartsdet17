# 三种等待方式 例子：test_address

直接等待：sleep，等待指定时间内 隐式等待：implicitly_wait，在指定时间内，轮询查看是否符合要求（全局的） 显式等待：WebDeriverWait，在指定时间内，轮询查看是否符合要求（个别的）

# PO设计模式 例子：login_page

page类中包含功能页，功能页面包含具体的操作步骤