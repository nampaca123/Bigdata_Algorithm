#include <iostream>
#include <string>

int main() {
    int t;
    std::cin >> t;
    while (t--) {
        std::string n;
        std::cin >> n;
        long long product = 1;
        int zero_count = 0;
        for (char digit : n) {
            if (digit == '0') {
                zero_count++;
            } else {
                product *= (digit - '0'); 
            }
        }

        if (zero_count == n.length()) {
            product = 0;
        }

        std::cout << product << " " << zero_count << std::endl;
    }
    return 0;
}
