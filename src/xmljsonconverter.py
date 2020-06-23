import json


class XMLJSONConverter:
    def convertJSONtoXML(self, json_file, xml_file):
        # Todo: Implement this method
        # print(json_file)
        # print(xml_file)
        # raise NotImplementedError
        # input file
        input_file_object = open(json_file, 'r')
        # print(input_file_object)
        output_file_object = open(xml_file, 'w')
        input_file_data = input_file_object.read()
        # print(input_file_data)
        file_data_json = json.loads(input_file_data)
        print(file_data_json)  # just to check the data
        self.ischeck(None, file_data_json, output_file_object)

        # if isinstance(file_data_json, dict):
        #     output_file_object.write('<object>')
        #     for key, val in file_data_json.items():
        #         self.ischeck(key, val, output_file_object)
        #     output_file_object.write('</object>')
        # else:
        #     a = " "
        #     self.ischeck(a, file_data_json, output_file_object)
        #output = self.convert(file_data_json)

    def convert(data, key):
        pass

    def ischeck(self, key, value, output_file_object):
        if value is None:
            if key == None:
                output_file_object.write('<null/>')
            else:
                output_file_object.write('<null name=\"' + str(key) + '\"/>')

        elif type(value) == float or type(value) == int:
            if key == None:
                output_file_object.write('<number>' + str(value) + '</number>')
            else:
                output_file_object.write(
                    '<number name=\"' + str(key) + '\">' + str(value) + '</number>')
        elif type(value) == str:
            if key == None:
                output_file_object.write(
                    '<string>' + str(value) + '</string>')
            else:
                output_file_object.write(
                    '<string name=\"' + str(key) + '\">' + str(value) + '</string>')
        elif type(value) == bool:
            if key == None:
                output_file_object.write(
                    '<boolean>' + str(value) + '</boolean>')
            else:
                output_file_object.write(
                    '<boolean name=\"' + str(key) + '\">' + str(value) + '</boolean>')
        elif type(value) == list:
            if key == None:
                output_file_object.write('<array>')
                for x in value:
                    self.ischeck(None, x, output_file_object)
                output_file_object.write('</array>')
            else:
                output_file_object.write('<array name=\"' + str(key) + '\">')
                for x in value:
                    self.ischeck(None, x, output_file_object)
                output_file_object.write('</array>')
        elif type(value) == dict:
            if key == None:
                output_file_object.write('<object>')
                for new_k, new_v in value.items():
                    self.ischeck(new_k, new_v, output_file_object)
                output_file_object.write('</object>')
            else:
                output_file_object.write('<object name\="' + str(key) + '\">')
                for new_k, new_v in value.items():
                    self.ischeck(new_k, new_v, output_file_object)
                output_file_object.write('</object>')
