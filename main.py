import json
import sys

from src.app import App

def set_log_std():
    #sys.stdout = open('./logs/log.txt', 'w', encoding='utf-8')
    #sys.stderr = open('./logs/error.txt', 'w', encoding='utf-8')
    pass

def main():
    set_log_std()
    config = {}
    with open('config.json', 'r') as file_config:
        config = json.load(file_config)
        print('Config loaded...')
    _app = App(config)
    _app.run()
    
if __name__ == '__main__':
    main()
    pass