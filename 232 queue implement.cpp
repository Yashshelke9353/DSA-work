#include <bits/stdc++.h>
using namespace std;
int main() {
    MyQueue* obj = new MyQueue();
    obj->push(1);
    obj->push(2);
    cout << obj->peek() << endl; // return 1
    cout << obj->pop() << endl; // return 1
    cout << obj->empty() << endl; // return false
    return 0;
}

class MyQueue {
public:

    stack<int> s1, s2;

    void push(int x) {
        s1.push(x);
    }

    int pop() {

        if(s2.empty()) {

            while(!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }

        int x = s2.top();
        s2.pop();

        return x;
    }

    int peek() {

        if(s2.empty()) {

            while(!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }

        return s2.top();
    }

    bool empty() {
        return s1.empty() && s2.empty();
    }
};
