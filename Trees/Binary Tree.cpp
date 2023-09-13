#include <assert.h>
#include <iostream>
using namespace std;

struct Node {
	int data;
	Node* left;
	Node* right;
};

auto addNode(int data) -> Node* {
	auto node = new Node;
	assert(node != nullptr);

	node->data = data;
	node->left = nullptr;
	node->right = nullptr;

	return node;
}

auto traverseInorder(Node* node) -> void {
	// left -> root -> right
	if (node != nullptr) {
		traverseInorder(node->left);
		cout << node->data << " -> ";
		traverseInorder(node->right);
	}
}

int main(int argc, char* argv[]) {
	auto root = addNode(10);
	root->left = addNode(2);
	root->right = addNode(3);
	root->left->left = addNode(4);

	traverseInorder(root);
	cout << "\n";
}