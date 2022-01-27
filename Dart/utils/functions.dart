int calulateTotal(List<String> myList) {
  int sum = 0;
  for (int i = 0; i < myList.length; i++) {
    if (myList[i] != "") {
      sum = sum + int.parse(myList[i]);
    }
  }
  return sum;
}

bool checkPhoneNumber(String number) {
  //TODO implement this function
  return false;
}
