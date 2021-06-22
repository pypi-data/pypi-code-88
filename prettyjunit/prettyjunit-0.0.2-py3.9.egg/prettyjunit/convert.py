import xml.etree.ElementTree as ET
import glob
import json
import os
import sys

def generate_html():
    try:
        if (sys.argv[1] == "-help"):
            print("--------------------------------Command Usage----------------------------------------------\n"
                  "prettyjunit <folder_path_containing_junit_xml_reports> <report_name>")
        else:
            path = sys.argv[1]
            if (len(sys.argv) == 3):
                reportname = sys.argv[2]
            else:
                reportname = "Test Summary"
            count = 0
            passCount = 0
            failCount = 0
            skipCount = 0
            testSuites = glob.glob(path+"/*.xml")
            testSuites.sort(key=os.path.getmtime)

            suiteData = []
            suiteRow={}
            cwd = os.path.dirname(os.path.realpath(__file__)).replace("\\\\","/")
            f = open(cwd+"/report_template.html", "r")
            suiteTemplateContent = f.read()
            f.close()
            for testsuite in testSuites:
                et = ET.parse(testsuite)
                root = et.getroot()
                suiteRow['name'] = root.get("name").split(".")[-1]
                suiteRow['tests'] = root.get("tests")
                suiteRow['fail'] = root.get("failures")
                suiteRow['skipped'] = root.get("skipped")
                suiteRow['time'] = root.get("time")
                suiteRow['pass'] = str(int(suiteRow['tests']) - (int(suiteRow['fail'])+int(suiteRow['skipped'])))
                suiteRow['passPc'] = str(round(int(suiteRow['pass'])/int(suiteRow['tests'])*100, 2))+" %"
                passCount += int(suiteRow['pass'])
                failCount += int(suiteRow['fail'])
                skipCount += int(suiteRow['skipped'])
                testData = []
                for child in root:
                    testRow = {}
                    if child.get("name"):
                        testRow['name'] = child.get("name")
                        testRow['time'] = child.get("time")
                        if not len(list(child)):
                            testRow['pass'] = "passed"
                            testRow['fail'] = ""
                            testRow['skipped'] = ""
                        else:
                            for status in child:
                                testRow['pass'] = ""
                                if status.tag == "failure":
                                    testRow['fail'] = "failed"
                                    testRow['_children'] = {"error":status.text}
                                elif status.tag== "skipped":
                                    testRow['skipped'] = "skipped"
                        testData.append(dict(testRow))
                        count += 1
                        suiteRow['_children'] = testData
                    else:
                        #print(child)
                        pass
                suiteData.append(dict(suiteRow))
            passPc = str(round((passCount/count)*100,2)) +" %"
            failPc = str(round((failCount/count)*100,2)) +" %"
            skipPc = str(round((skipCount/count)*100,2)) +" %"
            f=open(path+"/summary.html","w")
            suiteContent = suiteTemplateContent.replace("var tableData = [];", "var tableData = " + json.dumps(suiteData) + ";")
            suiteContent = suiteContent.replace("Total_Count", str(count)).replace("Failed_Count", str(failCount)+"("+failPc+")")\
                .replace("Passed_Count", str(passCount)+"("+passPc+")").replace("Skipped_Count", str(skipCount)+"("+skipPc+")")
            suiteContent = suiteContent.replace("Report_Name",reportname)
            f.write(suiteContent)
            f.close()
            print("Report Generated Successfully, Summary.html generated at "+ path)
    except Exception as e:
        print("Error:\n"+str(e))
        print("Please type prettyjunit -help for usage instructions")
