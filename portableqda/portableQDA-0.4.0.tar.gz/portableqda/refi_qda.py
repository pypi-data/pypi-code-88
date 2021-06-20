"""
portableQDA Core module: QDA projects, codebooks, codes, sets, constants.

The  Rotterdam  Exchange  Format  Initiative  (REFI),  responsible  for  the  interoperability  standard
described  in  this  document,  originated  in  September  2016  as  a  result  of  the  KWALON  Conference:
Reflecting on the Future of QDA Software, held at Erasmus University Rotterdam. Software developers
attending  the  conference  agreed  to  work  together  in  developing  an  exchange  format,  thus  en

[PDF](https://www.qdasoftware.org/wp-content/uploads/2019/09/REFI-QDA-1-5.pdf)


"""
import typing,uuid,re,platform,inspect,logging,pathlib,datetime
from enum import  Enum
import lxml.etree as etree
from portableqda import __version__
# from xmldiff import main as xmld #made optional dependency and moved to codebookCls.compareQDC()
# from xmldiff import actions as xmlda #made optional dependency and moved to codebookCls.compareQDC()
from portableqda import resultCls
from pprint import pprint

__all__ = ["log","etree"] #depends
__all__ +=["CATEGORY_SEP","ENCODING","guidRe"]  #constants
__all__ +=["codebookCls","codeCls","setCls"] #interface
#__all__ +=["TAG_SET","TAG_CODE"] #tags
#__all__ +=[] #
#__all__ +=[] #
#__all__ +=[] #

def _trace(self, message, *args, **kws):
    if self.isEnabledFor(logging.DEBUG - 1):
        self._log(logging.DEBUG - 1, message, args, **kws)  # pylint: disable=W0212

logging.addLevelName(logging.DEBUG - 1, "TRACE")
logging.Logger.trace = _trace  # type: ignore

logger = logging.getLogger
log = logger(__name__)

parser = etree.XMLParser()

CATEGORY_SEP = "::"
ENCODING = "utf-8"
CODEBOOK_UNPOPULATED=b"""<?xml version="1.0" encoding="UTF-8"?>
            <CodeBook xmlns="urn:QDA-XML:codebook:1.0" xmlns:qda="urn:QDA-XML:codebook:1.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="urn:QDA-XML:codebook:1.0 http://schema.qdasoftware.org/versions/Codebook/v1.0/Codebook.xsd"><Codes/><Sets/></CodeBook>"""
TAG_DESC="Description"
TAG_CODE="Code" #expected container is TAG_CODE+"s", "Codes"
TAG_SET="Set" #expected container is TAG_SET+"s"
TAG_SET_MEMBERCODE = "MemberCode"
CODES_ID = 0 #order of the container in the codebook
SETS_ID = 1 #order of the container in the codebook
class compOp(Enum): #tag the elements for re-importing on apps that does not support codebook updatng
    N="NotChanged"
    C="Created"
    U="Updated"
    D="Deleted"

# GUIDType, The schema can be accessed online at http://schema.qdasoftware.org/versions/Codebook/v1.0/Codebook.xsd
guidRe=re.compile("([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})")
# RGBType, The schema can be accessed online at http://schema.qdasoftware.org/versions/Codebook/v1.0/Codebook.xsd
colorRe=re.compile("#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})")

LOCAL_NAMESPACE = uuid.uuid3(uuid.NAMESPACE_DNS,platform.node()*2)

class elementCls:
    def __init__(self):
        # protectect attributes
        self._guid=None
        self._name=None
        self._etreeElement=None #

    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, value):
        if self._guid is None:
            self._guid = value
        elif self._guid != value:
            log.warning(f"changing element guid from {self._guid} to {value}")
            self._guid = value
            #raise ValueError("element guid cannot be changed")
        if self._etreeElement is None:
            #log.warning("element has no etree")
            pass
        else:
            if "guid" in self._etreeElement.attrib.keys() and \
                    self._etreeElement.attrib["guid"] != self._guid:
                log.debug(f"updating guid in tree from {self._etreeElement.attrib['guid']} to {self._guid}")
            self._etreeElement.attrib["guid"]=self._guid

    @property
    def etreeElement(self):
        return self._etreeElement

    @etreeElement.setter
    def etreeElement(self, value):
        if self._etreeElement is None:
            self._etreeElement = value
        else:
            raise ValueError("element etreeElement cannot be changed")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self._name is not None:
            log.warning(f"element's name chaged from {self._name} to {value} (guid: {self._guid})")
        self._name = value
        if self._etreeElement is None:
            #log.warning("element has no etree")
            pass
        else:
            self._etreeElement.attrib["name"]=value

    def __repr__(self):
        return f"portableqda.{self.TAG}:{self._name}:{self._guid}"

def valid_guid(guid=None,name=None):
    """
    if 'guid' is None,returns a valid GUID (as per REFI-QDa 1.5) using 'name' or the current time as seed.
    if 'guid' is not a valid GUID (as per REFI-QDa 1.5) returns a valid one using 'name' or the current time as seed.
    if 'guid' is  valid, it is returned untouched

    :param guid: None or a REFI-QDA 1.5 valid GUID
    :param name: None, element name or a random string
    :return:  a valid GUID (as per REFI-QDa 1.5)
    """
    result=guid
    if guid is None or not re.match(guidRe,guid):
        if guid is None:
            log.debug("valid_guid(): generating new GUID, guid is None")
        else:
            log.debug(f"valid_guid(): generating new GUID, '{guid}' doesn't re.match({guidRe.pattern})")
        if name is None:
            import time
            name = time.strftime("%s", time.gmtime())
        result = str(uuid.uuid5(LOCAL_NAMESPACE, name)).upper()
    return result

def valid_color(color=None):
    result=color
    if color is None or not re.match(colorRe,color):
        result = "#000000"
    return result

class codeSetDict(typing.MutableMapping):
    """defaultDict with type validation upon item creation

    based on: https://stackoverflow.com/questions/3387691/how-to-perfectly-override-a-dict
    """
    def __init__(self, memberTypes: list):
        if isinstance(memberTypes, typing.Sequence):
            self._memberTypes = memberTypes
        else:
            raise ValueError("ERR: a sequence containing types has to be passed as argument to 'memberTypes'")
        self._store = dict()
        #keys = self._store.keys # not needed, using __iter__ ?

    def __getitem__(self, key):
        #return self._store.setdefault(key, None)
        return self._store.get(key, None)

    def __setitem__(self, key, value):
        """
        Raises ValueError when type of 'value' not in _memberTypes


        :param key: as in dict
        :param value: as in dict
        :return: nothing
        """
        if not type(value) in self._memberTypes:
            raise  ValueError("type of argument ({}) not in memberTypes ({})".
                              format(type(value),
                                     self._memberTypes))
        self._store[key] = value

    def __delitem__(self, key):
        del self._store[key]

    def __iter__(self):
        return iter(self._store)

    def __len__(self):
        return len(self._store)

    def allowType(self,memberCandidateType):
        #return type(memberCandidate) in self._memberTypes
        return memberCandidateType in self._memberTypes

    def __repr__(self):
        return self._store.__repr__()

class codebookCls():
    def __init__(self,input=None,output=None):
        """
        REFI-QDA codebook object, as per https://www.qdasoftware.org/codebook-exchange/, retrieved jan/2020, cited 
        as [REFI-QDA21].  
        If not otherwise stated, [REFI-QDA21] standard applies to attributes and member objects throughout the module.

        :param input: name of a file-like object o stream URL, possibly fully qualified. optional, can be override when calling  or readQdcStrem()
        :param output: name of a file-like object o stream URL, if not fully qualified uses home directory . read-only. defaults to standard output.
        :param origin: string as per [REFI-QDA21]
        """
        self.__input=input
        self.originDict = dict(origin="portableQDA "+__version__)
        self.sets=codeSetDict(memberTypes=(setCls,))  #index of Code elements, validate and make sure they last
        self.codes=codeSetDict(memberTypes=(codeCls,)) #index of Set elements, make sure they last in lxml's proxy
        self._codes_id = CODES_ID
        self._sets_id = SETS_ID
        self.miscElements=dict() #elements other than sets or codes, presumably none
        # http://schema.qdasoftware.org/versions/Codebook/v1.0/Codebook.xsd
        self.children = dict()
        #self.tree=etree.ElementTree(etree.XML("""<?xml version="1.0" encoding="UTF-8"?>
        self.tree=etree.ElementTree(etree.fromstring(CODEBOOK_UNPOPULATED))
        self.tree_root = self.tree.getroot()
        #print(self.tree.docinfo.doctype)
        #< !DOCTYPE root SYSTEM; "test" >
        #tree.docinfo.public_id = ’- // W3C // DTD; XHTML; 1.0; Transitional // EN’
        #self.tree.docinfo.system_url = ’file: // local.dtd’
        log.debug("tree created, root node: 'CodeBook'. see REFI-QDA 1.5")
        self.__output = None
        if output is not None:
            try: #test whether the requested output is writable
                self.__output=pathlib.Path(output)
                pass
                if len(self.__output.parts) == 1:
                    self.__output = self.__output.home() / self.__output
                if self.__output.exists():
                    self.__output.touch()
                else:
                    with open(self.__output,mode="wb") as fh:
                        fh.write(etree.tostring(element_or_tree=self.tree))
                log.info("output is {}".format(self.__output))
            except Exception as e:
                self.__output = None
                log.warning("output param not pointing to a writable file, setting to None. writeQdcFile() will use standard output, error: {}".format(e))
                log.info("for streaming output try writeQCDstream")
        #log.trace(self.tree.tostring())
        # if output is None:
        #     self.saxOutput = None
        # else:
        #     self.saxOutput=XMLGenerator(self.output, encoding='utf-8',
        #                  short_empty_elements=True)
        #     self.saxOutput.startDocument()
        #     self.saxOutput.startPrefixMapping(None, 'urn:QDA-XML:codebook:1:0')

    def guidInTreeOrNone(self, guid):
        #TODO: decide whether to index element guids or rely on XLMX's performance. O(N)?
        return self.tree.find(f'.//*[@guid="{guid}"]')

    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self,input,*args,**kwargs):
        if hasattr(input,"read"):
            self.__input=input
        else:
            try: #test whether the requested input is suitable
                self.__input=pathlib.Path(input)
                if len(self.__input.parts) == 1:
                    self.__input = pathlib.Path.cwd() / input
                    if not self.__input.exists():
                        self.__input = self.__input.home() / input
                if not self.__input.exists():
                    raise FileNotFoundError("tried {}, then {}".format(pathlib.Path.cwd() / input, self.__input.home() / input))
            except Exception as e:
                self.__input = None
                log.warning("input param: file not found. setting to None. readQdcFile(input=___) need a valid input. {}".format(e))

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self,*args,**kwargs):
        log.warning("output set when codebook was instantiated, read-only attribute")

    def tostring(self,element_or_tree=None):
        if element_or_tree is None:
            element_or_tree = self.tree
        etree.tostring(element_or_tree=element_or_tree)

    def createElement(self,*args, elementCls: elementCls, name: str, parent = None,  **kwargs) -> resultCls:
        """
        Create an element (code or set). codebookCls will act as a container keeping an index of objects, and
        tree (lxml) for import/export

        createElement() sanitizes the argumets and preconditions. Keep corresponding index updated. When creating a
         code, all requested sets will be created and/or binded
        IMPORTANT: If guid is provided, it must match an element already  in codebooks's tree, constructor grabs attribs from it
                    (i.e. called by readQDC()).The new object will act as a proxy to that element in etree.
                    if GUID is None, element will be created from scratch (both the codebook.tree's element and
                     the corresponding proxy object and indexed in codebook.codes,codebook.sets,etc).
                     Please, avoid any inconsistent situation (guid not in cntr.tree, etc)

        example: createElement(elementCls= setCls,
                                name= "set1",
                                description= "desc1")
        example: error,errorDesc,newSet = createElement(elementCls= setCls, name= "set1",description= "desc1")
        example: newSet = resultCls(*createElement(elementCls= setCls, name= "set1",description= "desc1")
        example: newCode = resultCls(*createElement(elementCls= codeCls,
                                            name= "code1",
                                            description= "desc1",
                                            sets=["set1",set2object)



        :param elementCls: codeCls or setCls, (in the future noteCls, sourceCls, etc as per REFI-QDA)
        :param name: srt
        :param parent: if supported by elementCls
        :param kwargs: other parames needed by elementCls. NOT guid.
        :return: resultCls -> (error:bool,errorDesc:str,result:new instance subclass of elementCls).  
        """
        error=1
        errorDesc=""
        miSetsList = list()  #sanitized sets list (all valid setCls objects)
        if self.codes.allowType(elementCls):
            idx=self.codes
        elif self.sets.allowType(elementCls):
            idx=self.sets
        else:
            msg="element not recognised, indexed in miscElements"
            errorDesc+=msg+". "
            log.warning(msg)
            idx=self.miscElements
        if idx[name] is not None:
            msg="new element replaces existing one in index: {}".format(name)
            errorDesc+=msg+". "
            log.warning(msg)
        if parent is not None:
            if idx[parent] is None:
                msg="new orphan element {}. parent not found: {}".format(name, parent)
                errorDesc += msg+". "
                log.warning(msg)
        if "sets" in kwargs.keys():
            if elementCls is setCls and kwargs["sets"] is not None:
                msg="sets are not allowed to nest, discarding 'sets' argument. see REFI-QDA v1.5"
                errorDesc += msg+". "
                log.warning(msg)
                del kwargs["sets"]
            else:
                if kwargs["sets"] is None:
                    kwargs["sets"] = list()
                elif issubclass(type(kwargs["sets"]), typing.Iterable):
                    for  i,miSet in enumerate(kwargs["sets"]):
                        if type(miSet) == setCls:
                            miSetsList.append(miSet)
                            #ok to go
                        elif type(miSet) == str:
                            # might or might not exist. Should be both in index and in tree
                            if self.sets[miSet] is None:
                                # not in index... neither should exist in tree but no need to check (see readQDC use case)
                                if "guid" in kwargs.keys() and kwargs["guid"] is not None:
                                    msg=f"code '{name}' will not be part of set '{miSet}'. Please, report this as a BUG: looks like you are reading a QDC/QDPX file, but set '{miSet}' not found (not indexed, but might be in tree)"
                                    log.warning(msg)
                                    errorDesc += msg
                                    log.debug(f"codebookCls.createElement(): set '{miSet}' not found in index. arguments: {args}, {elementCls}, {name}, {parent}, {kwargs}")
                                    #no-ok
                                else:
                                    # not reading QDC filwe.. ok to create
                                    log.info(f"set not found '{miSet}', creating")
                                    set1params = {"elementCls": setCls, "name": miSet} #"ctnr":self, ?
                                    createdSet = resultCls(*self.createElement(**set1params))
                                    if createdSet.error:
                                        log.warning(f"code '{name}' will not be part of set '{miSet}', creation error: {createdSet.errorDesc}")
                                    else:
                                        miSetsList.append(createdSet.result)
                                    # ok to go
                            else:
                                # , valid set, indexed
                                miSetsList.append(self.sets[miSet])
                                # ok to go
                        else:#for i in borrar:
                            msg = f"sets argument should be a list of (only) setCls or strings, discarding argument #{i}:{kwargs['sets'].pop(i)}"
                            errorDesc += msg + ". "
                            log.warning(msg)
                else:
                    msg = "sets argument should be a list (or any iterable) of types setCls and setCls.name, discarding argument {}. see REFI-QDA v1.5".format(
                        kwargs["sets"])
                    kwargs["sets"] = list()
                    errorDesc += msg + ". "
                    log.warning(msg)
            del kwargs["sets"]
        if parent is not None:
            parent = idx[parent]
        try:
            if idx[name] is not None:
                log.debug(f"removing old code '{name}' ({idx.pop(name)}) from index, will be replaced")
            # Create code, sets are NO LONGER created by codeCls constructor
            idx[name]=elementCls(ctnr=self, name=name,parent=parent, **kwargs)
            # enroll code in valid requested sets,
            for miSet in miSetsList:
                result=resultCls(*miSet.memberCodeAppend(idx[name]))
                pass
        except ValueError as e:
            #let the caller deal with the element creation problem
            errorDesc += str(e) #will set variable 'error'
        except Exception:
            raise
        if len(errorDesc) == 0:
            error = False
        return error,errorDesc,idx[name]

    def writeQdcFile(self):
        if self.output is None:
            log.info("codebook.output not set, printing XML to standard output".format(self))
            log.debug("document dump starts -----"+"8<----"*5)
            print(etree.tostring(self.tree, xml_declaration=True, encoding = ENCODING, pretty_print = True).
                  decode(ENCODING))
            log.debug("document dump ends -----"+"8<----"*5)
        else:
            #fh = open(self.output,"")
            log.info("exporting as REFI-QDC  codebook to file: {}".format(self.output))
            self.tree.write(str(self.output), xml_declaration=True, encoding = ENCODING, pretty_print = True)

    def writeQdcStream(self):
        if self.output is None:
            self.writeQdcFile()
        else:
            raise NotImplementedError("writing to stream not yet implemented, please try writeQdcFile()")
            #etree.xmlfile...

    def readQdcFile(self,input = None):
        """
        load data from a QDC file

        :param input: a file path, defaults to the input already set (codebookCls.input)
        :return:
        """
        if input is not None:
            self.input=input
        if self.input is None:
            raise ValueError("readQdcFile: specify input file, either setting the input attribute or as a parameter to readQdc()")

        log.info("reading QDC data from {}".format(self.input))
        try:
            old_tree = self.tree
            with open(self.input,mode="rb"):
                self.tree=etree.parse(input)
        except Exception as e:
            raise
        finally:
            del old_tree
        self.tree_root=self.tree.getroot() #again? no... the other tree was emptry
        def tagMissing(id,tag):
            result = len(self.tree_root) - 1 < id or \
                not self.tree_root[id].tag.endswith(tag + "s")
            return  result
        #
        # validate input according to REFI-QDA 1.5
        #
        #look for "Codes" container
        if tagMissing(id=self._codes_id,tag=TAG_CODE): #Codes container not where it's supposed to be
            try:
                id_antes=self._codes_id
                self._codes_id=[i for i, e in enumerate(self.tree.getroot()[:]) if e.tag.endswith(TAG_CODE + "s")][0]
                log.debug("readQdcFile: {}s container not where it's supposed to be([0][{}]): found at tree[0][{}]".
                          format(TAG_CODE, id_antes, self._codes_id))
            except Exception as e:
                pass
            if tagMissing(id=self._codes_id,tag=TAG_CODE):
                raise ValueError("readQdcFile: tag {} not found (mandatory element under CodeBook tag)".format(TAG_CODE+"s"))

        #look for "Sets" container
        if tagMissing(id=self._sets_id,tag=TAG_SET): #Sets container not where it's supposed to be
            try:
                id_antes= self._sets_id
                self._sets_id=[i for i, e in enumerate(self.tree.getroot()[:]) if e.tag.endswith(TAG_SET + "s")][0]
                log.debug("readQdcFile: {}s container not where it's supposed to be([0][{}]): found at tree[0][{}]".
                          format(TAG_SET, id_antes, self._sets_id))
            except Exception as e:
                pass
            if tagMissing(id=self._sets_id,tag=TAG_SET):
                raise ValueError("readQdcFile: tag {} not found (mandatory element under CodeBook tag)".format(TAG_SET+"s"))

        #read sets in tree and create proxy objects
        #create sets FIRST then codes, in order to assure uniqueness and membership
        groupsToCode=dict()
        miSetIdx=0
        for miSet in self.tree_root[self._sets_id]:
            args={"elementCls":setCls, **miSet.attrib}
            if "name" not in args.keys():
                args["name"]=f"noNameSet{miSetIdx}"
                log.warning(f"readQdcFile(): set at index {miSetIdx} lacking 'name' attr, using {args['name']}")
            log.debug(f"readQdcFile(): reading set {args['name']}")
            try:
                # create proxy objects
                error, errorDesc, setQda = self.createElement(**args)
                #error, errorDesc, setQda = True, "dry-run", None
                if error:
                    log.warning(f"readQdcFile(): set {args['name']}: error {errorDesc} trying to create set ")
                else:
                    for miChild in miSet:
                        if miChild.tag.endswith("Description"):
                            if setQda.description is not None:
                                #TODO: is this a bug in some CAQDAS ??
                                log.warning(f"readQdcFile: REFI-QDA_1.5 support: set {args['name']} has non-standard 'Description' as a member tag (4.4 Exchanging codebooks )")
                                log.info(f"readQdcFile: set {args['name']} changes description from {setQda.description} to {miChild.text}")
                                setQda.description=miChild.text
                        elif miChild.tag.endswith("MemberCode"):
                            #use groupsToCode to keep track of gropus membership
                            if miChild.attrib["guid"] in groupsToCode.keys():
                                groupsToCode[miChild.attrib["guid"]].append(setQda.name)
                            else:
                                groupsToCode[miChild.attrib["guid"]]=[setQda.name,]
                        elif miChild.tag.endswith("MemberNote"):
                            log.warning(f"readQdcFile(): set {args['name']}: references to Notes not supported: {miChild.attrib}")
                        elif miChild.tag.endswith("MemberSource"):
                            log.warning(f"readQdcFile(): set {args['name']}: references to Sources not supported: {miChild.attrib}")
                        else:
                            log.warning(f"readQdcFile(): invalid tag {miChild.tag} to set {args['name']} ")
            except Exception as e:
                log.warning(f"readQdcFile(): set {args['name']}: unhandled error while reading:  {e} ")
            miSetIdx += 1
        #read codes in tree and create proxy objects
        miCodeIdx=0
        for miCode in self.tree_root[self._codes_id]:
            args={"elementCls":codeCls, **miCode.attrib}
            if "name" not in args.keys():
                args["name"]=f"noNameCode{miCodeIdx}"
                log.warning(f"readQdcFile(): code at index {miCodeIdx} lacking 'name' attr, using {args['name']}")
            if "guid" not in args.keys(): #guid is mandatory a  per REFI-QDA 1.5
                args["guid"]= valid_guid(None,name=args["name"]+"readQDC")
                log.warning(f"readQdcFile(): code at index {miCodeIdx} lacking 'guid' attr, using {args['guid']}. guid is mandatory a  per REFI-QDA 1.5")
            try:
                #create proxy objects
                error, errorDesc, codeQda = self.createElement(**args)
                if error:
                    log.warning(f"readQdcFile(): code {args['name']}: error {errorDesc} trying to create code")
                else:
                    for miChild in miCode:
                        log.warning(f"readQdcFile():  code {args['name']}: invalid tag {miChild.tag} (i.e. code nesting not supported)")
            except Exception as e:
                log.warning(f"readQdcFile(): code {args['name']}: unhandled error while reading:  {e} ")
            miSetIdx += 1
        #readQdcFile() ends: codobook now has a tree looded from QDC file and correspoding proxy objects (setCls and codeCls)
        #return

    def compareQdc(self, codebook, IamOlder=True, destination=None, elementSuffix=None):
        """
        compare a QDC file with current tree, saves the differences to the configured output

        'destinations' allows you to import a *modified* codebook, avoiding  collitions. In particular:
            - "atlas9": add a suffix to element modified names
            - "atlas9": generates new GUID for modified names
            - "atlas9": deleted elements will still be listed, but under a "deleted*" folder

        destination "atlas9" is meant to let you perform manually (by merging or deleting codes/sets)
         the changes that altas don't do automatically (yet? please!),

        :param input: a file path, defaults to the input already set (codebookCls.input)
        :param IamOlder: True to get differences from and older tree (False if it's the other way arround)
        :param destination: if not None,  process diferences beforr exporting. Available  destinations : "atlas9"
        :param outputSuffix: suffix to add to configured output ("output.qdc" becomes "output-diff.qdc")
        :param elementSuffix: suffix to add to modified elementos (for merge after import)
        :return:
        """
        from xmldiff import main as xmld #moved here as long as its an optional dependency
        from xmldiff import actions as xmlda #moved here as long as its an optional dependency
        if not IamOlder:
            raise NotImplementedError("only forward changes (updating and old codebook) implemented, IamOlder argument needs to be True")
        if not isinstance(codebook,codebookCls):
            raise ValueError("compareQdcFile: argument to 'codebook' must be another codebook to compare to (older or nwer, depending on 'IamOlder'). ")
        def atlas9(editScript: list):
            """
            apparently, atlas9  does not support codebook updating. So this funcion adapts the codebook for re-importing:
            1. adds a subcode to *every* elemnt by renaming  it as '*::NotChanged-compareQDA'
            1. modifies xmldiff's editScript
                1.  tagging new elemnts as '*::Created-compareQDA'
                1. tagging updated elemnts as '*::Updated-compareQDA'
                1. tagging deleted elemnts as '*::Deleted-compareQDA'
            1. creates a new GUID for every not-new element

            (where "-compareQDA" is the default value to elementSuffix )
            user of atlas9 has to manually execute the update operations by merging/deleting codes

            :param editScript:
            :return: editScript is  modified in place
            """
            nonlocal  elementSuffix
            elementGuid=dict()
            if elementSuffix is None or not elementSuffix is str:
                import datetime
                elementSuffix = "-compareQDC("+datetime.datetime.strftime(datetime.datetime.now(),"%c")+")"

            # adds a subcode to *every* elemnt by renaming  it as '*::NotChanged-compareQDA'
            root=self.treeDiff.getroot()
            for elm in root.iter():
                if "name" in elm.attrib.keys():
                    elm.attrib["name"] = elm.attrib["name"] + CATEGORY_SEP + compOp.N.value + elementSuffix
            deletedElementsDetected=False
            lastInsertTag=None
            for i,action in enumerate(editScript):
                #log.debug("compareQDC: destination atlas9: processing action {}".format(action))
                if isinstance(action, xmlda.InsertNode):
                    lastInsertTag=action.tag
                    #if not deletedElementsDetected:
                    # editScript.insert(0,None)
                    deletedElementsDetected = True
                elif isinstance(action, xmlda.InsertAttrib):
                    if lastInsertTag in ("Code","Set"):
                        if action.name=="name":
                            #newValue=  action.value.replace(compOp.N.value,compOp.U.value)
                            newValue=  action.value + CATEGORY_SEP + compOp.U.value + elementSuffix #-> name::Updated-compareQDA(date)
                            log.info("compareQDC: destination atlas9: changing element name from {} to {}".
                                     format(action.value,newValue))
                            editScript[i]=action._replace(value=newValue) #xmldiff actions are namedtuples
                            pass
                    if lastInsertTag in ("Code", "Set","MemberCode"):
                        if action.name=="guid":
                            if action.value in elementGuid.keys():
                                newValue = elementGuid[action.value]
                            else:
                                newValue = valid_guid(name=str(action))
                                elementGuid[action.value]= newValue
                                log.info("compareQDC: destination atlas9: changing element guid from {} to {}".
                                             format(action.value,newValue))
                            editScript[i]=action._replace(value=newValue) #xmldiff actions are namedtuples
                            pass
        destinations={"atlas9":atlas9}
        log.warning("compareQDC feature is HIGHLY EXPERIMENTAL, use output only as a hint")
        log.info(f"""comparing QDC from data from {"OLDER" if IamOlder else "NEWER"} codebook.input:{codebook.__input})""")
        #
        #produce editScript
        #
        if IamOlder:
            diffScript=xmld.diff_trees(self.tree,codebook.tree,diff_options={"uniqueattrs":["guid"]})
        else:
            #not tested, prevented by validation at the begining of compareQDC()
            diffScript=xmld.diff_trees(codebook.tree,self.tree,diff_options={"uniqueattrs":["guid"]})
        # copy the destination tree in order to mark  differences
        self.treeDiff=etree.ElementTree(etree.fromstring(etree.tostring(codebook.tree).decode())) #TODO: better way to copy an etree?
        if destination is not None:
            #
            # process differences adapting them to a specific destination  app
            #
            if destination in destinations.keys():
                destinations[destination](diffScript) #will update diffScript in place
                pass
            else:
                log.warning("compareQDC: ignoring requested deestination '{}', valid ones are: {}".
                            format(destination,destinations.keys()))
        try:
            # apply the script to the tree
            self.treeDiff=xmld.patch_tree(diffScript,self.treeDiff)
            pass
        except Exception as e:
            log.warning("compareQDC: applying editScript to output, failed: {}".format(e))
            #self.treeDiff=etree.ElementTree(etree.fromstring(CODEBOOK_UNPOPULATED))
            # self.codebookDiff=codebookCls(output="diff.qdc")
            # self.codebookDiff.readQdcFile(input=self.input)
            lastAction=None
            for action in diffScript:
                lastActionOK=True
                #log.debug("compareQDC: applying editScript step-by-step: {}".format(action))
                try:
                    self.treeDiff=xmld.patch_tree([action,],self.treeDiff)
                    lastActionOK = True
                    lastAction="compareQDC: editScript step OK: {}".format(action)
                    #log.debug(lastAction)
                except Exception as e:
                    lastActionOK = False
                    log.warning("compareQDC: lastAction: {}".format(lastAction) )
                    log.warning("compareQDC: editScript step failed: {}, {}".format(e,action))
                    #self.treeDiff=etree.ElementTree(etree.fromstring(CODEBOOK_UNPOPULATED))
        log.debug("compareQDC: diff generated")
        pass

    def writeQdcDiff(self,suffix=None):
        if hasattr(self,"treeDiff") and hasattr(self.treeDiff,"getroot"):
            if self.output is None:
                #
                # to stdout
                #
                log.info("codebook.output not set, differences to standard output".format(self))
                log.debug("document dump starts -----"+"8<----"*5)
                print(etree.tostring(self.treeDiff, xml_declaration=True, encoding = ENCODING, pretty_print = True).
                      decode(ENCODING))
                log.debug("document dump ends -----"+"8<----"*5)
            else:
                #
                # sanitize output path
                #
                if suffix is None:
                    suffix="-compareQDC"
                if len(suffix ) >3 and  suffix.lower()[-4:] == ".qdc":
                    suffix = suffix[:-4]
                    if len(suffix) == 0:
                        suffix="-compareQDC"
                #     log.warning("something went wrong whith the outpút path or the suffix you requested, output path set to default")
                outputDiff= self.output.parent / ( self.output.stem + suffix + ".qdc" )
                log.info("exporting differences as a REFI-QDC codebook to file: {}".format(outputDiff))
                #
                # aaaannnd finally: the output!
                #
                self.treeDiff.write(str(outputDiff), xml_declaration=True, encoding = ENCODING, pretty_print = True)
        else:
            log.warning("codebook.writeQdcDiff(): not run. Need to set treeDiff first using codebook.compareQdc()")

class projectCls():
    def __init__(self):
        raise NotImplementedError()

#class codeCls(elementCls,etree.ElementBase): #not a good idea according to docs :/
class codeCls(elementCls):
    TAG=TAG_CODE

    def __init__(self, ctnr: codebookCls, name: str, parent = None, color=None, guid=None, description=None, sets=list(), **kwargs):
        """
        class for REFI-QDA codeType

        :param ctnr: container (codebookCls)
        :param name: as per REFI-QDA 1.5
        :param parent: ancestor element as per REFI-QDA 1.5. not yet implemented
        :param color: as per REFI-QDA 1.5
        :param guid: if provided, element olready exists in ctnr's tree, grab attribs from it (i.e. called by readQDC()). The new instance will act as a proxy to an already existing element in etree. if GUID is None, element will be created from scratch (both the ctnr.tree element and the corresponding proxy object and indexed in codebook.codes,codebook.sets,etc). beware: any inconsistent situation (guid not in cntr.tree, etc) will raise a hard error
        :param description: as per REFI-QDA 1.5
        :param sets: as per REFI-QDA 1.5
        :param kwargs: ignore other params like isCodable (code nesting not supported yet)
        """
        super(codeCls, self).__init__()
        self.ctnr=ctnr
        ctnr_tree_parent=ctnr.tree_root[ctnr._codes_id]
        # misintrepretation of fig3 on REFI-QDA 1.5
        # etree.SubElement(self.etreeElement, TAG_DESC).text = description
        if type(description) == str:
            self.description = description
        else:
            log.debug(f"setCls.__init__: set '{name}' description to default")
            self.description = ""
        if guid is None:
            log.debug("codeCls: instantiated without GUID, creating new etree element. not read from file, isn't it?")
            self.guid = valid_guid(guid, name)
            self.name = name
            if sets is None:  # or not hasattr(sets,"__iter__"): # validated by createElement's consutructor
                sets = list()
            # self.children = codeSetDict(memberTypes=(self.__class__,))
            self.sets = codeSetDict(memberTypes=(setCls,))
            self.color=valid_color(color)
            if self.ctnr.guidInTreeOrNone(guid=self.guid) is None: #test if element already in etree (only when reading a QDC file, otherwise a bug)
                if True:# parent is None: #not supported yet
                    #TODO: code nesting as per REFI-QDA_1.5, "isCodable": "flase"?
                    #Codes not really orphan: a forest anchored at cntr.codes
                    self.etreeElement = etree.SubElement(ctnr_tree_parent,self.__class__.TAG,attrib={"name": self.name,
                            "guid": self.guid,"color": self.color,"isCodable": "true","description":self.description})
                    self.parent=None
                    if self.ctnr.guidInTreeOrNone(guid=self.guid) is None:
                        log.warning(
                            f"elementCls.init(): element not found in tree, you found a bug:  guidInTreeOrNone({guid}) is None")
                else:
                    pass
                #
                # set creation on bulk, moved to codebookCls.createElememnt(
                #
                # for miSet in sets:
                #     if type(miSet) is setCls:
                #         if ctnr.sets[miSet] is None:
                #             miSet = miSet.name
                #         else:
                #             msg = f"codeCls.__init__: set {miSet.name} not previously in codebook, creating"
                #             log.info(msg)
                #             error, errorDesc, miSet = ctnr.createElement(elementCls=setCls, name=miSet)
                #             if error:
                #                 msg = "codeCls.__init__: error {} when ".format(errorDesc) + msg
                #                 log.warning(msg)
                #         miSet.appendMemberCode(self)
                #         if miSet.memberCodes[self.name] is self:
                #             pass
                #         else:
                #             msg = "codeCls.__init__: failed to add code '{}' to set '{}' ".format(self, miSet.name)
                #             log.warning(msg)
                #     else:
                #         log.warning(f"codeCls.__init__: set '{miSet}' of wrong type '{type(miSet)}', ignoring")

                # self.etreeElement=etree.SubElement(ctnr_idx,self.__class__.TAG,attrib={"name": name,
                #                                                                        "guid": self.guid,
                #                                                                        "description": description})
                #self.attrib = self.etreeElement.attrib
            else: #
                msg=f"elementCls.init(): element already in tree, that's only good when reading a QDC file. If not, you might have found a bug:  guidInTreeOrNone({guid})!=None"
                log.error(msg)
                raise ValueError(msg)
        else: #guid present, creating a reference for an element already in tree
            log.debug("codeCls: instantiated with GUID, fetching attribs from corresponding etree ")
            self.etreeElement = self.ctnr.guidInTreeOrNone(guid=guid)
            if self.etreeElement is None: #test if element already in etree (only when reading a QDC file, otherwise a bug)
                msg=f"elementCls.__init__: called with guid, so it should be in etree (tipically when reading a QDC file). If it is, you might have found a bug: guidInTreeOrNone({guid})==None"
                log.error(msg)
                raise ValueError(msg)
            else: #guid present, creating a reference for an element alread in tree (called from readQdc()??)
                # validating guid
                if "guid" in self.etreeElement.attrib.keys(): #if found by guidInTreeOrNone() shuld have a guid nevertheless...
                    self.guid = self.etreeElement.attrib["guid"]
                    self.guid = valid_guid(self.guid)  # setter updates tree guid
                else:
                    log.error(f"codeCls: no guid in tree element using '{guid}', {self.etreeElement.attrib}")

                if name != self.etreeElement.attrib["name"]:
                    log.warning(f"renaming code from '{self.etreeElement.attrib['name']}' to '{name}', GUID: {self.guid} ")
                    self.etreeElement.attrib['name']=name
                    #log.debug(f"removing code {ctnr.codes.pop(name)} from index") - creaeElement should remove element from index

                for miKey in self.etreeElement.attrib.keys():#['name', 'guid', 'description']:
                    setattr(self,miKey,self.etreeElement.attrib[miKey])
                self.parent = None
                self.children = None  # codeSetDict(memberTypes=(self.__class__,))# not defined in the standard
        if len(kwargs) > 0:
            log.debug(f"codeCls.__init__:  ignored params {kwargs}")

class setCls(elementCls):
    TAG=TAG_SET

    def __init__(self, ctnr: codebookCls, name: str, guid=None, description=None, **kwargs):
        """
        class for REFI-QDA setType

        :param ctnr: container (codebookCls)
        :param guid: if provided, element olready exists in ctnr's tree, grab attribs from it (i.e. called by readQDC()). The new instance will act as a proxy to an already existing element in etree. if GUID is None, element will be created from scratch (both the ctnr.tree element and the corresponding proxy object and indexed in codebook.codes,codebook.sets,etc). beware: any inconsistent situation (guid not in cntr.tree, etc) will raise a hard error
        :param description: as per REFI-QDA 1.5
        :param name: as per REFI-QDA 1.5
        :param kwargs: ignore other params like isCodable (code nesting not supported yet)        """
        super(setCls, self).__init__()
        self.ctnr=ctnr
        ctnr_tree_parent=ctnr.tree_root[ctnr._sets_id]
        if guid is None: #new element, not in tree
            log.debug("setCls: instantiated without GUID, creating new etree element. remember to index in cntr.sets. not read from file, isn't it?")
            self.guid =  valid_guid(guid, name)
            self.name = name
            if type(description) == str:
                self.description = description
            else:
                log.debug(f"setCls.__init__: set '{name}' description to default")
                self.description = ""
            if "parent" in kwargs.keys():
                if kwargs["parent"] is None:
                    del kwargs['parent']
                else:
                    log.warning(f"REFI-QDA 1.5: sets are not allowed to nest, ignoring parent '{kwargs.pop('parent')}'")

            #self.children = None  # codeSetDict(memberTypes=(self.__class__,))# not defined in the standard
            if self.ctnr.guidInTreeOrNone(guid=self.guid) is None: #test if element already in etree (only when reading a QDC file, otherwise a bug)
                # set are not orphan:indexed at cntr.sets
                self.etreeElement=etree.SubElement(ctnr_tree_parent,self.__class__.TAG,attrib={"name": self.name,
                                                                "guid": self.guid,"description": self.description})
                if self.ctnr.guidInTreeOrNone(guid=self.guid) is None:
                    log.warning(f"elementCls.init(): element not found in tree, you found a bug:  guidInTreeOrNone({guid}) is None")
            else: #
                log.debug(f"elementCls.init(): element alraedy in tree, if not reading a QDC file, you found a bug:  guidInTreeOrNine({guid}) not None")
        else: #guid present, creating a reference for an element alread in tree  (called from readQdc()??)
            self.etreeElement=self.ctnr.guidInTreeOrNone(guid=guid)
            if self.etreeElement is None: #test if element already in etree (only when reading a QDC file, otherwise a bug)
                log.debug(f"elementCls.init(): guid should be in tree, you found a bug:  guidInTreeOrNine({guid}) is None")
                msg = f"elementCls.__init__: called with guid, so it should be in etree (tipically when reading a QDC file). If it is, you might have found a bug: guidInTreeOrNone({guid})==None"
                log.error(msg)
                raise ValueError(msg)
            else:
                # validating guid
                if "guid" in self.etreeElement.attrib.keys(): #if found by guidInTreeOrNone() shuld have a guid nevertheless...
                    self.guid = self.etreeElement.attrib["guid"]
                    self.guid = valid_guid(self.guid)  # setter updates tree guid
                else:
                    log.error(f"codeCls: no guid in tree element using '{guid}', {self.etreeElement.attrib}")

                if name != self.etreeElement.attrib["name"]:
                    log.warning(f"renaming set from '{self.etreeElement.attrib['name']}' to '{name}', GUID: {guid} ")
                    log.debug(f"renaming set in tree to match proxy_object.name, from '{self.etreeElement.attrib['name']}' to '{name}', GUID: {guid} ")
                    self.etreeElement.attrib['name']=name
                for miKey in self.etreeElement.attrib.keys():#['name', 'guid', 'description']:
                    setattr(self,miKey,self.etreeElement.attrib[miKey])
        self.memberCodes = codeSetDict(memberTypes=(codeCls,))
        if len(kwargs) > 0:
            log.debug(f"codeCls.__init__:  ignored params {kwargs}")


    def memberCodeAppend(self, code: codeCls):
        """
        add code to set, return silently if already there

        :param code: code to add, codeCls type
        :return: a View of resulting code.name's in set (collections.abc.KeysView)
        """
        error = True
        errorDesc = ""
        if self.memberCodes[code.name] is None:
            try:
                self.memberCodes[code.name] = code
                etree.SubElement(self.etreeElement, TAG_SET_MEMBERCODE, {"guid":code.guid})
                error=False
            except ValueError as e:
                #let the caller dael with the problem
                errorDesc+=str(e)
            except Exception:
                raise
        else:
            error = False
            errorDesc = "code already in set"
        return error,errorDesc,self.memberCodes.keys()

    def memberCodeRemove(self, code: codeCls):
        """
        remove code from set, return silently if not there
        for a in self.etreeElement.iterfind(".//"):print(a.attrib.get("guid"))

        :param code: code to add, codeCls type
        :return: a View of resulting code.name's in set (collections.abc.KeysView)
        """
        error = True
        errorDesc = ""
        if self.memberCodes[code.name] is not None:
            cntr=0 #not ctnr ... :)
            try:
                for memberCodeElement in self.etreeElement.iterfind(".//"):
                    if memberCodeElement.attrib.get("guid")==code.guid:
                        self.etreeElement.remove(memberCodeElement)
                        cntr +=1
                if cntr != 1:
                    msg=f"setCls.memberCodeRemove(): number of  memberCodeElement removed is {cntr} but should be 1"
                    log.debug(msg)
                    errorDesc += msg
                del self.memberCodes[code.name] #TODO: what is cntr == 0 ?
                error=False
            except ValueError as e:
                #let the caller dael with the problem
                errorDesc+=str(e)
            except Exception:
                raise
        else:
            error = False
            errorDesc = "code not in set"
        return error,errorDesc,self.memberCodes.keys()

