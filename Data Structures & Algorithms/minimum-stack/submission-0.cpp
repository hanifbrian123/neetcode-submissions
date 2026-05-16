class MinStack {
private:
    stack<int> st;
    stack<int> minHist;
public:
    MinStack() {}
    
    void push(int val) {
        if (st.empty() || val <= this->minHist.top()) {
            this->minHist.push(val);
        }
        this->st.push(val);
    }
    
    void pop() {
        if (this->st.top() == this->minHist.top()) {
            this->minHist.pop();
        }
        this->st.pop();
    }
    
    int top() {
        return this->st.top();
    }
    
    int getMin() {
        return this->minHist.top();
    }


};