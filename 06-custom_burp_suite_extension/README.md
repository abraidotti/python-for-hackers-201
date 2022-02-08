- install burp suite

- download jython standalone (.jar file)

- in burp suite > Extender > Options > Python Environment > select the jython jar

- go here: https://github.com/securityMB/burp-exceptions/blob/master/exceptions_fix.py, go to the raw file and save it to the dir in which you'll develop the extension

- once you run the burp extension, run ../05-python_projects/encrypted_bind_shell.py, then try to connect to 127.0.0.1 in the burp extension
