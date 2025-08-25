class AuthState {
  final String? accessToken;
  final String? refreshToken;
  final Set<String> roles; // p.ej. {"ADMIN","USER"}
  final bool isAuthenticated;

  const AuthState({
    required this.accessToken,
    required this.refreshToken,
    required this.roles,
    required this.isAuthenticated,
  });

  factory AuthState.unauthenticated() =>
      const AuthState(accessToken: null, refreshToken: null, roles: {}, isAuthenticated: false);

  AuthState copyWith({
    String? accessToken,
    String? refreshToken,
    Set<String>? roles,
    bool? isAuthenticated,
  }) => AuthState(
    accessToken: accessToken ?? this.accessToken,
    refreshToken: refreshToken ?? this.refreshToken,
    roles: roles ?? this.roles,
    isAuthenticated: isAuthenticated ?? this.isAuthenticated,
  );
}
