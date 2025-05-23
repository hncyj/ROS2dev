import rclpy
from rclpy.node import Node
from autopatrol_interfaces.srv import SpeachText
import espeakng

class Speaker(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.speech_service = self.create_service(SpeachText, 'speech_text', self.speak_text_callback)
        self.speaker = espeakng.Speaker()
        self.speaker.voice = 'en'
        
    def speak_text_callback(self, request, response):
        self.get_logger().info(f"{request.text}")
        self.speaker.say(request.text)
        text = request.text
        self.speaker.say(text)
        self.speaker.wait()
        response.result = True
        
        return response
    

def main(args=None):
    rclpy.init(args=args)
    node = Speaker("speaker")
    rclpy.spin(node)
    rclpy.shutdown()