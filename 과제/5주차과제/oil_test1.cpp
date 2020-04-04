#include "oil-openVer.h"
#include <iostream>
using namespace std;

void oil_hunt_left(int, int, int&);
void oil_hunt_right(int, int, int&);

int main() {
	initial();
	int len = oil_size();
	int begin = len-1, end = 0;
	oil_hunt_left(0, len - 1, begin);
	oil_hunt_right(0, len - 1, end);
	cout << "call observe È½¼ö : " << call_num << endl;
	oil_report(begin, end);
	return 0;
}

void oil_hunt_left(int start, int finish, int &begin) {
	if (start >= finish) return;
	int _begin = 0, _end = 0;
	int mid = (start + finish) / 2;

	int left = observe(start, mid);
	int right = 0;
	
	switch (left) {
	case 0:
		right = observe(mid + 1, finish);
		if (right == 0)
			return;
		else if (right == 1) {
			_begin = mid + 1;
			if (begin > _begin)
				begin = _begin;
		}
		else
			oil_hunt_left(mid + 1, finish, begin);
		break;
	case 1:
		_begin = start;
		if (begin > _begin)
			begin = _begin;
		break;
	case 2:
		oil_hunt_left(start, mid, begin);
		break;
	}
}

void oil_hunt_right(int start, int finish, int& end) {
	if (start > finish) return;
	int _end = 0;
	int mid = (start + finish) / 2;

	int right = observe(mid + 1, finish);
	int left = 0;

	switch (right) {
	case 0:
		left = observe(start, mid);
		if (left == 0)
			return;
		else if (left == 1) {
			_end = mid;
			if (end < _end)
				end = _end;
		}
		else
			oil_hunt_right(start, mid, end);
		break;
	case 1:
		_end = finish;
		if (end < _end)
			end = _end;
		break;
	case 2:
		oil_hunt_right(mid + 1, finish, end);
		break;
	}
}
