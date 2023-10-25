/*
 * Author:
 * Date:
 * Name:
 */
#include <string>
using namespace std;

string divideByA(long long A) {
    string num = "1";
    for (int i = 0; i < 99; i++) {
        num += "0";
    }
    string result = "";
    long long carry = 0;
    for (int i = 0; i < 100; i++) {
        long long digit = (num[i] - '0' + carry * 10) / A;
        result += to_string(digit);
        carry = (num[i] - '0' + carry * 10) % A;
    }
    return result;
}