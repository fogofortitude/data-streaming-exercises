from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic
    
    # generates dummy data from input file
    def generate_data(self):
        print(self.topic)
        with open(self.input_file) as file:
            data = json.load(file)
            
            for line in data:
                message = self.dict_to_binary(line)
                data = json.load(file)
                # send the message data for the topic
                self.send(self.topic, message)
                time.sleep(1)

    # returns the json dictionary to binary               
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf-8')


