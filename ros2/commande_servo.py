import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommandeServo(Node):
    def __init__(self):
        super().__init__('commande_servo')
        self.subscription = self.create_subscription(
            String, '/commande_servo', self.callback_commande, 10)
        self.get_logger().info('Noeud commande servo demarre')

    def callback_commande(self, msg):
        commande = msg.data
        if commande == 'SERVO_BAC_PLASTIQUE':
            angle = 45
            bac = 'Bac bleu (Plastique)'
        elif commande == 'SERVO_BAC_VERRE':
            angle = 90
            bac = 'Bac vert (Verre)'
        elif commande == 'SERVO_BAC_METAL':
            angle = 135
            bac = 'Bac gris (Metal)'
        else:
            angle = 0
            bac = 'Bac general'
        self.get_logger().info(
            f'SERVO --> angle: {angle} degres | destination: {bac}')

def main():
    rclpy.init()
    node = CommandeServo()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
