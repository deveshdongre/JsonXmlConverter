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

    def ischeck(self, key, value, output_file_object)
       if value == ' ':
            self.ischeck(value, key, output_file_object)
        elif value is None:
            if key == ' '
               output_file_object.write('<null/>')
            else:
                output_file_object.write('<null name=\"' + str(key) + '\"/>')
               
        elif type(value) == float or type(value) == int:
            if key == ' ':
                output_file_object.write(
                    key '<number>' + str(key) + '</number>')
            else:
                output_file_object.write(
                    '<number name=\"' + str(key) + '\" >' + str(value) + '</number>')
        elif type(value) == str:
            if key == ' '
               output_file_object.write(
                    '<string>' + str(value) + '</string>')
            else:
                output_file_object.write(
                    '<string name=\"' + str(key) + '\" >' + str(value) + '</string>')
        elif type(value) == bool:
            if key == ' ':
                output_file_object.write('<boolean>' + str(value) + '</boolean>')
            else:
                output_file_object.write(
                    '<boolean name=\"' + str(key) + '\" >' + str(value) + '</boolean>')
        elif type(value) == list:
            if key == ' ':
                output_file_object.write('<array>')
                    for x in value:
                        self.ischeck(key, value,output_file_object)
                output_file_object.write('</array>')
            else:
                output_file_object.write('<array name=\"' + str(key) + '\" >')
                    for x in value:
                        self.ischeck(key, value,output_file_object)
                output_file_object.write('</array>')
        elif type(value) == dict:
            new_k,new_v = value.split(':')
            output_file_object.write('<object name\"'+ str(key) +  '\">')
            self.ischeck(new_k.strip(),new_v.strip(),output_file_object)
            output_file_object.write('</object>')
