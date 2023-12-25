

# Take input of both site and osint to perform 
# INput of osint can be a file containing list of queries 
# take input for number of tabs to open in one go
# 

# "redir","redirect","redirecturi","redirect_uri","redirecturl","redirect_uri","return","returnurl","relaystate","forward","forwardurl","forward_url","url","dest","uri","destination","next






osint_list=["redir=","redirect=","redirecturi=","redirect_uri=","redirecturl=","redirect_uri=","return=","returnurl=","relaystate=","forward=","forwardurl=","forward_url=","url=","dest=","uri=","destination=","next=","r=","view=","path=","image_url="]


import webbrowser as web

site = input('enter site\'s url in this format example.com \n')


google_url = "https://www.google.com/search?q="


for url in osint_list:
    global O_url
    O_url =google_url + "site:" + site + " inurl:" + url
    web.open(O_url)



# R_url= google_url + site +"site: " + 

# web.open(R_url)


