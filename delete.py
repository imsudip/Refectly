import os

# delete files in the following directory in windows
# db_logs,chromadb,chat_logs,api_logs

files = ['db_logs', 'chromadb', 'chat_logs', 'api_logs']

for file in files:
    os.system('del /f /q /s '+file+'\\*')
    os.system('rmdir /s /q '+file)
    os.system('mkdir '+file)
    print('Deleted '+file+' folder')
