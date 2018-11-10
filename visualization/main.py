# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 20:26:29 2018

@author: administered
"""

import mSQLFunction

m = mSQLFunction.mSQL();
#查看user_identity_type和pay_status有哪些值
m.mClassificate("has_refund");
m.close();





