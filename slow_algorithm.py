# Task: Improve this slow algorithm to find the nth Fibonacci number.
#include <iostream>
#include <vector>
using namespace std;

// Function to generate Fibonacci series
vector<int> fibonacci(int n) {
    vector<int> fib_series;
    int a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        fib_series.push_back(a);
        int temp = a + b;
        a = b;
        b = temp;
    }
    return fib_series;
}

int main() {
    int n;
    cout << "Enter the value of n: ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive integer." << endl;
    } else {
        cout << "Fibonacci series up to " << n << " terms:" << endl;
        vector<int> series = fibonacci(n);
        for (int num : series) {
            cout << num << " ";
        }
        cout << endl;
    }

    return 0;
}
