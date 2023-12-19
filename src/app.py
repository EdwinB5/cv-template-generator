import os
import json

from .compilator import Compilator


class App():
    def __init__(self, config={}):
        self.config = config
        self.data = {}
        self.list_components = []
        self.template = ''
        self.output_path = self.config['output']['dir'] + self.config['output']['name_file'] 
        print('App init...')


    def run(self):
        print('Running App...')
        self.load_components()
        self.load_data()
        self.load_template()
        Compilator.proccess(self.data, self.list_components, self.template, self.output_path)


    def load_components(self):
        components = os.listdir(self.config['input']['components_path'])
        result     = {}

        for i in range(len(components)):
            result[components[i]] = self.config['input']['components_path'] + components[i]
        
        self.list_components = result
        
        print(f'Components loaded: {self.list_components}')
    

    def load_data(self):
        self.data = {}
        data_path = self.config['input']['data_path'] + self.config['input']['name_file_data']
        with open(data_path, 'r', encoding='utf-8') as file_data:
            self.data = json.load(file_data)
        print(f'Data loaded...')


    def load_template(self):
        template_path = self.config['input']['template_path'] + self.config['input']['name_file_template']
        with open(template_path, 'r') as file_template:
            self.template = file_template.read()
        print(f'Template loaded...')