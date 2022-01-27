import 'dart:io';
import './utils/functions.dart';

void main(List<String> args) {
  // Example of functions usage
  print("Enter numbers to sum (separated by space): ");
  String? myInput = stdin.readLineSync();
  List<String> myList = myInput!.split(" ");

  print(calulateTotal(myList));
}
