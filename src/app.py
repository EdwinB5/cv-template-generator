import os
import json

from .compilator import Compilator


class App():
    def __init__(self, config={}):
        self.config = config
        self.data = {}
        self.properties = {}
        self.list_components = []
        self.list_properties = []
        self.template = ''
        self.output_path = self.config['output']['dir'] + self.config['output']['name_file'] 
        print('App init...')


    def run(self) -> None:
        print('Running App...')
        self.get_components_path()
        self.get_properties_path()
        self.load_properties()
        self.load_data()
        self.load_template()
        Compilator.proccess(self.data, self.list_components, self.data_properties, self.list_properties, self.template, self.output_path)


    def get_components_path(self) -> None:
        components = os.listdir(self.config['input']['components_path'])
        result     = {}

        for i in range(len(components)):
            result[components[i]] = self.config['input']['components_path'] + components[i]
        
        self.list_components = result
        
        print(f'Components loaded: {self.list_components}')
    

    def get_properties_path(self) -> None:
        properties = os.listdir(self.config['input']['properties_path'])
        result     = {}
        
        for i in range(len(properties)):
            result[properties[i]] = self.config['input']['properties_path'] + properties[i]

        self.list_properties = result

        print(f'Propierties CV loaded: {self.list_properties}')


    def load_properties(self) -> None:
        self.properties = {}
        properties_path = self.config['input']['data_properties_path'] + self.config['input']['name_file_properties']
        
        with open(properties_path, 'r', encoding='utf-8') as file_properties:
            self.data_properties = json.load(file_properties)
        print('Properties loaded...')

    
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