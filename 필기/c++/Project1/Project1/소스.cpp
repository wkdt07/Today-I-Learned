#include <stdio.h>
int main() {
	//�� ������
	//!,||,&&
	// ��,����
	// 0�� �ƴ� ���� ��� ���̶�� ����. Ư�� 1.
	// ������ �׳� 0 

	true;
	false;
	
	bool truefalse = false; // ���� ������ �������̱� �ѵ� �� �ָ���
	bool isTrue = 100; // printf�ϸ� 1 -> ������ �����Ǵ� ������ �ƴ�

	// 1) ��

	isTrue = true;
	isTrue != isTrue;//�������� ����

	// �ٵ� �̰� �Ϲ� ������ �ڷ������� ������.

	int iTrue = 100;
	iTrue = !iTrue; // iTrue�� 0�� ����

	// 2) ���� && -> ������ ��� ���̾�� �Ѵ�.
	iTrue = 100 && 200; // 1
	iTrue = 0 && 200; // 0

	// 3) �� ��
	iTrue = 0 || 100;//1
	iTrue = 1 || 100;//0

	// ���� : 1�� ���ΰ� �ƴϴ�. �׸��� bool�� ��

	// ���� �����ڿ� �� ����(if,else/switch,case) -> ��ǻ� ���� ���
	

	//5. ����

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
	
	// �� ������
	// ==,!=,<,<=,>,>=
	
	// 2) switch case

	/*
	switch (������)
	{
	case Ư����:
		������ == Ư���� �� �� �Լ� ����
			break;

	case :
		~~
			break;

	// ���̽� �������� ���� ���� �ִ�,. 

	case 50:
	case 60:
	case 70:

		break;


	default: // ���� ��� ���̽��� �������� ���� ��

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

	// switch case �� break�� ������ default�� ���� ������ �����Ѵ�.
	// default�� '�׻� �ϴ� ��'�̶�� �����ϴ°� ���ϴ�. => break �־�����Ѵ�. 

	//3) ���׿�����
	// if else���� ���ǹ��� �� ������ ���� ���� ��

	iTest == 20 ? iTest = 100 : iTest = 200; // iTest == 20�� true�� ��, �ƴϸ� �ڸ� ����
	
	// ��Ʈ������
	return 0;

}