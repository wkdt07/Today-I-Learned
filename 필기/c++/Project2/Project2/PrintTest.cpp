//#include <stdio.h>
//
//
////void Output(const int* pI) {
////	int i = *pI;
////}
//int main() {
//	// 1. const -> 값이 안 바뀌는 상수화 하지만, 억지로라도 바꿀 수는 있다. 다만, 일부로 바꾸는 상황 자체가 잘못된거임
//	const int i = 100;
//
//	// const와 포인터
//
//	int a = 0;
//	int* pInt = &a;
//
//	*pInt = 1; // a의 값이 바뀌는거임
//	pInt = nullptr; 
//
//	// 포인트 변수는 가리키는 변수를 바꿀 수도, 가리키는 대상을 바꿀 수도 있다.
//	// 그럼 const가 포인터와 엮이면?
//	// 2가지 경우
//	// 포인터 변수가 가리키는 곳을 const로 만들지
//	// 아니면 포인터 변수 자체가 const 화 될지 -> 더 이상 가리키는 대상을 바꾸지 않는다. 
//	// const가 붙는 위치에 따라 다름
//
//	const int* pConstInt = &a; // a의 주소가 pConstInt의 포인터 주소인데, 이건 더 이상 바뀌지 않는다
//	//*pConstInt = 100;//값을 수정할 수 없음. 포인터가 '가리키는 변수'가 const화
//	//pConstInt = &a; // 이건 가능(주소 변경)
//	//printf("%d\n", *pConstInt);
//
//	int* const pIntConst = &a; // 이건 주소 자체의 상수화. 
//	//pIntConst = &i; //이건 불가능
//
//	const int* const pConstIntConst = nullptr; // 둘 다 사용도 가능 -> 가리키는 값을 바꿀 수도, 가리키는 주소를 바꿀 수도 없음.
//	
//
//	// 헷갈리면 const가 누굴 수식하고 있냐를 생각. 
//
//	// const 'int*' point -> 가리키고 있는 애를 상수화 
//	// int* const 'point' -> point를 상수화 
//
//	// int const* p = &a -> const가 수식해주는건 포인터인 * => const int* pConstInt = &a; 얘랑 똑같은 거임 -> 가리키는 대상을 상수화 
//	// 위치 기준은 별보다 뒤에 있냐 앞에 있냐. 
//
//	{
//		int a = 0;
//		const int* pInt = &a; //a가 상수화 
//		a = 100;
//		// 이게 가능하다! why? a랑은 전혀 상관이 없는 얘기임
//		// 사실 위에서처럼 얘기하면 const a랑 전혀 다를게 없음
//
//		// 얘는 그냥, 포인터 pInt a를 수정하는 행위를 막아둔 것. 
//		printf("a=%d\n", a);
//
//	}
//	// 그럼 const 포인터를 왜 씀?
//
//	// 입력받아야 할 데이터가 너무 많고 큼
//	// or 무조건 하나만 받아야 함. 
//	a = 100;
//	Output(&a);
//	// 바꿀 수는 있지만, 바꾸는게 미친 짓
//	// 그냥 바꾸지 않는다는 개발자의 의도를 표출한다고 생각. 
//
//	
//
//
//	return 0;
//}
//
//// 단축키
//// Ctrl+Shift+Space