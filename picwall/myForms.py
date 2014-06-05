#########################################################################
# File Name: login_form.py
# Author: Jeremy
# mail: Jeremy19921115@gmail.com
# Created Time: Sat 24 May 2014 12:27:36 AM CST
#########################################################################
#!/usr/bin/env python
#coding=utf-8


from django import forms

class Login_Form(forms.Form):
    name = forms.CharField(max_length = 20)
    pwd = forms.CharField(max_length = 20)
