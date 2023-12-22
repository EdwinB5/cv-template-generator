class Compilator():
    
    #Static variables
    list_str_components = []


    @classmethod
    def proccess(cls, data:dict, components:dict, template: str, output_path: str) -> None:
        print("Compilator proccess init...")
        #print(components)
        
        # 1. Get components to replace
        print("Get components to replace...")
        cls.get_to_replace(data, components)
        print("Components OK... ")

        # 2. Replace components in template
        print("Replace components in template...")
        template = cls.replace_template(template)
        print("Replace components OK...")

        # 3. Save template in output path
        print("Save template in output path...")
        with open(output_path, 'w', encoding='utf-8') as file_output:
            file_output.write(template)
        print("Compilator proccess finished...")


    @classmethod
    def get_to_replace(cls, data:dict, components:dict) -> None:
        for key, value in data.items():
            if isinstance(value, list):
                path_component = cls.search_component(key, components)
                
                if path_component != None:
                    #print(f"Component found: {path_component}")
                    
                    template_component = cls.get_component(path_component)
                    component_str = cls.replace_values(template_component, value)
                    
                    component = {}
                    nw_key = str('%{key}%').replace('key', key)
                    component[nw_key] = component_str

                    cls.list_str_components.append(component)

                else:
                   print("Component not found")
                   
            elif isinstance(value, dict):
                path_component = cls.search_component(key, components)
                if path_component != None:
                    template_component = cls.get_component(path_component)
                    component_str = cls.replace_str(template_component, value)
                    component = {}
                    nw_key = str('%{key}%').replace('key', key)
                    component[nw_key] = component_str
                    cls.list_str_components.append(component)
                else:
                    for field, sub_value in value.items():
                        field_t = {}
                        nw_key = str('@key@').replace('key', field)
                        field_t[nw_key] = sub_value
                        cls.list_str_components.append(field_t)

    @classmethod
    def replace_template(cls, template:str) -> None:
        for component in cls.list_str_components:
            #print(component)
            template = cls.replace_str(template, component, False)
        
        return template

    
    @staticmethod
    def search_component(key, components:dict) -> str:
        path_component = components.get(key)
        return path_component
    
    
    @staticmethod
    def get_component(path_component):
        component = ''
        with open(path_component, 'r', encoding='utf-8') as file_component:
            component = file_component.read()
        return component
    
    
    @classmethod
    def replace_values(cls, component: str, list_data:list) -> str:
        # Iterate each value and replace in the component
        # Example: VALUE: @DESCRIPTION - COMPONENT TEMPLATE: @DESCRIPTION@
        format_str = ''
        for data in list_data:
            format_str += cls.replace_str(component, data) + '\n\n'
         
        return format_str
    

    @staticmethod
    def replace_str(component: str, data: dict, is_format: bool = True):
        # Iterate each value and replace according dict values
        for key, value in data.items():
            # Replace each value in the component according to its key
            format_key = f'@{key}' if is_format else key
            component = component.replace(format_key, str(value))

        return component
         
        
            