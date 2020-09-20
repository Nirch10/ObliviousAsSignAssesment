# ObliviousAI - Coding Assessment
Secret(Key) based connection between a client and a server using a 3rd party key generator

#prerequisites

*python 3 installed

*python libraries needed (most of them are defaulty downloaded when python 3 is inatalled): 

	[os, ssl, requests, json, flask, abc, random] 

# How to use : 
First, we need to make sure our certificate is valid, in the certificate folder there is an example of a certificate, which you must add to your local certificate list (on MacOS -> go to KeyChain access -> click on the lock sign -> go to certificates -> click on the + -> choose the correct certificate)
If you wish to use your own (or something went wrong implementing the example certificate) - read manual of to create a certificate (f.e on mac : https://www.freecodecamp.org/news/how-to-get-https-working-on-your-local-development-environment-in-5-minutes-7af615770eec/)

Second, Configure your Config.json file as needed : 
*make sure your servers ips and ports are correct (choose ports higher than 1024 ..)
*make sure your certificates file paths are correct

Now after we set our certificate correctly - its time for some magic :)
There are 4 steps in order to make sure the program is working :

*Step 1 :NOT A MUST STEP in the main.py file -> set the Config.json path inside get_config_path() to your local path of Config.json
		the default config.json file will be located in the main folder.

*Step 2 : run the server -> from ServerPkg.__init__.py

*Step 3 : run the key generator -> from KeyGeneratorPkg.__init__.py

*Step 4 : run the client -> from ClientPkg.__init__.py

after step 3 the response will reveal wheater the secret numbers chosen by the server and client lead to the same number or not. 
*you can run step 3 as many times as you wish without repeating steps 1+2.

Good luck :)