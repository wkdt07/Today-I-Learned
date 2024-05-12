#include <stdio.h>

// 메모리영역

// 1. 스택
// 2. 데이터
// 3. 힙 
// 4. ROM(Read Only Memory, 코드영역) -> 여기에 집중

int main() {

	// 문자
	//char c = 1; // 1바이트 정수형 자료형. character. 문자 최적화 데이터 타입
	bool b = 1;

	int i = 0;


	wchar_t wc = 49; // 2바이트짜리 문자 최적화 데이터타입
	short s = 49;

	// 모두 데이터가 바뀐건 아님. 읽고자 하는 '데이터타입'이 변경되었으니 문자로 보이는것. 실질적으론 010100101형태의 이진수임

	// 주의 : 1 != '1'

	char cc = '1';
	char ccc = 1;
	// cc!=ccc

	//wc = 459;
	"459"; // 아스키 코드로 4-52, 5-53, 9-57, 1바이트씩 해당 숫자가 들어가있는거임. 
	// 근데 그럼 문자열은 어디까지 이어져있을까? 문자열의 끝이 어딘지 알려줘야 해석 가능하지 않을까?
	// 마지막에 마침표로 0이라는 숫자를 찍어줌 how? nul문자 
	// 그럼 0에 대응하는 문자는? nul 문자.  -> 끝났다는 마침표


	//----------------------------------
	// 1. 문자열(1)

	// 문자 
	// char(1), wchar(2)

	// 실질적으로 1바이트의 8비트는 0~255 까지지만, 맨 앞은 특정 케이스가 들어가서 0~127까지
	// 그럼 이걸 한글은 어떻게?
	// 2바이트는 2^(16-1)승이니깐...

	char c = 'a';
	//wchar_t wc = L'a'; // L은 2바이트 표현식의 약속임. 

	char szChar[10] = "abcdef";
	wchar_t szWChar[10] = L"abcdef"; // 이런 식의 L 문자열 초기화는 해당 타입만 가능
	//wchar_t szWChar[6] = L"abcdef"; 잘못된 표현임. why? abcdef 6개 말고도 끝에 nul 문자 하나를 추가해야함. 따라서 최소 7자리가 필요

	//short arrShort[10]=L"abcdef" 불가능
	short arrShort[10] = { 97,98,99,100,101,102, };
	//wchar_t wcharShort[10] = { 97,98,99,100,101,102, };
	

	// 문자열과 포인터
	//wchar_t* p_char = L"abcdef"; // 이러면 L 부분에서 빨간 줄 뜬다. 


	// swWChar은 배열, p_char은 포인터

	wchar_t szWChar[10] = L"abcdef"; // 배열
	wchar_t* p_char = L"abcdef" // 포인터. 이게 가능하려면? 문자열이 '주소'여야 한다. 
	// 포인터 선언 뒤에 오는걸 해당 값을 갖고오는 '주소'임. (문자열의 시작 주소)
		// int a=0; int*pointer = &a; => &a는 해당 값을 갖고 있는 주소를 의미함


	const wchar_t* t_char = L"abcdef"; // 포인터를 통해서 값을 못 바꾸도록. 
	// 이게 가능하다는게 시사하는 바
	// 1. 문자열은 '주소값'이다. -> 어딘가의 주소를 나한테 주는 것임(배열처럼 시작 주소를)
	// 2. L은 하나당 2바이트를 차지한다는 의미이므로, 포인터의 해석 의미도 wchar_t로 준 것.

	wchar_t szArr[10] = L"abcdef"; 
	// 얘의 의미가 이제 이해가 된다. 
	// szWChar이라는 20바이트짜리 배열에, 문자열 주소에 담겨져 있는 값들을 복사해 오는 것.

	szArr[1] = 'a';
	//pChar[1] = 'a'; == *(pChar+1)='a'
	szChar[1];

	//szWChar 과 pChar은 다르다. 
	//szWChar은 복사해서 갖고 온 값, *pChar은 원본 값. 


	//p_char[1];//이러지 마라. ROM 영역인 코드에서 메모리값을 바꾸려 하면 컴파일러가 터짐. 
	// 애초에 실행 도중에 쓰고있는 본인을(szArr에서 사용 중임) 바꿔버리는 코드는 마취 안 한 상태에서 뛰다가 쥐났다고 근육 꼬인거 푸는 꼴임.

	// 문법 자체가 틀린거는 아님. 다만 OS 딴에서 터져버리는거임.


	// 정리
	//배열 Arr은 ROM에 있는 코드 "abcdef"의 주소를 Arr에 저장하고 Arr주소에 있는 abcdef의 사본을 스택메모리에 가져와서 할당한다.
	//	포인트 Ptr은 ROM에 있는 코드 "abcdef"의 주소를 Ptr에 저장하고 Ptr주소에 있는 abcdef의 원본(ROM)에 접근한다.
	//	Arr과 Ptr의 주소값은 동일하지만, 그 기능은 사본과 원본의 차이다.ROM에 대한 포인트 접근 / 수정을 사전 차단하기 위해 문자열의 타입은 const char 형식으로 개선되었다.
	

	// 2. 문자열(2)
 	char szTest[10] = "abc한글";// a,b,c는 1바이트, 한글은 2바이트 -> 멀티바이트 시스템 
	// 근데 멀티바이트 시스템은 이제 잘 사용되지 않음.
	// why? 굳이 오류의 위험이 있는 경우를 가져가고 싶지 않음. 

	wchar_t szTestW[10] = L"abc한글"; //이제 이런 와이드바이트 시스템이 주로 사용된다. 
	//10m
	
	return 0;
}
