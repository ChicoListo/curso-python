# Definir la clase para un nodo
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Definir la clase para una linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


# Crear una linked list            
mi_linked_list = LinkedList()
mi_linked_list.append(1)
mi_linked_list.append(2)
mi_linked_list.append(3)
print("Creacion de Linked List")
# Imprimir la linked list
mi_linked_list.print_list()

# Definir la clase para un nodo
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Definir la clase para una linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def delete_node(self, key):
        current_node = self.head

        # Caso especial: eliminar el primer nodo
        if current_node is not None and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        # Buscar el nodo a eliminar
        prev_node = None
        while current_node is not None:
            if current_node.data == key:
                break
            prev_node = current_node
            current_node = current_node.next

        # Si no se encontró el nodo, salir
        if current_node is None:
            return

        # Eliminar el nodo
        prev_node.next = current_node.next
        current_node = None

# Crear una linked list
mi_linked_list = LinkedList()
mi_linked_list.append(1)
mi_linked_list.append(2)
mi_linked_list.append(3)
print("eliminar un nodo de la printed list")
# Eliminar un nodo
mi_linked_list.delete_node(2)
mi_linked_list.print_list()
