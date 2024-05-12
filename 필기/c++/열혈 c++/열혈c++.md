# Ch01

- 책에 있는 내용이 이해가 된다면 그냥 책 보면 된다.

- 처음 공부할 때 가장 필요한거: 관찰. 무언가를 이해하려고 노력하기보단, 관찰을 통해서 알아라.
- 이 책은 c언어를 알고 있다는 가정 하에 공부하게 됨
  - c언어를 완전히 이해하지 않아도...

## 01-1 printf 와 scanf를 대신하는 입출력 방식

### 데이터 출력

> std::cout<<"출력대상1"<<"출력대상2"<<"출력대상3"<<std::endl;

### 데이터 입력

> std::cin>>"변수"

> <<>>의 방향? 그냥 '여기에 넣어라' 라고 생각해라

```cpp
//
// Created by user on 24. 5. 13.
//
# include <iostream>

int main(void){
    int num=20;
    // 데이터 출력
    // std::cout<<"출력대상1"<<"출력대상2"<<"출력대상3"<<std::endl;
    std::cout<<"Hello World";//<<std::endl;// 이걸 넣으면 띄어쓰기

    std::cout<<"enter"<<std::endl;


    // 데이터 입력
//    std::cin>>"변수"

    int val1;
    std::cout<<"input first num:";
    std::cin>>val1;
    // c++ 에선  변수의 선언 위치에 제한을 두지 않는다.
    int val2;
    std::cout<<"input second num:";
    std::cin>>val2;
    int result = val1+val2;
    std::cout<<"sum value:"<<result<<std::endl;

    return 0;
}
```

> 여러개가 나열되어 있을 때 입력의 순서?

```cpp
std::cin>>val1>>val2;
// val1에 먼저 입력되고, 이후에 val2에 입력된다.


```

> 문자열 입출력

```cpp
    char name[100];
    wchar_t name_s[100];

    std::cout<<"please input your name";
    std::cin>>name;
//    std::cin>>name2;
    // wchar_t는 wcin이라는게 쓰임
    /*
     #include <iostream>

int main() {
    char name[100];
    wchar_t name_s[100];

    std::cout << "please input your name";
    std::cin >> name;
    std::wcin >> name_s; // 수정: std::wcin 사용

    std::cout << name << std::endl;
    std::wcout << name_s << std::endl; // 추가: std::wcout 사용
    return 0;
}

     */

    std::cout<<name<<std::endl;
    return 0;
```

## 01-2 함수 오버로딩(Function Overloading)

- 용어에 긴장하지 마라
- c와 달리 cpp는 함수이름+함수인자 조합으로 함수를 구분할 수 있다
  - c에서는 함수 인자가 달라도 함수 이름이 같으면 컴파일 오류가 났다.
  - 인자 정보는 자료형, 인자 갯수 등
    - 반환형의 차이는 오버로딩의 조건을 만족시키지 않는다.
    - 오버로딩은 '함수 이름'+'함수 인자' 로만.

```cpp
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
```

## 01-3 매개변수의 디폴트값
