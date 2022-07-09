#include <iostream>
#include <stdio.h>
#include <queue>
using namespace std;

typedef struct Node {
	char key;
	Node* left;
	Node* right;
} Node;

Node* newNode(char value) {
	Node* n = new Node;
	n->key = value;
	n->left = nullptr;
	n->right = nullptr;
	return n;
}

Node* insert(Node* root, char value, queue<Node*>& q) {
	Node* node = newNode(value);
	if (!root) {
        root = node;
    } else if (!q.front()->left) {
		q.front()->left = node;
    } else {
		q.front()->right = node;
		q.pop();
	}
	q.push(node);
	return root;
}

Node* createTree(vector<char> arr, int n)
{
	Node* root = nullptr;
	queue<Node*> q;
	for (int i = 0; i < n; i++)
	    root = insert(root, arr[i], q);
	return root;
}

string inOrder(Node* root) {
	string res = "";
	if (!root) return res;
	res += inOrder(root->left);
	res += root->key;
	res += inOrder(root->right);
	return res;
}

int main() {
    string key;
    cout << "Enter the key: ";
    cin >> key;
	vector<char> arr;
    for (char c : key) {
        arr.push_back(c);
    }
	auto n = arr.size();
	Node* root = createTree(arr, n);
	if (inOrder(root) == "REDACTED") {
		cout << "You got it.\n";
	} else {
		cout << "Nope.\n";
	}
	return 0;
}