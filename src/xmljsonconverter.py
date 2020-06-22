import json


class XMLJSONConverter:
    def convertJSONtoXML(self, json_file, xml_file):
        # Todo: Implement this method
        print(json_file)
        print(xml_file)
        # raise NotImplementedError
        # input file
        input_file_object = open(json_file, 'r')
        print(input_file_object)
        output_file_object = open(xml_file, 'w')
        input_file_data = input_file_object.read()
        print(input_file_data)
        file_data_json = json.loads(input_file_data)
        if type(file_data_json) == float or type(file_data_json) == int:
            output_file_object.write(
                '<number>' + str(input_file_data) + '<number>')
