#include<iostream>

class Node {
public:
    int data;
    Node *left;
    Node *right;

    // Constructor to initialize the Node with data
    Node(int x) : data(x), left(nullptr), right(nullptr) {}
};

class BinaryTree {
public:
    // Function to insert a node at the left of the root
    Node* insertNodeAtLeft(Node* root, int x) {
        if (root == nullptr) {
            std::cout << "Error: Attempt to add left node to a nullptr" << std::endl;
            return nullptr;
        }
        root->left = new Node(x);
        return root->left;
    }

    // Function to insert a node at the right of the root
    Node* insertNodeAtRight(Node* root, int x) {
        if (root == nullptr) {
            std::cout << "Error: Attempt to add right node to a nullptr" << std::endl;
            return nullptr;
        }
        root->right = new Node(x);
        return root->right;
    }
};

int main() {
    BinaryTree tree;

    // Create the root node
    Node *root = new Node(1);

    // Build the rest of the tree
    tree.insertNodeAtLeft(root, 2);
    tree.insertNodeAtRight(root, 3);

    tree.insertNodeAtLeft(root->left, 4);
    tree.insertNodeAtRight(root->left, 5);

    tree.insertNodeAtLeft(root->right, 6);
    tree.insertNodeAtRight(root->right, 7);

    // Example usage of the tree structure
    // Assume you have a function to print or traverse to demonstrate the tree structure

    // Clean up the dynamically allocated memory if necessary (not shown)
    // In a real program, you should also delete nodes to prevent memory leaks

    return 0;
}
