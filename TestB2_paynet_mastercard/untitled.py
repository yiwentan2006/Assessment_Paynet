#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Script-Name: account_holder_messaging
#

from __future__ import absolute_import
from __future__ import print_function
from mastercardapicore import RequestMap, Config, APIException, OAuthAuthentication
from os.path import dirname, realpath, join
from mastercardmdescustomerservice import AccountHolderMessaging
import pytest

keyStorePath = "/Users/apple/Django/myScript/Test_B-sandbox.p12" # e.g. /Users/yourname/project/sandbox.p12 | C:\Users\yourname\project\sandbox.p12
keyAlias = "keyalias"   # For production: change this to the key alias you chose when you created your production key

@pytest.mark.parametrize(
    "consumerKey,keyPassword ",
    [("Sb-lNlFBgbtbOS9CYuegPYqmw1w2LwP2ENsEqiahbf123c46!571e5262c2a84e8bbbb0b3b124828a7b0000000000000000", "keystorepassword")])
def test_login(consumerKey,keyPassword):
    auth = OAuthAuthentication(consumerKey, keyStorePath, keyAlias, keyPassword)
    Config.setAuthentication(auth)
    Config.setDebug(True) # Enable http wire logging
    Config.setSandbox(True)

    try:
        mapObj = RequestMap()
        mapObj.set("AccountHolderMessagingRequest.TokenUniqueReference", "DWSPMC00000000010906a349d9ca4eb1a4d53e3c90a11d9c")
        mapObj.set("AccountHolderMessagingRequest.MessageText", " You have earned a statement credit ")
        mapObj.set("AccountHolderMessagingRequest.MessageExpiration", "2020-09-18T18:04:35-06:00")
        mapObj.set("AccountHolderMessagingRequest.MessageLanguageCode", "en")
        mapObj.set("AccountHolderMessagingRequest.MessageIdentifier", "6598123486451346764616431064")
        mapObj.set("AccountHolderMessagingRequest.IssuerApplicationMessageDisplay", "FALSE")
        mapObj.set("AccountHolderMessagingRequest.AuditInfo.UserId", "A1435477")
        mapObj.set("AccountHolderMessagingRequest.AuditInfo.UserName", "John Smith")
        mapObj.set("AccountHolderMessagingRequest.AuditInfo.Organization", "Any Bank")
        mapObj.set("AccountHolderMessagingRequest.AuditInfo.Phone", "5555551234")

        response = AccountHolderMessaging.create(mapObj)
        out(response, "AccountHolderMessagingResponse.Token.TokenUniqueReference"); #-->DWSPMC00000000010906a349d9ca4eb1a4d53e3c90a11d9c

    except APIException as e:
        err("HttpStatus: %s", e.getHttpStatus())
        err("Message: %s", e.getMessage())
        err("ReasonCode: %s", e.getReasonCode())
        err("Source: %s",e.getSource())


def out(response, key):
    print("%s--> %s" % (key, response.get(key)))

def err(message, value):
    print(message % (value))


def errObj(response, key):
    print("%s--> %s" % (key, response.get(key)))


