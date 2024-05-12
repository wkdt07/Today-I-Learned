int myFunc(void){
    return 0;
}

int myFunc(int a){
 return a;
}

#include <iostream>;
int main(void){
    int test1 = myFunc(6);
    int test2 = myFunc();

    std::cout<<"test1:"<<test1<<std::endl; // 6
    std::cout<<"test2:"<<test2<<std::endl; // 0

    return 0;
}