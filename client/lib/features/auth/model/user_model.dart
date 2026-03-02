import 'dart:convert';

class UserModel {
  final String id;
  final String email;
  final String username;

  UserModel({required this.id, required this.email, required this.username});

  UserModel copyWith({String? id, String? email, String? username}) {
    return UserModel(
      id: id ?? this.id,
      email: email ?? this.email,
      username: username ?? this.username,
    );
  }

  Map<String, dynamic> toMap() {
    return <String, dynamic>{'id': id, 'email': email, 'username': username};
  }

  factory UserModel.fromMap(Map<String, dynamic> map) {
    return UserModel(
      id: map['id'] ?? '',
      email: map['email'] ?? '',
      username: map['username'] ?? '',
    );
  }

  String toJson() => json.encode(toMap());

  factory UserModel.fromJson(String source) =>
      UserModel.fromMap(json.decode(source) as Map<String, dynamic>);

  @override
  String toString() => 'UserModel(id: $id, email: $email, username: $username)';

  @override
  bool operator ==(covariant UserModel other) {
    if (identical(this, other)) return true;
    return other.id == id && other.email == email && other.username == username;
  }

  @override
  int get hashCode => Object.hash(id, email, username);
}
