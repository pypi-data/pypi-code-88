UNDEFINED_RESULT = -2
import shutil,os
from .yuncheng_al_class import *
from .util_file import *
class Seral():
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
class YunchengAlResult(Seral):
    def __init__(self,filepath,jsonObj):
        self.filepath = filepath
        if jsonObj is None:
            self.code = 404
        else:
            self.lhClineRight = jsonObj.get("lhClineRight",UNDEFINED_RESULT)
            self.barcode = jsonObj.get("barcode",UNDEFINED_RESULT)
            self.lhCheckUrl = jsonObj.get("lhCheckUrl",UNDEFINED_RESULT)
            self.lhPaperAlType = jsonObj.get("lhPaperAlType",UNDEFINED_RESULT)
            self.lhClineLeft = jsonObj.get("lhClineLeft",UNDEFINED_RESULT)
            self.reverse = jsonObj.get("reverse",0)
            self.lhTlineLeft = jsonObj.get("lhTlineLeft",UNDEFINED_RESULT)
            self.errorCode = jsonObj.get("errorCode", 0)
            self.cLocation = jsonObj.get("cLocation", UNDEFINED_RESULT)
            self.code = jsonObj.get("code", 0)
            self.lhValue = jsonObj.get("lhValue", UNDEFINED_RESULT)
            self.lhTlineRight = jsonObj.get("lhTlineRight", UNDEFINED_RESULT)
            self.lhRatio = jsonObj.get("lhRatio", UNDEFINED_RESULT)
            self.tLocation = jsonObj.get("tLocation",UNDEFINED_RESULT)
class Compare(Seral):
    def __init__(self,filepath:str,result1:YunchengAlResult,result2:YunchengAlResult):
        self.filepath = filepath
        self.result1 = result1
        self.result2 = result2

    def compare_pre(self):
        if self.result1.code == 404 and self.result2.code != 404:
            return False
        if self.result1.code != 404 and self.result2.code == 404:
            return False
        return True

    def compare_value(self):
        key = "lhValue"
        v1 = self.result1.lhValue
        v2 = self.result2.lhValue
        return int(v1 != v2)

    def compare_line(self):
        '''
        1,一个有T，一个没有T

        :param result1:
        :param result2:
        :return:
        '''
        key1 = "lhTlineLeft"
        key2 = "lhTlineRight"
        key3 = "lhClineLeft"
        key4 = "lhClineRight"
        v1_key1 = self.result1.lhTlineLeft
        v2_key1 = self.result2.lhTlineLeft
        v1_key2 = self.result1.lhTlineRight
        v2_key2 = self.result2.lhTlineRight
        v1_key3 = self.result1.lhClineLeft
        v2_key3 = self.result2.lhClineLeft
        v1_key4 = self.result1.lhClineRight
        v2_key4 = self.result2.lhClineRight

        result = 0
        if (v1_key2 == 0 and v2_key2 != 0) or (v1_key2 != 0 and v2_key2 == 0):
            result = result ^ 0x01
        if (v1_key4 == 0 and v2_key4 != 0) or (v1_key4 != 0 and v2_key4 == 0):
            result = result ^ 0x02
        if result != 0:
            return result
        if v1_key2 != 0:
            if v1_key1 > v2_key2 or v1_key2 < v2_key1:
                result = result ^ 0x04
        if v1_key3 != 0:
            if v1_key3 > v2_key4 or v1_key4 < v2_key3:
                result = result ^ 0x08
        return result


    def compare_brand(self):
        key = "lhPaperAlType"
        v1 = self.result1.lhPaperAlType
        v2 = self.result2.lhPaperAlType
        return int(v1 != v2)

    def compare_direction(self):
        key = "reverse"
        v1 = self.result1.reverse
        v2 = self.result2.reverse
        return int(v1 != v2)

    def compare_al_result(self) -> 'Compare_result':
        compare_result = {"wrong": 0}
        if not self.compare_pre():
            compare_result['wrong'] = 1
            return compare_result
        brand_result = self.compare_brand()
        line_result = self.compare_line()
        direction_result = self.compare_direction()
        value_result = self.compare_value()
        return Compare_result(self.filepath,line_result,brand_result,direction_result,value_result,self.result1,self.result2)
    def save_compare_result(self):
        pass
class Compare_result(Seral):
    def __init__(self,file,line_result,brand_result,dirction_result,value_result,result1:YunchengAlResult,result2:YunchengAlResult):
        self.file = file
        self.line_result = line_result
        self.brand_result = brand_result
        self.dirction_result = dirction_result
        self.value_result = value_result
        self.result1 = result1
        self.result2 = result2
    def show_dif_brand_result(self,saveResult:[]):
        if self.brand_result != 0:
            saveResult.append({"file":self.file,"source":self.result1.lhPaperAlType,"compare":self.result2.lhPaperAlType})
    def show_dif_line_result(self,saveResult:[]):
        if self.line_result != 0:
            saveResult.append({"file":self.file,"source":[self.result1.lhTlineLeft,self.result1.lhTlineRight,self.result1.lhClineLeft,self.result1.lhClineRight,self.result1.reverse],
                              "compare":[self.result2.lhTlineLeft,self.result2.lhTlineRight,self.result2.lhClineLeft,self.result2.lhClineRight,self.result2.reverse]})
    def show_dif_value_result(self,saveResult:[]):
        if self.value_result != 0:
            saveResult.append({"file":self.file,"source":self.result1.lhValue,"compare":self.result2.lhValue})
    def show_dif_direction_result(self,saveResult:[]):
        if self.dirction_result != 0:
            saveResult.append({"file":self.file,"source":self.result1.reverse,"compare":self.result2.reverse})

class Get_result_and_compare():
    def __init__(self,url1,url2,picLocals,saveFile,useCache,url1ResultSavePath,url2ResultSavePath):
        print(f"test files:{len(picLocals)}")
        self.url1 = url1
        self.url2 = url2
        self.url1ResultSavePath = url1ResultSavePath
        self.url2ResultSavePath = url2ResultSavePath
        self.picLocals = picLocals
        self.saveFile = saveFile
        self.useCache = useCache
        if useCache:
            self.cache_init()
    def cache_init(self):
        try:
            with open(self.url1ResultSavePath,'r') as f:
                self.result1Cache = json.loads(f.read())
        except Exception as e:
            self.result1Cache = {}
        try:
            with open(self.url2ResultSavePath, 'r') as f:
                self.result2Cache = json.loads(f.read())
        except Exception as e:
            self.result2Cache = {}

    def cache_save(self):
        if self.useCache is True and self.url1ResultSavePath is not None and self.url2ResultSavePath is not None:
            with open(self.url1ResultSavePath,'w') as f:
                f.write(json.dumps(self.result1Cache))
            with open(self.url2ResultSavePath,'w') as f:
                f.write(json.dumps(self.result2Cache))
    def cache_insert(self,key,v,index):
        cache = self.result1Cache
        if index == 2:
            cache = self.result2Cache
        cache[key] = v

    def cache_get(self,key,index):
        cache = self.result1Cache
        if index == 2:
            cache = self.result2Cache
        return cache.get(key,None)
    def get_result(self,session,url,jsonData,index=1):
        result = None
        if self.useCache:
            id = jsonData['id']
            result = self.cache_get(id,index)
        if result is None:
            result = post_for_request(url, jsonData,session)
            if self.useCache:
                id = jsonData['id']
                self.cache_insert(id,result,index)
        return result



    def compare_two_pic_local(self):
        session = requests.session()
        lastResult = []
        for index,i in enumerate(self.picLocals):
            try:
                print(f"test:{index}")
                imdata = read_pic_to_base64(i)
                id = i
                jsonData = make_al_input(imdata,id)
                result1 = self.get_result(session, self.url1, jsonData,1)
                result2 = self.get_result(session, self.url2, jsonData,2)
                com = Compare(i,YunchengAlResult(i, result1),YunchengAlResult(i, result2))
                lastResult.append(com.compare_al_result())
            except Exception as e:
                print("error:{}".format(e))
        self.cache_save()
        self.lastResult = lastResult
    def summary(self):
        value_dif = []
        line_dif = []
        brand_dif = []
        direct_dif = []
        for i in self.lastResult:
            i.show_dif_direction_result(direct_dif)
            i.show_dif_line_result(line_dif)
            i.show_dif_value_result(value_dif)
            i.show_dif_brand_result(brand_dif)
        cou = 0
        for i in self.lastResult:
            if i.result1.lhPaperAlType == i.result2.lhPaperAlType and i.result1.lhPaperAlType in (7,8,9):
               cou += 1
        print("7,8,9 相同的共有:{}".format(cou))
        print(f"sum:{len(self.lastResult)},brand_dif:{len(brand_dif)},direct_dif:{len(direct_dif)},line_dif:{len(line_dif)},value_dif:{len(value_dif)}")
        lastResult = {"v":value_dif,"line":line_dif,"brand":brand_dif,"rever":direct_dif}
        with open(self.saveFile,'w') as f:
            f.write(json.dumps(lastResult))

class DecodeTheSummaryFile():
    def __init__(self,summaryFile,savePath):
        self.fig_number = 10
        self.summaryFile = summaryFile
        with open(summaryFile,'r') as f:
            data = f.read()
        data = json.loads(data)
        self.brand = data['brand']
        self.line = data['line']
        self.rever = data['rever']
        self.value = data['v']
        self.savePath = savePath
    def show_brand_dif(self):
        count = []
        for i in self.brand:
            if i['source'] in (7,8,9) or i['compare'] in (7,8,9):
                count.append(i)
        figIndex = 0
        for index,i in enumerate(count):
            if index % self.fig_number == 0:
                plt.figure(figsize=(10, 20))

            filepath = i['file']
            title = '{},source:{}-compare:{}'.format(os.path.basename(filepath),i['source'],i['compare'])
            data = cv2.imread(filepath)
            rows = index % self.fig_number + 1
            plt.subplot(self.fig_number,1,rows)
            plt.imshow(data[:,:,::-1])
            plt.title(title)
            if rows == 10 or index == len(count) - 1:
                plt.savefig(f'{self.savePath}/brand-{figIndex}.png')
                figIndex += 1
                # plt.show()
    def show_value_dif(self):
        for i in self.value:
            filepath = i['file']
            title = 'source:{}-compare:{}'.format(i['source'],i['compare'])
            data = cv2.imread(filepath)
            plt.imshow(data[:,:,::-1])
            plt.title(title)
            plt.show()
    def show_direction_dif(self):
        figIndex = 0
        for index,i in enumerate(self.rever):
            if index % self.fig_number == 0:
                plt.figure(figsize=(10, 20))
            rows = index % self.fig_number + 1
            plt.subplot(self.fig_number,1,rows)
            filepath = i['file']
            title = '{},source:{}-compare:{}'.format(os.path.basename(i['file']),i['source'],i['compare'])
            data = cv2.imread(filepath)
            plt.imshow(data[:,:,::-1])
            plt.title(title)
            if rows == 10 or index == len(self.rever) - 1:
                plt.savefig(f'{self.savePath}/dire-{figIndex}.png')
                figIndex += 1
                plt.show()

    def draw_line(self,filepath,line):
        imdata = cv2.imread(filepath)
        if line[4] == 1:
            imdata = setRotateJust180(imdata)
        h,w,_ = imdata.shape
        if line[0] > 0.1:
            t1 = int(w*line[0])
            t2 = int(w*line[1])
            imdata[h*3//4:,t1:t2,:] = (255,0,0)
        if line[2] > 0.1:
            c1 = int(w*line[2])
            c2 = int(w*line[3])
            imdata[h*3//4:,c1:c2,:] = (0,0,255)
        return imdata
    def show_line_dir(self):
        figIndex = 0
        for index,i in enumerate(self.line):
            filepath = i['file']
            if index % self.fig_number == 0:
                fig = plt.figure(figsize=(10, 25))
            rows = index % self.fig_number + 1

            plt.subplot(self.fig_number*2,1,rows*2-1)

            imdata1 = self.draw_line(filepath,i['source'])
            plt.imshow(imdata1[:,:,::-1])
            plt.title("source,reverse:{}".format(i['source'][4]))
            plt.subplot(self.fig_number*2,1,rows*2)
            imdata2 = self.draw_line(filepath,i['compare'])
            plt.imshow(imdata2[:,:,::-1])
            plt.title("compare,reverse:{}".format(i['compare'][4]))
            if rows == self.fig_number or index == len(self.line)-1:
                plt.savefig(f'{self.savePath}/line-{figIndex}.png')
                plt.show()
                figIndex+=1
    def get_brand_dif(self,save_dir):
        if os.path.exists(save_dir) is False:
            os.makedirs(save_dir)
        for i in self.brand:
            filepath = i['file']
            name = os.path.join(save_dir,os.path.basename(filepath))
            shutil.copy(filepath,name)
    def get_concrete_brand(self,id):
        # print(self.brand)
        for i in self.brand:
            if i['file'].find(id) != -1:
                print(i)
                break

    def summary_brand_dif(self):
        count = 0
        for i in self.brand:
            if i['source'] in (7,8,9) or i['compare'] in (7,8,9):
                count += 1
        print(count)
def com_two_pics_test(url1,savePath1,url2,savePath2,pics,summaryFile):
    '''
    将两个地址的算法结果进行对比，该程序会将结果进行缓存，如果发现该结果已经计算过则不再进行重复请求，
    :param url1: 地址1
    :param savePath1:  结果1保存位置
    :param url2: 地址2
    :param savePath2:  结果2保存位置
    :param pics:  本地图片地址集合['path1','path2']
    :param summaryFile:  对比结果保存位置
    :return: None
    '''
    g = Get_result_and_compare(url1, url2, pics, summaryFile, True, savePath1, savePath2)
    g.compare_two_pic_local()
    g.summary()

def analysis_summary_result(summaryFile,difSavePath):
    '''
    对比对结果进行解读
    :param summaryFile: 比对结果
    :param difSavePath:  不同结果进行标准后保存的位置
    :return: None
    '''
    dif = DecodeTheSummaryFile(summaryFile,difSavePath)
    dif.show_brand_dif()
    dif.show_line_dir()
    dif.show_direction_dif()
    dif.show_value_dif()
