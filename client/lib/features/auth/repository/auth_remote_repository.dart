import 'dart:convert';
import 'package:fpdart/fpdart.dart';
import 'package:http/http.dart' as http;

class AuthRemoteRepository {
  Future<Either<String, Map<String, dynamic>>> signup({
    required String email,
    required String username,
    required String password,
  }) async {
    try {
      final reponse = await http.post(
        Uri.parse("http://127.0.0.1:8000/api/v1/auth/signup"),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({
          "email": email,
          "username": username,
          "password": password,
        }),
      );
      if (reponse.statusCode != 201) {
        throw Exception("Failed to signup");
      }
      return Right(jsonDecode(reponse.body) as Map<String, dynamic>);
    } catch (e) {
      return Left(e.toString());
    }
  }

  Future<Either<String, Map<String, dynamic>>> login({
    required String email,
    required String password,
  }) async {
    try {
      final reponse = await http.post(
        Uri.parse("http://127.0.0.1:8000/api/v1/auth/login"),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({"email": email, "password": password}),
      );
      if (reponse.statusCode != 200) {
        throw Exception("Failed to login");
      }
      return Right(jsonDecode(reponse.body) as Map<String, dynamic>);
    } catch (e) {
      return Left(e.toString());
    }
  }
}
