import 'package:flutter/material.dart';

class CustomField extends StatelessWidget {
  final String hintText;
  final TextEditingController controller;
  final bool obscureText;
  const CustomField({
    super.key,
    required this.hintText,
    required this.controller,
    this.obscureText = false,
  });

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      obscureText: obscureText,
      controller: controller,
      obscuringCharacter: "*",
      validator: (value) => value == null || value.trim().isEmpty
          ? "Field cannot be empty"
          : null,
      decoration: InputDecoration(hintText: hintText),
    );
  }
}
