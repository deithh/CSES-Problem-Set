#include <iostream>
#include <set>
#include <vector>
void balance(std::multiset<int, std::greater<int>>* lower, std::multiset<int> *upper) {

    while (upper->size() < lower->size()) {
        auto temp = lower->begin();
        upper->insert(*temp);
        lower->extract(*temp);
    }

    while (upper->size() > lower->size()) {
        auto temp = upper->begin();
        lower->insert(*temp);
        upper->extract(*temp);
    }
}

int median(std::multiset<int, std::greater<int>>* lower, std::multiset<int>* upper) {
    if (lower->size() == 0) {
        return INT32_MAX;
    }
    return *lower->begin();
}


void insert(std::multiset<int, std::greater<int>>* lower, std::multiset<int>* upper, int num) {
    if (num <= median(lower, upper)) {
        lower->insert(num);
    }
    else {
        upper->insert(num);
    }
    balance(lower, upper);
}
void remove(std::multiset<int, std::greater<int>>* lower, std::multiset<int>* upper, int num) {
    if (num <= median(lower, upper)) {
        lower->extract(num);
    }
    else {
        upper->extract(num);
    }
    balance(lower, upper);
}

void solve(int n, int k, std::vector<int> arr) {

    std::multiset<int, std::greater<int>>  lower;
    std::multiset<int> upper;

    for (int i = 0; i < k; i++) {
        insert(&lower, &upper, arr[i]);
    }

    for (int i = k; i < n; i++) {
        std::cout << median(&lower, &upper)<<" ";
        remove(&lower, &upper, arr[i - k]);
        insert(&lower, &upper, arr[i]);
    }
    std::cout << median(&lower, &upper);
}



int main()
{

    int n, k, temp;
    std::cin >> n;
    std::cin >> k;
    std::vector<int> arr;
    for (int i = 0; i < n; i++) {
        std::cin >> temp;
        arr.push_back(temp);
    }

    solve(n, k, arr);

    return 0;
}