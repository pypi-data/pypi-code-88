#! /usr/bin/env python2

class radius(object):

  def __init__(self):
        import radiusd
        self._scene = 'radius'

  def __scene__(self):
        return self._scene

  def __help__(self):
        print 'Radius Grafter by iSafeTech 2021.'

  @staticmethod
  def instantiate(p):
    print "*** instantiate ***"
    print p
    # return 0 for success or -1 for failure
  @staticmethod
  def authorize(p):
    print "*** isafe authorize ***"
    radiusd.radlog(radiusd.L_INFO, '*** radlog call in authorize ***')
    print p
    print radiusd.config
    return radiusd.RLM_MODULE_OK

  @staticmethod
  def preacct(p):
    print "*** preacct ***"
    print p
    return radiusd.RLM_MODULE_OK

  @staticmethod
  def accounting(p):
    print "*** accounting ***"
    radiusd.radlog(radiusd.L_INFO, '*** radlog call in accounting (0) ***')
    print p
    return radiusd.RLM_MODULE_OK

  @staticmethod
  def pre_proxy(p):
    print "*** pre_proxy ***"
    print p
    return radiusd.RLM_MODULE_OK

  @staticmethod
  def post_proxy(p):
    print "*** post_proxy ***"
    print p
    return radiusd.RLM_MODULE_OK

  @staticmethod
  def post_auth(p):
    print "*** isafe post_auth ***"

    # This is true when using pass_all_vps_dict
    if type(p) is dict:
      print "Request:", p["request"]
      print "Reply:", p["reply"]
      print "Config:", p["config"]
      print "State:", p["session-state"]
      print "Proxy-Request:", p["proxy-request"]
      print "Proxy-Reply:", p["proxy-reply"]

    else:
      print p

    # Dictionary representing changes we want to make to the different VPS
    update_dict = {
          "request": (("User-Password", ":=", "A new password"),),
          "reply": (("Reply-Message", "The module is doing its job"),
                    ("User-Name", "NewUserName")),
          "config": (("Cleartext-Password", "A new password"),),
    }

    return radiusd.RLM_MODULE_OK, update_dict
    # Alternatively, you could use the legacy 3-tuple output
    # (only reply and config can be updated)
    # return radiusd.RLM_MODULE_OK, update_dict["reply"], update_dict["config"]

  @staticmethod
  def recv_coa(p):
    print "*** recv_coa ***"
    print p
    return radiusd.RLM_MODULE_OK

  @staticmethod
  def send_coa(p):
    print "*** send_coa ***"
    print p
    return radiusd.RLM_MODULE_OK

  @staticmethod
  def detach(p):
    print "*** goodbye from example.py ***"
    return radiusd.RLM_MODULE_OK

