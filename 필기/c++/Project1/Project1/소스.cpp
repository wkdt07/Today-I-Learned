#include <stdio.h>
int main() {
	//논리 연산자
	//!,||,&&
	// 참,거짓
	// 0이 아닌 수를 모두 참이라고 본다. 특히 1.
	// 거짓은 그냥 0 

	true;
	false;
	
	bool truefalse = false; // 굳이 따지면 정수형이긴 한데 좀 애매함
	bool isTrue = 100; // printf하면 1 -> 완전히 대응되는 개념이 아님

	// 1) 역

	isTrue = true;
	isTrue != isTrue;//뒤집은게 들어간다

	// 근데 이게 일반 정수형 자료형에도 먹힘다.

	int iTrue = 100;
	iTrue = !iTrue; // iTrue에 0이 들어간다

	// 2) 논리곱 && -> 양쪽이 모두 참이어야 한다.
	iTrue = 100 && 200; // 1
	iTrue = 0 && 200; // 0

	// 3) 논리 합
	iTrue = 0 || 100;//1
	iTrue = 1 || 100;//0

	// 주의 : 1만 참인게 아니다. 그리고 bool에 숫

	// 삼항 연산자와 비교 구문(if,else/switch,case) -> 사실상 같은 기능
	

	//5. 구문

	//1) if,else
	int data = 0;

	if (1&&200) {
		data = 200;
	}

	printf("%d", data);

	if (data==100) {
		data = 200;
	}
	else if (data==200) {
		data = 100;
	}
	else {
		data = 100;
	}

	printf("\n%d", data);
	
	// 비교 연산자
	// ==,!=,<,<=,>,>=
	
	// 2) switch case

	/*
	switch (데이터)
	{
	case 특정값:
		데이터 == 특정값 일 때 함수 실행
			break;

	case :
		~~
			break;

	// 케이스 여러개를 묶을 수도 있다,. 

	case 50:
	case 60:
	case 70:

		break;


	default: // 만약 모든 케이스에 부합하지 않을 때

		break
	}

	*/

	switch (10)
	{
	case 10:
		break;

	case 20:

		break;

	case 50:
	case 60:
	case 70:
		
		break;

	default:
		break;
	}


	int iTest = 10;
	if (iTest == 10) {

	}
	else if (iTest == 20) {

	}
	else {

	}

	// switch case 는 break가 없으면 default에 적힌 경우까지 실행한다.
	// default는 '항상 하는 것'이라고 생각하는게 편하다. => break 넣어줘야한다. 

	//3) 삼항연산자
	// if else에서 조건문을 좀 간단히 쓰고 싶을 때

	iTest == 20 ? iTest = 100 : iTest = 200; // iTest == 20이 true면 앞, 아니면 뒤를 실행
	
	// 비트연산자
	return 0;

}