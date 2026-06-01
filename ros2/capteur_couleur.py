import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CapteurCouleur(Node):
    def __init__(self):
        super().__init__('capteur_couleur')
        self.publisher = self.create_publisher(String, '/couleur_dechet', 10)
        self.timer = self.create_timer(2.0, self.publier_couleur)
        self.couleurs = ['bleu', 'vert', 'gris', 'bleu', 'vert']
        self.index = 0
        self.get_logger().info('Capteur couleur demarre')

    def publier_couleur(self):
        msg = String()
        msg.data = self.couleurs[self.index % len(self.couleurs)]
        self.publisher.publish(msg)
        self.get_logger().info(f'Dechet detecte : {msg.data}')
        self.index += 1

def main():
    rclpy.init()
    node = CapteurCouleur()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
