"""
# @Time    : 12/2/2021 15:07
# @Author  : leandro.batlle@gmail.com
# @File    : test_refi_qda.py

"""

from portableqda.refi_qda import codeSetDict, codebookCls, etree, ENCODING, codeCls, setCls
from pprint import pprint
import portableqda
import nose


import logging,sys,pathlib
#handler = logging.StreamHandler(sys.stderr)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
portableqda.refi_qda.log.addHandler(handler)
portableqda.log.setLevel(logging.DEBUG)

def refi_qda_all():
    """
    run all tests for this pachage

    :return:
    """
    test_0_run_this_first()
    test_codeSetDict_class()



def test_0_run_this_first():
    portableqda.log.warning("+="*40)
    print(f"""test_0_run_this_first():  PortableQDA.refi_qda TEST SET 
most output is via interpreter_s logger. if you don't see something like **general notes on test_refi.qda.py**
on the next few lines plaese adjust your logger. 
- nosetest might need the -s modifier. Other runners... ¯\_(ツ)_/¯
```python
# interpeter logger prep
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
portableqda.refi_qda.log.addHandler(handler)
portableqda.log.setLevel(logging.DEBUG)    
```
    """)
    portableqda.log.warning("test_0_run_this_first(): general notes on test_refi.qda.py tests set")
    portableqda.log.warning("...test_0_run_this_first... if you don't some tests might fail")
    portableqda.log.warning("+="*40)


#@nose.SkipTest
def test_codeSetDict_class():
    """
    test class codeSetDict, index for members of the CodeBook. See comments here

    :return:
    """
    portableqda.log.warning("+"*80)
    portableqda.log.warning(f" test_codeSetDict_class() starts")

    #
    #  codeSetDict constructor needs a list for memberTypes
    #
    try:
        myCodeSetDict = codeSetDict(memberTypes=None)
    except ValueError as e:
        if str(e).find("sequence") == -1:
            raise
    myCodeSetDict = codeSetDict(memberTypes=(int, float))

    #
    #  codeSetDict constructor does not populate the underlying dict in any way
    #
    assert len(myCodeSetDict.keys()) == 0

    #
    # codeSetDict tells you if an item will be wellcomed
    #
    assert not myCodeSetDict.allowType(str)
    assert myCodeSetDict.allowType(int)

    #
    #  codeSetDict raises ValeuError when a new meber's type is not listed in memberTypes
    #
    try:
        myCodeSetDict["non-existant key"] = "bad type"
        pass
    except ValueError as e:
        if str(e).find("memberTypes") == -1:
            raise
        portableqda.log.info(f"OK codeSetDict rejects new member with message '{e}'")
    except Exception as e:
        raise
    else:
        raise NotImplementedError("class codeSetDict accepts types not in 'memberTypes'")

    #
    #  codeSetDict behaves as defaultDict
    #
    var = myCodeSetDict["non-existant key"]
    assert var is None
    assert "non-existant key" in myCodeSetDict.keys()
    myCodeSetDict["non-existant key"] = 10
    assert myCodeSetDict["non-existant key"] == 10
    myCodeSetDict["key2"] = myCodeSetDict["non-existant key"] / 2
    assert myCodeSetDict["key2"] == 5 / 1
    portableqda.log.warning("+"*80)
    portableqda.log.warning(f" test_codeSetDict_class()  ends SUCCESFULLY :)")


def test_create_code(codebook=None):
    """
    test code creation.

    if codebook parameter provided, resuses an existing codebookCls object

    :param codebook:
    :return:
    """
    portableqda.log.warning(f"test_create_code({codebook}): starts")
    portableqda.log.warning("+"*80)

    testCodeNames=["code1","code2"]#,"code3",]
    if codebook is None:
        codebook = codebookCls()
    else:
        portableqda.log.debug("test_create_set(): operating in codebook passed as argument")
    r = portableqda.resultCls #wrapper class, namedtuple(error,errorDesc,result)
    #
    # create a new code
    #
    portableqda.log.info("="*80)
    portableqda.log.info("create a new code")
    portableqda.log.info("="*80)
    code1params={"elementCls":codeCls, "name":testCodeNames[0],"guid":"FAKE-GUID-FAKE-GUID-FAKE-1111","color":"#a1a2a3", "description":"desc1"}
    createdCode=r(*codebook.createElement(**code1params))
    # error should pop
    assert createdCode.error, f"codebook.createElement with a nonexiting GUID should complain"
    portableqda.log.warning("it's OK to ignore the previous line: ERROR 'elementCls.__init__: called with guid, so it should be in etree (tipically when reading a QDC file)'")
    code1params={"elementCls":codeCls, "name":testCodeNames[0],"color":"#a1a2a3", "description":"desc1"}
    createdCode=r(*codebook.createElement(**code1params))
    # no error should pop
    assert not createdCode.error, f"codebook.createElement error: {createdCode.errorDesc}"
    # check each code atrribute for correctness
    for paramKey in code1params.keys():
        if paramKey not in ("elementCls",):
            assert code1params[paramKey] == getattr(createdCode.result,paramKey),  f"{paramKey} should be '{code1params[paramKey]}' but is {getattr(createdCode.result,paramKey)}"
    pass
    #
    # create another code, pretending the etree elemente was read from a file (with an invalid uid)
    #
    portableqda.log.info("="*80)
    portableqda.log.info("create another code, pretending the etree element was read from a file (with an invalid uid)")
    portableqda.log.info("="*80)
    fakeGuid="FAKE-GUID-FAKE-GUID-FAKE-1111"
    portableqda.log.info(f"test_create_code(): faking guid of {codebook.codes[testCodeNames[0]]}, to simulate a flawed QDC file")
    codebook.codes[testCodeNames[0]].etreeElement.attrib["guid"]=fakeGuid #breaking abstraction just one, promes
    code2params={"elementCls":codeCls, "guid":fakeGuid, "name": testCodeNames[1],"bogusParam":"ignore this"}
    createdCode2=r(*codebook.createElement(**code2params))
    portableqda.log.info(f"test_create_code(): created another code '{createdCode2.result.name}' check for consistency")
    for codeName in testCodeNames:
        assert codeName in codebook.codes.keys(), f"codeName '{codeName}' NOT in codebook.codes.keys(): '{codebook.codes.keys()}' "
        assert codeName == codebook.codes[codeName].name, f"wrong codeName '{codebook.codes[codeName].name}', should be '{codeName}' "
    portableqda.log.warning(f" please run test_code_set_relation() in order to test set membership")
    portableqda.log.warning("+"*80)
    portableqda.log.warning(f"test_create_code({codebook}): ends SUCCESFULLY :)")


def test_create_set(codebook=None):
    """
    test set creation

    :param codebook:
    :return:
    """
    portableqda.log.warning(f"test_create_set({codebook}): starts")
    portableqda.log.warning("+"*80)
    testSetNames=["set1","set2",]
    if codebook is None:
        codebook = codebookCls()
    else:
        portableqda.log.debug("test_create_set(): operating in codebook passed as argument")
    r = portableqda.resultCls #wrapper class, namedtuple(error,errorDesc,result)
    #
    # create a new set
    #
    portableqda.log.info("="*80)
    portableqda.log.info("create a new set")
    portableqda.log.info("="*80)
    set1params = {"elementCls": setCls, "name": testSetNames[0], "guid": "FAKE-GUID-FAKE-GUID-FAKE-1111",
                   "color": "#a1a2a3", "description": "desc1"}
    createdSet = r(*codebook.createElement(**set1params))
    # error should pop
    assert createdSet.error, f"codebook.createElement with a nonexiting GUID should complain"
    portableqda.log.warning(
        "it's OK to ignore the previous line: ERROR 'elementCls.__init__: called with guid, so it should be in etree (tipically when reading a QDC file)'")
    set1params = {"elementCls": setCls, "name": testSetNames[0], "color": "#a1a2a3", "description": "desc1"}
    portableqda.log.warning("color should be ignored as per REFI-QDa 1.5 ")
    createdSet = r(*codebook.createElement(**set1params))
    del set1params["color"]
    # no error should pop
    assert not createdSet.error, f"setbook.createElement error: {createdSet.errorDesc}"
    # check each set atrribute for correctness
    for paramKey in set1params.keys():
        if paramKey not in ("elementCls",):
            assert set1params[paramKey] == getattr(createdSet.result,paramKey),\
                f"{paramKey} should be '{set1params[paramKey]}' but is {getattr(createdSet.result, paramKey)}"
    pass
    #
    # create another set, pretending the etree elemente was read from a file (with an invalid guid)
    #
    portableqda.log.info("="*80)
    portableqda.log.info(" create another set, pretending the etree elemente was read from a file (with an invalid guid)")
    portableqda.log.info("="*80)
    fakeGuid="FAKE-GUID-FAKE-GUID-FAKE-1111"
    portableqda.log.info(f"test_create_code(): faking guid of {codebook.codes[testSetNames[0]]}, to simulate a flawed QDC file")
    codebook.sets[testSetNames[0]].etreeElement.attrib["guid"]=fakeGuid #breaking abstraction just one, promes
    set2params = {"elementCls": setCls, "guid": fakeGuid, "name": testSetNames[1],
                   "bogusParam": "ignore this"}
    createdSet2 = r(*codebook.createElement(**set2params))
    assert not createdSet2.error, f"setbook.createElement error: {createdSet2.errorDesc}"
    portableqda.log.info(
        f"test_create_set(): created another set '{createdSet2.result.name}' check for consistency")
    for setName in testSetNames:
        assert setName in codebook.sets.keys(), f"setName '{setName}' NOT in codebook.sets.keys(): '{codebook.sets.keys()}' "
        assert setName == codebook.sets[setName].name, f"wrong setName '{codebook.sets[setName].name}', should be '{setName}' "
    portableqda.log.warning("+"*80)
    portableqda.log.warning(f"test_create_set({codebook}): ends SUCCESFULLY :)")



def test_code_set_relation():
    """
    test various operations on sets (append codes, etc)

    :return:
    """
    portableqda.log.warning(f"test_code_set_relation(): starts")
    portableqda.log.warning("+"*80)

    testSetNames=["set1","set2","set3"] # in test_set_creation()    testSetNames=["set1","set2",]
    testCodeNames=["code3"]#,"code4"]

    codebook = codebookCls()
    r=portableqda.resultCls
    #
    # precondition: create a unlated sets and codes
    #
    portableqda.log.info("test_code_set_relation(): suppresing log output while executing:     test_create_code(codebook); test_create_set(codebook)")
    portableqda.log.setLevel(logging.FATAL)
    test_create_code(codebook)
    test_create_set(codebook)
    portableqda.log.setLevel(logging.DEBUG)
    portableqda.log.info("test_code_set_relation(): resuming  log output")
    #
    # append existing code1 to exisiting set1, code2 to set2
    #
    portableqda.log.info("="*80)
    portableqda.log.info("append existing code1 to exisiting set1, code2 to set2")
    portableqda.log.info("=" * 80)
    result=r(*codebook.sets["set1"].memberCodeAppend(codebook.codes["code1"]))
    assert not result.error, f"error Appending code 'code1' to 'set1': {result.errorDesc}"
    assert codebook.sets["set1"].memberCodes["code1"] is not None, f"'code1' not a member of 'set2', but there was no error codition ...'{result.errorDesc}'"
    #[ code for code in codebook.sets["set1"].memberCodes if code is not None ], current members are {codebook.sets['set1'].memberCodes.keys()}"
    codebook.sets["set2"].memberCodeAppend(codebook.codes["code2"])
    assert codebook.sets["set2"].memberCodes["code2"] is not None, f"'code2' not a member of 'set2'"
    portableqda.log.info("good.")
    #
    # create now code3 into new set3. invaluid Guid. should break
    #
    portableqda.log.info("=" * 80)
    portableqda.log.info("create new code3 into new set3. invalid Guid. should break")
    portableqda.log.info("=" * 80)
    name=testCodeNames[0]+"fail"
    code1params={"elementCls":codeCls, "name":name,"guid":portableqda.refi_qda.valid_guid(name=name),
                "sets":testSetNames,"color":"#a1a2a3", "description":name}
    portableqda.log.warning(f"test_code_set_relation(): next couple of errors are normal: complaints about  set 'set3' not being  found are expected because  'guid' was provided")
    createdCode=r(*codebook.createElement(**code1params))
    assert createdCode.error, f"calling codebook.createElement with invalid Guid ({code1params['guid']}) should break"
    portableqda.log.info(f"last error is normal, calling codebook.createElement with invalid Guid should break, received error '{createdCode.errorDesc}'")
    assert codebook.sets["set3"] is None, f"'set3' should not exist yet"
    portableqda.log.info("good.")
    #
    # create new code3ok into new set3. shuold work
    #
    portableqda.log.info("=" * 80)
    portableqda.log.info("create new code3ok into new set3. shuold work")
    portableqda.log.info("=" * 80)
    code1params["guid"]=None
    code1params["name"] = code1params["name"].replace("fail","ok")
    portableqda.log.debug(f"test_code_set_relation(): set 'set3' shoud NOW be created by createElemtn() because not 'guid' was provided")
    createdCode=r(*codebook.createElement(**code1params))
    assert not createdCode.error, f"codebook.createElement error: {createdCode.errorDesc}"
    assert isinstance(codebook.sets["set3"],setCls), f"'set3' should not exist by now. but codebook.sets['set3']=={codebook.sets['set3']}"
    #assert createdCode.result.name in codebook.sets["set3"].memberCodes, f"'code3' not a member of 'set3'"
    assert codebook.sets["set3"].memberCodes[createdCode.result.name] is not None, f"'{createdCode.result.name}' not a member of 'set3'"
    portableqda.log.info("good.")
    #
    # remove code3ok from set3
    #
    portableqda.log.info("=" * 80)
    portableqda.log.info("remove code3ok from set3")
    portableqda.log.info("=" * 80)
    codebook.sets["set3"].memberCodeAppend(codebook.codes["code1"])
    codebook.sets["set3"].memberCodeAppend(codebook.codes["code2"])
    result=r(*codebook.sets["set3"].memberCodeRemove(createdCode.result))
    assert not result.error, f"set3.memberCodeRemove({createdCode.result.name}) resulted in error: '{result.errorDesc}'"
    assert len(result.result) == 2, f"wrong number of memberCodes: {len(result.result)}, sholud be 2"
    assert not createdCode.result.name in list(result.result), f" '{createdCode.result.name}' should not be in 'set3' anymore but meberCodes are {result.result} "
    assert codebook.sets["set3"].memberCodes[createdCode.result.name] is None, f"'{createdCode.result.name}' not a member of 'set3'"
    portableqda.log.warning("+"*80)
    portableqda.log.warning(f"test_code_set_relation(): ends SUCCESFULLY :)")



#@nose.SkipTest
def test_codebookCls_writeQdc():
    portableqda.log.warning(f"test_codebookCls_writeQdc(): starts")
    portableqda.log.warning("+"*80)
    f_out="portableQDA_test.qdc"
    codebook = codebookCls()
    codebook.writeQdcFile()  # stdout
    codebook = codebookCls(output=f_out)  # home directory, all platforms
    for number in range(4):
        if number%2:
            sets = ["setAll"]
        else:
            sets=["setAll", "setEven"]
        codebook.createElement(elementCls=portableqda.codeCls,
                                                name=f"code{number}",
                                                description=f"code{number} - description",
                                                sets=sets)
    #incept some unsupported features
    _=etree.SubElement(codebook.sets["setAll"].etreeElement, "MemberNote")
    codebook.sets["setAll"].etreeElement.attrib["guid"]="FAKE-GUID-FAKE-GUID-GUID"
    #same as this?? etree.SubElement(codebook.sets["setAll"].etreeElement, "MemberSource").attrib["guid"]="-GUID-GUID-GUID-GUID"
    codebook.writeQdcFile()
    portableqda.log.info(f"test complete, look for the file {f_out} at your home directory")
    portableqda.log.warning("+"*80)
    portableqda.log.warning(f"test_codebookCls_writeQdc(): ends SUCCESFULLY :)")


#@nose.SkipTest
def test_codebookCls_readQdc():
    portableqda.log.warning(f" test_codebookCls_readQdc(): starts")
    portableqda.log.warning("+"*80)
    f_out="portableQDA_test_output.qdc"
    portableqda.log.info("suppresing log output while executing: test_codebookCls_writeQdc()")
    portableqda.log.setLevel(logging.FATAL)
    test_codebookCls_writeQdc()
    portableqda.log.setLevel(logging.DEBUG)
    portableqda.log.info("resuming log output after executing: test_codebookCls_writeQdc()")
    codebook = codebookCls(output=f_out)
    codebook.readQdcFile(input=str(pathlib.Path(".").home() / f_out.replace("_output","")))
    # codebook.input = "portableQDA_test.qdc"
    # codebook.readQdcFile()  # input param cis optional if already as object attribute
    codebook.writeQdcFile()
    #assert compare
    portableqda.log.info(f"INFO: test_codebookCls_readQdc() complete, look for the file {f_out} at your home directory")
    portableqda.log.warning("+"*80)
    portableqda.log.warning(f" test_codebookCls_readQdc(): ends SUCCESFULLY :)")


#@nose.SkipTest
def test_codebookCls_roundtrip_REFIQDA1_5():
    """
    test roudtrip import/export using the appendix A of the REFI-QDA 1.5 Standard (Sets tag added for completeness)

    see https://www.qdasoftware.org/wp-content/uploads/2019/09/REFI-QDA-1-5.pdf

    :return:
    """
    portableqda.log.warning(f"test_codebookCls_roundtrip_REFIQDA1_5() starts")
    portableqda.log.warning("+"*80)
    file = {"initial": "REFI-QDA-1-5.qdc",
            "intermediate": "REFI-QDA-1-5_test.qdc",
            "final": "REFI-QDA-1-5_test2.qdc"}
    codebook = codebookCls(output=file["intermediate"])
    codebook.readQdcFile(input=str (pathlib.Path("tests") / file["initial"]))
    codebook.writeQdcFile()
    codebook2 = codebookCls(output=file["final"])
    #portableqda.log.error(f"input= str(codebook.output)=='{str(codebook.output)}'")
    #assert False
    codebook2.readQdcFile(input= str(codebook.output) ) # same as  pathlib.Path.home() / file["intermediate"]
    codebook2.writeQdcFile()
    # compare the two outputs
    with open(codebook.output, encoding=ENCODING) as fh:
        with open(codebook2.output, encoding=ENCODING) as fh2:
            pass
            compare = fh.read() == fh2.read()
    assert compare
    # with open(codebook.output,mode="rb") as fh:
    #    codebook.tree2=etree.fromstring(fh.read())
    portableqda.log.warning("+"*80)
    portableqda.log.warning(f"test_codebookCls_roundtrip_REFIQDA1_5() ends SUCCESFULLY :)")


#@nose.SkipTest
def test_codebookCls_roundtrip_atlasti():
    """
    test roundtrip import/export using a codebook from ATLAS.ti 9.0

    see https://www.atlasti.com

    :return:
    """
    portableqda.log.warning(f" test_codebookCls_roundtrip_atlasti(): starts")
    portableqda.log.warning("+"*80)
    file = {"initial": "portableQDA_Atlasti.qdc",
            "intermediate": "portableQDA_Atlasti_test2.qdc",
            "final": "portableQDA_Atlasti_test3.qdc"}
    codebook = codebookCls(output=file["intermediate"])
    codebook.readQdcFile(input=str (pathlib.Path("tests") / file["initial"]))
    codebook.writeQdcFile()
    codebook2 = codebookCls(output=file["final"])
    codebook2.readQdcFile(input= str(codebook.output) )  #same as pathlib.Path.home() / file["intermediate"]
    codebook2.writeQdcFile()
    # compare the two outputs
    with open(codebook.output, encoding=ENCODING) as fh:
        with open(codebook2.output, encoding=ENCODING) as fh2:
            pass
            compare = fh.read() == fh2.read()
    assert compare
    portableqda.log.warning("+"*80)
    portableqda.log.warning(f" test_codebookCls_roundtrip_atlasti(): ends SUCCESFULLY :)")



@nose.SkipTest
def test_codebookCls_compareQdc():
    """
    test suspendended since rel 0.3

    :return:
    """
    portableqda.log.warning(f"test_codebookCls_compareQdc starts")
    portableqda.log.warning("+"*80)
    r=portableqda.resultCls
    codebookOld = codebookCls(output="portableQDA_compareQDC_Old.qdc")
    #
    # create two codebooks to compare
    #
    #  codebookOld = one code to delete (code1)
    #  codebookOld = one code and one set to keep  (___2)

    #set1 discard error state
    codebookOld.createElement(elementCls=setCls, #codebook elements are codeCls or setClas
                                                name="set1-Delete",
                                                description="set only in old codebook")
    set2=r(*codebookOld.createElement(elementCls=setCls, #codebook elements are codeCls or setClas
                                                name="set2-Common",
                                                description="set in both codebooks"))
    #check set2.error...
    error, errorDesc, code1 = codebookOld.createElement(elementCls=codeCls, name="code1-Delete",
                                                    description="code only in old codebook", sets=[set2.result.name,])
    code2 = r(*codebookOld.createElement(elementCls=codeCls, name="code2-Common",
                                                    description="test code  in both codebooks Desc", sets=None))
    #
    # New codebook
    #
    codebookNew = codebookCls(output="portableQDA_compareQDC_New.qdc")
    set2new=r(*codebookNew.createElement(elementCls=setCls, #codebook elements are codeCls or setClas
                                         name=set2.result.name,
                                         description=set2.result.description,
                                         guid=set2.result.guid))
    code2new = r(*codebookNew.createElement(elementCls=codeCls, name=code2.result.name+"-new name",
                                            description=code2.result.description+"-new name", guid=code2.result.guid,
                                            sets=[set2new.result.name,]))
    code3 = r(*codebookNew.createElement(elementCls=codeCls, name="code3-New",
                                            description="code3 new to de new codebook",
                                            sets=[set2new.result.name,]))
    #
    # write codebooks
    #
    codebookOld.writeQdcFile()
    codebookNew.writeQdcFile()
    #
    # compare with no destination
    #
    portableqda.log.info("compareQDC with destination set to None (no postprocessing)")
    codebookOld.compareQdc(codebook=codebookNew, IamOlder=True, destination=None)
    codebookOld.writeQdcDiff(suffix="-DestinationDefault")

    #
    # compare with  destination="atlas9"
    #
    portableqda.log.info("compareQDC with destination (postprocessing) set atlas9")
    codebookOld.compareQdc(codebook=codebookNew, IamOlder=True, destination="atlas9")
    #codebookOld.writeQdcDiff(suffix=".qdc") #sub-testcase
    codebookOld.writeQdcDiff(suffix="-DestinationAtlas9.qdc")
    portableqda.log.warning("+"*80)
    portableqda.log.warning(f"test_codebookCls_compareQdc ends SUCCESFULLY :)")
