import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DecisionTri(Node):
    def __init__(self):
        super().__init__('decision_tri')
        self.subscription = self.create_subscription(
            String, '/couleur_dechet', self.callback_couleur, 10)
        self.publisher = self.create_publisher(String, '/commande_servo', 10)
        self.get_logger().info('Noeud decision tri demarre')

    def callback_couleur(self, msg):
        couleur = msg.data
        commande = String()
        if couleur == 'bleu':
            commande.data = 'SERVO_BAC_PLASTIQUE'
        elif couleur == 'vert':
            commande.data = 'SERVO_BAC_VERRE'
        elif couleur == 'gris':
            commande.data = 'SERVO_BAC_METAL'
        else:
            commande.data = 'SERVO_BAC_GENERAL'
        self.publisher.publish(commande)
        self.get_logger().info(f'Couleur: {couleur} --> {commande.data}')

def main():
    rclpy.init()
    node = DecisionTri()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
